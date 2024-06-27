from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import os
bp = Blueprint('/', __name__)
ip = os.getenv("IP")
@bp.route('/', methods =('GET','POST'))
def index():
     return render_template('home.html', web=os.getenv("WEBSITELINKDME"))