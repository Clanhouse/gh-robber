from github import Github
from sqlalchemy.exc import IntegrityError
from random import seed, randint, choice
from . import db
from app.models import GithubUserInfo, GithubUserInfoSchema
from datetime import datetime, timedelta


"""
    To do:
        add file 'GH_access_token.txt' to 'backend/app' with github access token 
        token must be without ' and " 

    search_for_repositories(
        language  - string  technology name example: python
        time      - int     days before now to scrap
        stars     - int     maximum stars for searching repository \
            to stars may be used maths characters example "<=20" then must be string type  
    )
    
    search_for_user(
        username  - string  search user by name
    )
    
"""

with open("./app/GH_access_token.txt") as f:
        GH_access_token = f.read().strip()    
    

# example search_for_repositories('python', 5, '>20')
def search_for_repositories(language=None, days=None, stars_count=None):
    
    g = Github(str(GH_access_token))
    
    time_delta = ((datetime.now() - timedelta(days=int(days))).strftime('%Y-%m-%d'))
    
    repositories = g.search_repositories(
        query="language:{technology} created:<{time_delta} stars:{stars_count}".format(technology=str(language), 
                                                                                 time_delta=time_delta, 
                                                                                 stars_count=str(stars_count))
    )
    
    for repo in repositories:
        
        found_user = GithubUserInfo.query.filter_by(username=repo.owner.login, repository=repo.name).first()
        if found_user:
            print("User {user}'s already exists").format(repo.owner.login)
            
        else:
        
            user_info = GithubUserInfo(
                username=repo.owner.login,
                repository=repo.name,
                language=repo.language,
                date=repo.created_at,
                stars=repo.stargazers_count,  # !!! stars of repo not user !!!
                number_of_repositories=g.get_user(repo.owner.login).public_repos,
            )
            
            db.session.add(user_info)
        
        

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        

# example search_for_user('orzeech')
def search_for_user(username=None):
    
    g = Github(str(GH_access_token))
    
    repository = g.search_repositories(
        query=("user:{username}").format(username=str(username))
    )    
        
                                      
    for repo in repository:
        
        found_user = GithubUserInfo.query.filter_by(username=repo.owner.login, repository=repo.name).first()
        if found_user:
            pass
            
        else:
            
            user_info = GithubUserInfo(
                username=repo.owner.login,
                repository=repo.name,
                language=str(repo.language),
                date=repo.created_at,
                stars=repo.stargazers_count,  # !!! stars of repo not user !!!
                number_of_repositories=g.get_user(repo.owner.login).public_repos,
            )
            
            db.session.add(user_info)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
