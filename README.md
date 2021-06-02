# Github Robber
Github robber is an application that collects profiles on Github, ranks 
and makes them available to recruiters in the form of subscription.

### How to start application
1. Navigate to backend/app folder
1. ```pip install -r requirements.txt```
1. 
   On Windows: ```set FLASK_APP=gh_robber.py```
   
   On Linux: ```export FLASK_APP=gh_robber.py```
1. ```flask db init```
1. ```flask deploy```   
1. ```flask run```

### How to create fake data
1. Navigate to backend/app folder
1. ```flask create_fake_data```