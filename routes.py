from mysite import app
from flask import render_template,session,request,flash

@app.route('/')
def home(actor=None):
    actor =actor or ''
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html',actor=actor)
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    user='' 
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
        user = 'admin'
    else:
        flash('wrong password!')
        user = None 
    return home(user)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
