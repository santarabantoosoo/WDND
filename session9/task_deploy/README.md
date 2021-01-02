# Heroku walk thru 

1 - download and install heroku CLI ... It will take time.. 

*Windows/Mac/linux*    https://devcenter.heroku.com/articles/heroku-cli#download-and-install 

*WSL*   https://dev.to/wrightdotclick/heroku-cli-on-wsl-26fp 

2- after installment, run app.py locally using python3 app.py 

3- sign up for free heroku account and create an app 

4- login into heroku using *heroku login* 

5- in the home directory, *git init* 

6- *heroku git:remote -a [ur-app-name]    --> the one u named in step 3 

7- Add a Procfile ==> note that it has no extension. Just Procfile

    -- write in the file *web: gunicorn app:app*     
    
    -- web: waitress-serve --port=$PORT flasky:app         for windows
    
8-  in ur terminal: 
    a- pipenv install flask gunicorn   
    b- pipenv shell   
    c- git add .  
    d- git commit -m "initial commit"  
    e- git push heroku master   


### External Links  

https://medium.com/@abhishekori/damn-simple-flask-app-on-heroku-739948512c65 a very simple app

https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0 including database in deployment 







