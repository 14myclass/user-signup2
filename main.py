from flask import Flask,request,redirect
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

signup_form="""
<!DOCTYPE html>
<html>
<style>
    .error{{color: red;}}
</style>
<body>
<h1>SIGN UP FORM</h1>
<form method='POST'>
    <label>USERNAME:
        <input name="username" type="text" value='{username}' />
    </label>
    <span class="error">{username_error}</span><br>
    <p><label>PASSWORD:
        <input name="password" type="password" value='{password}' />
    </label>
    <span class="error">{password_error}</span></p>
     <p><label>VERIFY PASSWORD:
        <input name="verify_password" type="password" value='{verify_password}' />
    </label>
    <span class="error">{verify_password_error}</span></p>
    <p><input type="submit" /></p>
</form>
</body>
</html>
"""

#displays form
@app.route("/validate")
def index():
    return signup_form.format(username="", username_error="",password="",password_error="",verify_password="", verify_password_error="")

#function to validate the inputs
@app.route("/validate", methods=['POST'])
def validate():
    username=request.form['username']
    username_error=""
    password=request.form['password']
    password_error=""
    verify_password=request.form['verify_password']
    verify_password_error=""




    #checking validity of inputs
    if len(username) < 3 or len(username) >20 or username=="":
        username_error="Please enter a valid name."
        
    if len(password) < 3 or len(password) >20 or password=="":
        password_error="Enter a valid password."
    if len(verify_password) < 3 or len(verify_password) >20 or verify_password=="" or verify_password != password :
        verify_password_error="Password does not match."
        
     #rendering form with error messages   
    if not username_error and not password_error and not verify_password_error:
        return '<h1>Welcome</h1>'
    elif not username_error and password_error and not verify_password_error:
        return signup_form.format(username=username, username_error="",password="",password_error=password_error,verify_password="",verify_password_error="")
    elif not username_error and not password_error and verify_password_error:
        return signup_form.format(username=username, username_error="",password="",password_error="",verify_password="",verify_password_error=verify_password_error)
    elif username_error and not password_error and verify_password_error:
        return signup_form.format(username="", username_error=username_error,password="",password_error="",verify_password="",verify_password_error=verify_password_error) 
    elif username_error and not password_error and not verify_password_error:
        return signup_form.format(username="", username_error=username_error,password="",password_error="",verify_password="",verify_password_error="")
    elif username_error and password_error and not verify_password_error:
        return signup_form.format(username="", username_error=username_error,password="",password_error=password_error,verify_password="",verify_password_error="")
    elif username_error and password_error and verify_password_error:
         return signup_form.format(username="", username_error=username_error,password="",password_error=password_error,verify_password="",verify_password_error=verify_password_error)



app.run()