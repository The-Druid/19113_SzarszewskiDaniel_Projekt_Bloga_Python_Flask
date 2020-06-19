from flask import Blueprint, render_template
from . import db
from flask_login import login_required, current_user
import sqlite3 as sql
main = Blueprint('main', __name__)

@main.route('/')
def index():
    dane = {'tytul':'Strona Główna', 'tresc':'Zarejestruj się, a następnie zaloguj by zobaczyć treść tylko dla zalogowanych.'
           }
    return render_template('index.html',tytul=dane['tytul'], tresc=dane['tresc'])

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

