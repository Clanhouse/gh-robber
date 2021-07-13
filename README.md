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

There is also possibility to define desired number of fake data to be created for each table
(default is 10).
To do that, add ```--count NUMBER_OF_FAKE_DATA``` to upper command.

## Start client side app

Download files and instal dependencies :

npm install
or
yarn install

Then, run the development server:

```bash
npm run dev
# or
yarn dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.
