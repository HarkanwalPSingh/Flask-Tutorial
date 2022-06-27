from datetime import date, datetime, timedelta
from flask import Flask, make_response, render_template, session, request, jsonify
import jwt

app = Flask(__name__)

app.config['SECRET_KEY'] = 'gp-GiePfwdL0Ad-ollM'

# UUID Approach
# import uuid
# uuid.uuid4().hex
# Secrets [ only for Python 3.6 + ]
#import secrets
# secrets.token_urlsafe(14)


@app.route("/")
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('dashboard.html')


@app.route("/login", methods=['POST'])
def login():
    if request.form['email'] and request.form['password'] == 'test':
        session['logged_in'] = True

        token = jwt.encode(
            {
                'user': request.form['email'],
                'expiration': str(datetime.utcnow() + timedelta(seconds=60))
            },
                app.config['SECRET_KEY']
        )
        return token
    
    else:
        return make_response('Not verified', 403, {'WWW-Authenticate': 'Basic realm: "Authentication Failed"'})

if __name__ == "__main__":
    app.run(debug=True)