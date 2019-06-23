# Django  
## Library Online Management System written in Django - CSOC :octocat:  

To get this project up and running locally on your computer:

1. Set up the Python development environment. We recommend using a Python virtual environment.    
2. Assuming you have Python setup, run the following commands (if you're on Windows you may use py or py -3 instead of python to start Python):    
  pip3 install -r requirements.txt    
  python3 manage.py makemigrations    
  python3 manage.py migrate    
  python3 manage.py collectstatic    
  python3 manage.py test # Run the standard tests. These should all pass.    
  python3 manage.py createsuperuser # Create a superuser    
  python3 manage.py runserver    
3. Open a browser to http://127.0.0.1:8000/admin/ to open the admin site.   
4. Create a few test objects of each type.    
5. Open tab to http://127.0.0.1:8000 to see the main site, with your new objects.  

![](http://www.upl.co/uploads/robocroprealpython1561243600.jpeg)    

Technologies: django, python, html, css, Java Script, jQuery, Twitter Bootstrap, Git, Heroku.  
**Date:** 23 june 2019. 
> It is an online interface for a library and allows users to:  
* borrow/return books (like in real library) (a few books are present in the system).    
* search for a given book by title or author or genre. 
  
**Exemplary system accounts:**

admin account:  
  
login: yashraj  
pass: learncode  
  
standard user:  
  
login: Peter  
pass: learncode  

(do not forget to change database settings if you want to run app locally) or simply visit website: https://yash-library-web.herokuapp.com
