import functools
import logging
logging.basicConfig(level=logging.DEBUG)
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, session
)
from werkzeug.security import check_password_hash, generate_password_hash
import psycopg2
from flaskr.db import get_db
import sys
bp = Blueprint('auth', __name__, url_prefix='/auth')
@bp.route('/', methods=('GET', 'POST'))
def index():
    return render_template('auth.html')
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        print("hello",file=sys.stderr)
        username = request.form['username']
        password = request.form['password']
        print(username)
        db = get_db()
        cur = db.cursor()
        
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                cur.execute(
                    "INSERT INTO profile (user_id, password) VALUES (%s, %s)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
                cur.close()
                db.close()
                
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                session['user_id'] = request.form['username']
                return redirect(url_for('profile.index'))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cur = db.cursor()
        error = None
        sql = f"SELECT * FROM profile WHERE user_id = '{username}'"
        cur.execute(sql)
        user = cur.fetchone()
        print("name",user)

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user[1], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user[0]
            return redirect(url_for('profile.index'))

        flash(error)

    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
