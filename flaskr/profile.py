from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flaskr.db import get_db, get_s3
import os
import boto3
import logging
boto3.set_stream_logger('', logging.CRITICAL)
bp = Blueprint('profile', __name__)
@bp.route('/profile', methods =('GET','POST','PUT','DELETE', 'PATCH'))
def index():
    print(os.getenv("WEBSITELINKDME"))
    s3_client = get_s3()

    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
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
        sql=f"UPDATE profile set links=ARRAY{user[3]}::text[] WHERE user_id ='{user_id}'"
        cur.execute(sql)
        db.commit()
        
    if request.method=="PUT":
        print("put request started")
        if (request.content_type =="application/json"):
            bio=request.json['bio']
            if (bio==""):
                sql=f"UPDATE profile set bio=NULL WHERE user_id='{user_id}'"
            else :
                sql=f"UPDATE profile set bio='{bio}' WHERE user_id='{user_id}'"
            cur.execute(sql)
            db.commit()
        else:
            name=f'{user_id}.png'
            print(request.files['file'])
            response = s3_client.put_object(Body=request.files["file"],Bucket="linkdmebucket", Key=name)
            print(response)
            link = f'https://linkdmebucket.s3.us-east-2.amazonaws.com/{user_id}.png'
            sql = f"UPDATE profile set image='{link}' WHERE user_id='{user_id}'"
            cur.execute(sql)
            db.commit()
        
            
    if request.method=='GET':
        pass
        
        
    return render_template('profile.html',user=user, web=os.getenv("WEBSITELINKDME"), s3_client=s3_client)

@bp.route('/profile/logout', methods =('GET','POST'))
def logout():
    session.pop('user_id')
    return redirect(url_for('auth.login'))