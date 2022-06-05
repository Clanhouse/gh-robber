from forgery_py.forgery.internet import user_name
from github import Github
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.operators import isnot
from . import db
from app.models import GithubUserInfo, GithubRepositories
from datetime import datetime
from os import path
import logging
import os
import time


"""
    To do:
        add file 'GH_access_token.txt' to 'backend/app' with github access token 
        token must be without '' and ""
"""

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(
    filename="GH_API_handling_logs.log", level=logging.INFO, format=LOG_FORMAT
)
logger = logging.getLogger()

with open("./app/GH_access_token.txt") as f:
    GH_access_token = f.read().strip()


class Scraping:
    gh_scraping_running = True
    last_scraped_user_name = None
    last_scraped_user_timestamp = None
    last_scraped_repo_name = None
    last_scraped_repo_timestamp = None

    def user_is_in_db(self, usrname=None):
        """Check if the user with usrname is in database"""
        found_user = GithubUserInfo.query.filter_by(username=usrname).first()

        if found_user:
            logger.debug(f"User {usrname} has been found in database")
            return True
        else:
            return False

    def repo_is_in_db(self, repo_name=None):
        """Check if the repository with repo_name is in database"""
        found_repo = GithubRepositories.query.filter_by(reponame=repo_name).first()

        if found_repo:
            logger.debug(f"Repository {repo_name} has been found in database")
            return True
        else:
            return False

    def update_repo(self, repo_name=None):
        """Updates repository names repo_name"""
        if repo_name != None:
            if self.repo_is_in_db(repo_name):
                g = Github(str(GH_access_token))
                repo_to_update = GithubRepositories.query.filter_by(
                    reponame=repo_name
                ).first()
                repo = g.get_repo(repo_name)

                contributors_objs_list = []

                for contributor in repo.get_contributors():
                    while self.gh_scraping_running == False:
                        time.sleep(10)
                    if (
                        contributor.login != "None"
                        and self.user_is_in_db(contributor.login) == False
                    ):
                        gh_user = self.add_user_to_database(
                            contributor.login, return_added_user=True
                        )
                        contributors_objs_list.append(gh_user)
                    elif (
                        contributor.login != "None"
                        and self.user_is_in_db(contributor.login) == True
                    ):
                        user_from_db = GithubUserInfo.query.filter_by(
                            username=contributor.login
                        ).first()
                        contributors_objs_list.append(user_from_db)

                repo_to_update.languages = repo.get_languages()  # dict
                repo_to_update.last_update = datetime.today().date()
                repo_to_update.topics = repo.get_topics()  # list
                repo_to_update.stars = repo.stargazers_count  # int
                repo_to_update.has_sourced_users = True
                repo_to_update.contributors = contributors_objs_list  # list of objects
                try:
                    db.session.commit()
                    return logger.info(
                        f"Repo {repo_name} has been successfully updated"
                    )

                except IntegrityError:
                    db.session.rollback()
                    return logger.exception(
                        f"Exception while updating repo {repo_name}"
                    )

    def update_user_info(self, usrname=None):
        """Updates user_info of user named usrname"""
        if usrname != None:
            if self.user_is_in_db(usrname):
                g = Github(str(GH_access_token))
                user = g.get_user(usrname)
                sourced_repos = []
                for repo in user.get_repos():
                    while self.gh_scraping_running == False:
                        time.sleep(10)
                    added_repo = self.add_repo_to_database(
                        repo.full_name, return_added_repo=True
                    )
                    sourced_repos.append(added_repo)

                user_to_update = GithubUserInfo.query.filter_by(
                    username=usrname
                ).first()
                user_to_update.last_update = datetime.today().date()
                user_to_update.repositories = sourced_repos

                try:
                    db.session.commit()
                    return logger.info(f"Repo {usrname} has been successfully updated")

                except IntegrityError:
                    db.session.rollback()
                    return logger.exception(f"Exception while updating user {usrname}")

    def add_repo_to_database(self, repo_name=None, return_added_repo=False):
        """
        Adds repository from github to database - it doesn't add contributors of the repo to prevent infinite loop.
        To add all contributors of repositories, use function fill_repos_with_users()
        """

        if repo_name != None:
            if self.repo_is_in_db(repo_name) and return_added_repo == False:
                return logger.info(f"Repo {repo_name} is already in database")
            if self.repo_is_in_db(repo_name) and return_added_repo == True:
                logger.info(f"Repo {repo_name} is already in database")
                return GithubRepositories.query.filter_by(reponame=repo_name).first()
            else:
                while self.gh_scraping_running == False:
                    time.sleep(10)
                g = Github(str(GH_access_token))
                repo = g.get_repo(repo_name)

                repo_info = GithubRepositories(
                    id=None,
                    reponame=repo_name,  # str
                    languages=repo.get_languages(),  # dict
                    last_update=datetime.today().date(),
                    topics=repo.get_topics(),  # list
                    stars=repo.stargazers_count,  # int
                    has_sourced_users=False,
                )

                db.session.add(repo_info)

                if return_added_repo == False:
                    try:
                        db.session.commit()
                        self.last_scraped_repo_name = repo_name
                        self.last_scraped_repo_timestamp = datetime.now()
                        return logger.info(
                            f"Repo {repo_name} has been successfully added"
                        )

                    except IntegrityError:
                        db.session.rollback()
                        return logger.exception(
                            f"Exception while adding repo: {repo_name}"
                        )
                elif return_added_repo == True:
                    try:
                        db.session.commit()
                        self.last_scraped_repo_name = repo_name
                        self.last_scraped_repo_timestamp = datetime.now()
                        logger.info(f"Repo {repo_name} has been successfully added")
                        return repo_info

                    except IntegrityError:
                        db.session.rollback()
                        return logger.exception(
                            f"Exception while adding repo: {repo_name}"
                        )
        else:
            pass

    def add_user_to_database(self, username=None, return_added_user=False):
        """Add user from GH to database. It also adds all the repositories of the user"""
        if username != None:
            g = Github(str(GH_access_token))
            if self.user_is_in_db(username) and return_added_user == False:
                return logger.info(f"User {username} is already in database")
            elif self.user_is_in_db(username) and return_added_user == True:
                logger.info(f"User {username} is already in database")
                return GithubUserInfo.query.filter_by(username=username).first()
            else:
                user = g.get_user(username)
                sourced_repos = []

                for repo in user.get_repos():
                    while self.gh_scraping_running == False:
                        time.sleep(10)
                    if self.repo_is_in_db(repo.full_name):
                        added_repo = GithubRepositories.query.filter_by(
                            reponame=repo.full_name
                        ).first()
                        sourced_repos.append(added_repo)
                    elif self.repo_is_in_db(repo.full_name) == False:
                        added_repo = self.add_repo_to_database(
                            repo.full_name, return_added_repo=True
                        )
                        sourced_repos.append(added_repo)

                user_info = GithubUserInfo(
                    username=username,
                    last_update=datetime.today().date(),
                    repositories=sourced_repos,
                )

                db.session.add(user_info)

            if return_added_user == False:
                try:
                    db.session.commit()
                    self.last_scraped_user_name = username
                    self.last_scraped_user_timestamp = datetime.now()
                    return logger.info(f"User {username} has been successfully added")

                except IntegrityError:
                    db.session.rollback()
                    return logger.exception(f"Exception while adding user: {username}")
            elif return_added_user == True:
                try:
                    db.session.commit()
                    self.last_scraped_user_name = username
                    self.last_scraped_user_timestamp = datetime.now()
                    logger.info(f"User {username} has been successfully added")
                    return user_info

                except IntegrityError:
                    db.session.rollback()
                    return logger.exception(f"Exception while adding user: {username}")
        else:
            pass

    def fill_repos_with_users(self):
        """Fills repositories that don't have all the contributors sourced from GH"""
        repos_to_update = GithubRepositories.query.filter(
            GithubRepositories.has_sourced_users == False
        )
        for repo in repos_to_update:
            while self.gh_scraping_running == False:
                time.sleep(10)
            self.update_repo(repo.reponame)
        logger.debug("Func fill_repos_with_users ended.")

    def update_all_users(self, older_than=None):
        """
        Updates all users - older_than parameter allows to update users that have been updated before given date.
        Required form of date: YYYY-MM-DD
        """
        if older_than == None:
            users_to_update = GithubUserInfo.query.all()
        elif older_than != None:
            users_to_update = GithubUserInfo.query.filter(
                GithubUserInfo.last_update < older_than
            )
        for user in users_to_update:
            while self.gh_scraping_running == False:
                time.sleep(10)
            self.update_user_info(user.username)
        logger.debug("Func update_all_users ended.")

    def update_all_repos(self, older_than=None):
        """
        Updates all repositories - older_than parameter allows to update repositories that have been updated before given date.
        Required form of date: YYYY-MM-DD
        """
        if older_than == None:
            repos_to_update = GithubRepositories.query.all()
        elif older_than != None:
            repos_to_update = GithubRepositories.query.filter(
                GithubRepositories.last_update < older_than
            )
        for repo in repos_to_update:
            while self.gh_scraping_running == False:
                time.sleep(10)
            self.update_repo(repo.reponame)
        logger.debug("Func update_all_repos ended.")

    def auto_scraping_GH(self):
        """
        Function adds repos from GH_seed_repos.txt and users from GH_seed_users.txt to database.
        Then it starts infinite loop to continiously scrape GH for repos and users
        """

        GH_repos_seed_path = os.environ.get("GH_REPOS_SEED_PATH")
        GH_users_seed_path = os.environ.get("GH_USERS_SEED_PATH")

        if GH_repos_seed_path != None:
            GH_repos_seed_file_exists = path.exists(GH_repos_seed_path)
        else:
            GH_repos_seed_file_exists = False

        if GH_users_seed_path != None:
            GH_users_seed_file_exists = path.exists(GH_users_seed_path)
        else:
            GH_users_seed_file_exists = False

        GH_seed_repos_list = []
        GH_seed_users_list = []

        if GH_repos_seed_file_exists:
            logger.debug("File GH_seed_repos.txt has been found.")

            with open(GH_repos_seed_path) as repos_file:
                for repo in repos_file:
                    line = repo.rstrip()
                    if not line.startswith("#"):
                        if line != "":
                            GH_seed_repos_list.append(line)
                            logger.info(f"Repo {line} is loaded from seed file.")

        if GH_users_seed_file_exists:
            logger.debug(f"File GH_seed_users.txt has been found.")

            with open(GH_users_seed_path) as users_file:
                for user in users_file:
                    line = user.rstrip()
                    if not line.startswith("#"):
                        if line != "":
                            GH_seed_users_list.append(line)
                            logger.info(f"User {line} is loaded from seed file.")

        for repo in GH_seed_repos_list:
            try:
                self.add_repo_to_database(repo)
            except:
                logger.exception(f"Exception while getting repo from seed file: {repo}")
        for user in GH_seed_users_list:
            try:
                self.add_user_to_database(user)
            except:
                logger.exception(f"Exception while getting user from seed file: {user}")

        logger.info("Infinite loop in auto_scraping_script initiated.")
        while True:
            if self.gh_scraping_running == True:
                self.fill_repos_with_users()
            elif self.gh_scraping_running == False:
                time.sleep(10)
