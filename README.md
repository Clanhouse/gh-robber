# Github Robber

Github robber is an application that collects profiles on Github, ranks
and makes them available to recruiters in the form of subscription.

### How to start application with docker
1. Navigate to `backend` folder.
2. Type in terminal `docker-compose up`.
3. Open `localhost:5000` with your browser to see the result.

### How to start application

1. Navigate to `backend` folder.
2. Type in terminal `pip install -r requirements.txt`
3. Right click on the `gh_robber.py` file and then click `run` or run from the terminal
   
   On Windows: `set FLASK_APP=gh_robber.py`

   On Linux: `export FLASK_APP=gh_robber.py`

5. Type in terminal `flask db init`
6. Type in terminal `flask upgrade` if the data is already in the database
7. Type in terminal `flask run`

### How to create fake data

1. Navigate to backend/app folder
1. `flask db-manage add-data`

### How to remove fake data

1. Navigate to backend/app folder
1. `flask db-manage remove-data`

### How to run automatic data scraping from gh

1. Navigate to `backend/app folder`
2. Update file named `GH_seed_repos.txt` - list of repos to scrape (optional)
3. Update file named `GH_seed_users.txt` - list of users to scrape (optional)
4. Navigate to `backend` folder
5. Type in terminal `flask db-manage auto-scraping`
6. To stop this process press kill the terminal

### How to run tests

To execute the tests located in the tests/ folder, navigate to the backend folder and run the command:
`python -m pytest tests/`

## Start client side app

Download files and instal dependencies :

yarn install

Then, run the development server:

```bash
yarn dev
```

Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) with your browser to see the result.
