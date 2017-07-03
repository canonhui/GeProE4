from flask import (redirect, render_template, session, url_for, flash, request, 
                  abort, current_app, jsonify)
from flask_login import logout_user, login_required, login_user, current_user
from werkzeug.utils import secure_filename

import os, time, base64

from config import basedir, UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from .. import app, db
from ..ldap import Ldap
from ..models import User, load_user

from . import admin_bp

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@admin_bp.route('/', methods=['GET', 'POST'])
@login_required
def admin():
    if request.method == 'GET':
	    return render_template('admin.html')

    file_fir = os.path.join(basedir, UPLOAD_FOLDER)
    if not os.path.exists(file_fir):
        os.makedirs(file_fir)
    if 'liste_etudiants' in request.files:
        f = request.files['liste_etudiants']
        new_filename = 'liste_etudiants'
    elif 'liste_projets' in request.files:
        f = request.files['liste_projets']
        new_filename = 'liste_projets'
    print(f)
    if f and allowed_file(f.filename):
        fname = secure_filename(f.filename)
        print('fname', fname)
        ext = fname.rsplit('.', 1)[1]
        new_filename = new_filename + '.' + ext
        #unix_time = int(time.time())
        #new_filename = str(unix_time) + '.' + ext
        f.save(os.path.join(file_fir, new_filename))
        #token = base64.b64encode(new_filename)
        #print(token)

        return jsonify({'errno':0, 'errmsg':'Upload success'})#, 'token':token})
    else:
        return jsonify({'errno':1001, 'errmsg':'Upload fails'})
    #return render_template('admin.html')

