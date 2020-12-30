# A discovery task 

1- git clone https://github.com/miguelgrinberg/flasky.git 

    -- check the structure of the flask app that u have installed. what do u think?

    -- now let's return back to an application format we are more familiar with 

2- cd into flasky  

3- git checkout 6a 

Now we can divide tasks for members in breakout rooms: 

### Member 1: 

Read how to handle configurations  https://hackersandslackers.com/configure-flask-applications/ 

how can we safely store secret info without having to repeat "Export" to the environment ? 

### Member 2: 

how can we convert the structure of this app into the structure in the picture in the repo ? 
https://hackersandslackers.com/flask-application-factory 

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure 

done ? check solution: 
make a copy of your local repo

in terminal 
git reset --hard  ==> this will erase all u have done 
git checkout 7a 

### Member 3: 

He is using Flask-mail, but sending an email may be a slow process. Can you make it faster using threads?    Hint: use *from threading import Thread*

done ?  check solution :    
make a copy of your local repo 

in terminal 
git reset --hard  ==> this will erase all u have done 
git check 6b 

### Member 4:

How can we use Flask-celery for running background tasks? https://blog.miguelgrinberg.com/post/using-celery-with-flask 

