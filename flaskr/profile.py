from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flaskr.db import get_db
bp = Blueprint('profile', __name__)
@bp.route('/profile', methods =('GET','POST','PUT','DELETE', 'PATCH'))
def index():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    print(user_id)
    db=get_db()
    cur=db.cursor()
    sql = f"SELECT * FROM profile WHERE user_id = '{user_id}'"
    cur.execute(sql)
    user = cur.fetchone()
    if request.method=='POST':
        a_link = request.json['add_link']
        user[3].append(a_link)
        sql=f"UPDATE profile set links=ARRAY{user[3]} WHERE user_id ='{user_id}'"
        cur.execute(sql)
        db.commit()
    if request.method=='PATCH':
        o_link=request.json['o_link']
        n_link=request.json['n_link']
        if o_link is not n_link:
            for i in range(0,len(user[3])):
                if user[3][i] == o_link:
                    user[3][i] = n_link
            sql=f"UPDATE profile set links=ARRAY{user[3]} WHERE user_id ='{user_id}'"
            cur.execute(sql)
            db.commit()
    if request.method =='DELETE':
        del_link=request.json['del_link']
        user[3].remove(del_link)
        print(user[3])
        sql=f"UPDATE profile set links=ARRAY{user[3]}::text[] WHERE user_id ='{user_id}'"
        cur.execute(sql)
        db.commit()
            
    if request.method=='GET':
        pass
        
        
    return render_template('profile.html',user=user)

@bp.route('/profile/logout', methods =('GET','POST'))
def logout():
    session.pop('user_id')
    return redirect(url_for('auth.login'))