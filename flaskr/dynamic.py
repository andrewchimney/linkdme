from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import psycopg2
from flaskr.db import get_db
import os

bp = Blueprint('<dynamic>', __name__, url_prefix='/')

@bp.route('/<dynamic>', methods=('GET', 'POST'))
def dynamic(dynamic):
    ip = os.getenv("IP")
    if request.method=='GET':
        db=get_db()
        cur = db.cursor()
        sql = f"SELECT * FROM profile WHERE user_id = '{dynamic}'"
        cur.execute(sql)
        user = cur.fetchone()
    
    
    return render_template("dynamic.html", user=user, ip=ip)