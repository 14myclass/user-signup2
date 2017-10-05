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
<h1>SIGN UP FORM</h1>
<form method='POST'>
    <label>USERNAME:
        <input name="username" type="text" value='{username}' />
    </label>
    <span class="error">{username_error}</span>
    <p><input type="submit" /></p>
</form>
</html>
"""

#displays form
@app.route("/validate")
def index():
    return signup_form.format(username="", username_error="")

#function to validate the inputs
@app.route("/validate", methods=['POST'])
def validate():
    username=request.form['username']
    username_error=""




    if len(username) < 3 or len(username) >20 or username=="":
        username_error="Please enter a valid name."
        return signup_form.format(username="", username_error=username_error)
    else:
        return '<h1>Welcome</h1>'

app.run()