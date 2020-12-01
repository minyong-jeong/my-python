from datetime import timedelta
from flask import Flask, session, redirect, url_for, request
from markupsafe import escape

app = Flask(__name__)

app.secret_key = b'SeCrEt_KeY'

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/')
def index():
    if 'username' in session:
        return '''
        <p>Logged in as %s</p>
        <a href="/logout">Logout!</p>
        ''' % escape(session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return '''
        <p>Logged out!!</p>
        <a href="/">Go home!</a>
    '''

if __name__ ==  "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
