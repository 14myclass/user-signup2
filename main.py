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
    #verify_password=request.form['verify_password']
    #verify_password_error=""
    #email=request.form['email']
    #email_error=""




    #checking validity of inputs
    if len(username) < 3 or len(username) >20 or username=="":
        username_error="Please enter a valid name."
    for each in username:
        if each == " ":
            username_error="Please enter a valid name."
    #if not username_error:
        #return render_template('welcome.html', name=username )
    #else:
        #return render_template('signup_form.html', error=username_error)
 
    if len(password) < 3 or len(password) >20 or password=="":
        password_error="Enter a valid password."
    for each in password:
        if each == " ":
            password_error="Enter a valid password."
    if not username_error and not password_error:
        return render_template('welcome.html', name=username )
    elif not username_error and password_error:
        return render_template('signup_form.html', username=username, password_error=password_error)
    elif username_error and not password_error:
        return render_template('signup_form.html', username_error=username_error)
    else:
        return render_template('signup_form.html', username_error=username_error, password_error=password_error)
            

    #if len(verify_password) < 3 or len(verify_password) >20 or verify_password=="" or verify_password != password :
        #verify_password_error="Password does not match."
    #for each in verify_password:
        #if each == " ":
            #verify_password_error="Password does not match."
    
    #if email != "":
        #for each in email:
            #if each != "@" and each != ".":
                #email_error="Please enter a valid email address"
   
     #rendering form with error messages   
    #if not username_error and not password_error and not verify_password_error and not email_error:
       # return render_template('welcome.html')                                           
    #elif not username_error and password_error and not verify_password_error:
        #return signup_form.format(username=username, username_error="",password="",password_error=password_error,verify_password="",verify_password_error="")
    #elif not username_error and not password_error and verify_password_error:
        #return signup_form.format(username=username, username_error="",password="",password_error="",verify_password="",verify_password_error=verify_password_error)
    #elif username_error and not password_error and verify_password_error:
        #return signup_form.format(username="", username_error=username_error,password="",password_error="",verify_password="",verify_password_error=verify_password_error) 
    #elif username_error and not password_error and not verify_password_error:
        #return signup_form.format(username="", username_error=username_error,password="",password_error="",verify_password="",verify_password_error="")
    #elif username_error and password_error and not verify_password_error:
        #return signup_form.format(username="", username_error=username_error,password="",password_error=password_error,verify_password="",verify_password_error="")
    #elif username_error and password_error and verify_password_error:
         #return signup_form.format(username="", username_error=username_error,password="",password_error=password_error,verify_password="",verify_password_error=verify_password_error)
    

    
#@app.route('/valid-inputs')
#def valid_inputs():
    #username=request.args.get('username')
    #return render_template('welcome.html')

app.run()