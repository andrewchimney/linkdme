import psycopg2
import click
from flask import current_app, g
import sys

def get_db():
    if 'db' not in g:
        try:
                        
            params = {
            'database': 'postgres',
            'user': 'postgres',
            'password': 'skippy123',
            'host': '127.0.0.1',
            'port': 5432
            }
            print("connecting to database")
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