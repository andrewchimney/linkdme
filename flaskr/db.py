import psycopg2
import click
from flask import current_app, g
import os
from dotenv import load_dotenv
import boto3
def get_db():
    load_dotenv()
    if 'db' not in g:
        try:
                        
            params = {
            'database': os.getenv('DATABASELINKDME'),
            'user': os.getenv("USERLINKDME"),
            'password': os.getenv("PASSWORDLINKDME"),
            'host': os.getenv("HOSTLINKDME"),
            'port': os.getenv("PORTLINKDME")
            }
            
            g.db = psycopg2.connect(**params)

        except Exception as e:
            print("Connection Failed", e)

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
def init_app(app):
    app.teardown_appcontext(close_db)
def get_s3():
    load_dotenv()
    s3_client = boto3.client('s3', aws_access_key_id=os.getenv('AWSACCESSKEYID'), aws_secret_access_key= os.getenv('AWSSECRETACCESSKEY'), config= boto3.session.Config(signature_version='v4', region_name = 'us-east-2',))
    return s3_client