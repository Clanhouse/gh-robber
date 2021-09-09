# Github Robber
Github robber is an application that collects profiles on Github, ranks 
and makes them available to recruiters in the form of subscription.

### How to start application
1. Navigate to backend/app folder
1. ```pip install -r requirements.txt```

1. ```Right click on the gh_robber.py file and then click "run".```
   
   ```or run from the terminal```

   On Windows: ```set FLASK_APP=gh_robber.py```
   
   On Linux: ```export FLASK_APP=gh_robber.py```
1. ``` "flask db init" ```
1. ``` "flask deploy" or "flask upgrade" if the data is already in the database```   
1. ```flask run```

### How to create fake data
1. Navigate to backend/app folder
1. ```flask db-manage add-data```

### How to create fake data
1. Navigate to backend/app folder
1. ```flask db-manage remove-data```


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

Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) with your browser to see the result.
