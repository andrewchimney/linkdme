from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import psycopg2
from flaskr.db import get_db
bp = Blueprint('profile', __name__)
@bp.route('/profile', methods =('GET','POST'))
def index():
    if request.method=='GET':
        db=get_db()
        cur=db.cursor()
        print(g.user)
        sql = f"SELECT * FROM profile WHERE user_id = '{'sadfas'}'"
        print(sql)
        cur.execute(sql)
        user = cur.fetchone()
        
    return render_template('profile.html')