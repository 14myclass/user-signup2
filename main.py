from flask import Flask, request, redirect, render_template
import cgi
import os



app = Flask(__name__)
app.config['DEBUG'] = True



#displays form
@app.route("/validate")
def index():
    return render_template('signup_form.html')

#function to validate the inputs
@app.route("/validate", methods=['POST'])
def validate():
    username=request.form['username']
    
    username_error=""
    password=request.form['password']
    password_error=""
    verify_password=request.form['verify_password']
    verify_password_error=""
    email=request.form['email']
    email_error=""




    #checking validity of username
    if username !="":
        if len(username) < 3 or len(username) >20:
            username_error="Username needs to be between 3-20 characters."
        for each in username:
            if each == " ":
                username_error="Enter a username without spaces."
    else:
        username_error = "Please enter a username."

    #check validity of password
    if password !="":
        if len(password) < 3 or len(password) >20:
            password_error="Enter a valid password between 3-20 characters."
        for each in password:
            if each == " ":
                password_error="Enter a password without spaces."
    else:
        password_error="Please enter a password."

    #check password confirmation
            
    if verify_password !="":
        if len(verify_password) < 3 or len(verify_password) >20 or verify_password != password :
            verify_password_error="Password does not match."
        for each in verify_password:
            if each == " ":
                verify_password_error="Password does not match."
    else:
        verify_password_error = "Please confirm the password. "

    #check if email valid
    if email != "":
        if len(email) >= 3 and len(email) <=20 :
            for each in email:
                if each !=" ":
                    if "@" in email and "." in email:
                        email_error=""
                    else:
                        email_error="Enter a valid email address."
        else:
            email_error="Enter an email address between 3-20 characters."

     #rendering form with error messages   
    if not username_error and not password_error and not verify_password_error and not email_error:
        return render_template('welcome.html', name=username)                                           
    
    else: 
        return render_template('signup_form.html', username_error=username_error, password_error=password_error, verify_password_error=verify_password_error,email_error=email_error,email=email,username=username)
         
    

    
app.run()