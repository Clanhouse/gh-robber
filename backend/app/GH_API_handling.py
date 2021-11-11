from forgery_py.forgery.internet import user_name
from github import Github
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.operators import isnot
from . import db
from app.models import GithubUserInfo, GithubRepositories
from datetime import datetime
import logging


"""
    To do:
        add file 'GH_access_token.txt' to 'backend/app' with github access token 
        token must be without '' and ""
"""

LOG_FORMAT = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig(
    filename="*\\GH_API_handling_logs.log", level=logging.INFO, format=LOG_FORMAT
)
logger = logging.getLogger()

with open("./app/GH_access_token.txt") as f:
    GH_access_token = f.read().strip()


def user_is_in_db(usrname=None):
    """Check if the user with usrname is in database"""
    found_user = GithubUserInfo.query.filter_by(username=usrname).first()

    if found_user:
        logger.debug(f"User {usrname} has been found in database")
        return True
    else:
        return False


def repo_is_in_db(repo_name=None):
    """Check if the repository with repo_name is in database"""
    found_repo = GithubRepositories.query.filter_by(reponame=repo_name).first()

    if found_repo:
        logger.debug(f"Repository {repo_name} has been found in database")
        return True
    else:
        return False


def update_repo(repo_name=None):
    """Updates repository names repo_name"""
    if repo_name != None:
        if repo_is_in_db(repo_name):
            g = Github(str(GH_access_token))
            repo_to_update = GithubRepositories.query.filter_by(
                reponame=repo_name
            ).first()
            repo = g.get_repo(repo_name)

            contributors_objs_list = []

            for contributor in repo.get_contributors():
                if (
                    contributor.login != "None"
                    and user_is_in_db(contributor.login) == False
                ):
                    gh_user = add_user_to_database(
                        contributor.login, return_added_user=True
                    )
                    contributors_objs_list.append(gh_user)
                elif (
                    contributor.login != "None"
                    and user_is_in_db(contributor.login) == True
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
                return logger.info(f"Repo {repo_name} has been successfully updated")

            except IntegrityError:
                db.session.rollback()
                return logger.exception(f"Exception while updating repo {repo_name}")


def update_user_info(usrname=None):
    """Updates user_info of user named usrname"""
    if usrname != None:
        if user_is_in_db(usrname):
            g = Github(str(GH_access_token))
            user = g.get_user(usrname)
            sourced_repos = []
            for repo in user.get_repos():
                added_repo = add_repo_to_database(
                    repo.full_name, return_added_repo=True
                )
                sourced_repos.append(added_repo)

            user_to_update = GithubUserInfo.query.filter_by(username=usrname).first()
            user_to_update.last_update = datetime.today().date()
            user_to_update.repositories = sourced_repos

            try:
                db.session.commit()
                return logger.info(f"Repo {usrname} has been successfully updated")

            except IntegrityError:
                db.session.rollback()
                return logger.exception(f"Exception while updating user {usrname}")


def add_repo_to_database(repo_name=None, return_added_repo=False):
    """
    Adds repository from github to database - it doesn't add contributors of the repo to prevent infinite loop.
    To add all contributors of repositories, use function fill_repos_with_users()
    """

    if repo_name != None:
        if repo_is_in_db(repo_name) and return_added_repo == False:
            return f"Repo {repo_name} is already in database"
        if repo_is_in_db(repo_name) and return_added_repo == True:
            print(f"Repo {repo_name} is already in database")
            return GithubRepositories.query.filter_by(reponame=repo_name).first()
        else:
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
                    return logger.info(f"Repo {repo_name} has been successfully added")

                except IntegrityError:
                    db.session.rollback()
                    return logger.exception(f"Exception while adding repo: {repo_name}")
            elif return_added_repo == True:
                try:
                    db.session.commit()
                    logger.info(f"Repo {repo_name} has been successfully added")
                    return repo_info

                except IntegrityError:
                    db.session.rollback()
                    return logger.exception(f"Exception while adding repo: {repo_name}")
    else:
        pass


def add_user_to_database(username=None, return_added_user=False):
    """Add user from GH to database. It also adds all the repositories of the user"""
    if username != None:
        g = Github(str(GH_access_token))
        if user_is_in_db(username) and return_added_user == False:
            return f"User {username} is already in database"
        elif user_is_in_db(username) and return_added_user == True:
            print(f"User {username} is already in database")
            return GithubUserInfo.query.filter_by(username=username).first()
        else:
            user = g.get_user(username)
            sourced_repos = []

            for repo in user.get_repos():
                if repo_is_in_db(repo.full_name):
                    added_repo = GithubRepositories.query.filter_by(
                        reponame=repo.full_name
                    ).first()
                    sourced_repos.append(added_repo)
                elif repo_is_in_db(repo.full_name) == False:
                    added_repo = add_repo_to_database(
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
                return logger.info(f"User {username} has been successfully added")

            except IntegrityError:
                db.session.rollback()
                return logger.exception(f"Exception while adding user: {username}")
        elif return_added_user == True:
            try:
                db.session.commit()
                logger.info(f"User {username} has been successfully added")
                return user_info

            except IntegrityError:
                db.session.rollback()
                return logger.exception(f"Exception while adding user: {username}")
    else:
        pass


def fill_repos_with_users():
    """Fills repositories that don't have all the contributors sourced from GH"""
    repos_to_update = GithubRepositories.query.filter(
        GithubRepositories.has_sourced_users == False
    )
    for repo in repos_to_update:
        update_repo(repo.reponame)
    logger.debug("Func fill_repos_with_users ended.")


def update_all_users(older_than=None):
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
        update_user_info(user.username)
    logger.debug("Func update_all_users ended.")


def update_all_repos(older_than=None):
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
        update_repo(repo.reponame)
    logger.debug("Func update_all_repos ended.")
