from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from playlistSync.auth import login_required
from playlistSync.db import get_db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    db = get_db()
    #set up the main page