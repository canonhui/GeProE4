from flask import (redirect, render_template, session, url_for, flash, request, 
                  abort, current_app)
from flask_login import logout_user, login_required, login_user, current_user

from .. import app, db
from ..forms import LoginForm
from ..ldap import Ldap
from ..models import User, Projet, Groupe, GrouPro, load_user
from config import PROJETS_PAR_PAGE, MAX_GROUPE_INS

from . import main_bp

@main_bp.route('/liste_groupes')
@login_required
def liste_groupes():

    return render_template('liste_groupes.html')

@main_bp.route('/liste_projets', methods=['GET', 'POST'])
@main_bp.route('/liste_projets/<liste>', methods=['GET', 'POST'])
#@main_bp.route('/liste_projets/<int:page>', methods=['GET', 'POST'])
@login_required
def liste_projets(liste='inscrit'):
    if liste not in ['inscrit', 'resume']:
        abort(404)
    page = request.args.get('page', 1, int)
    user_id = session.get('user_id', None)
    role = current_user.get_role()
    count_projets = Projet.query.count()
    if count_projets % PROJETS_PAR_PAGE == 0:
        page_max = int(count_projets / PROJETS_PAR_PAGE)
    else:
        page_max = int(count_projets / PROJETS_PAR_PAGE + 1)

    projets = Projet.query.paginate(page, PROJETS_PAR_PAGE, False)
    pros_attribue = Projet.query.filter(Projet.groupe_attribue!=None).all()
    groupes_attribues = []
    if pros_attribue:
        for pro_attribue in pros_attribue:
            groupes_attribues.append(pro_attribue.groupe_attribue)
    if request.method == 'GET':
        return render_template('liste_projets.html',
                            title='Liste des projets',
                            projets=projets,
                            User=User,
                            page=page,
                            role=role,
                            liste=liste,
                            groupes_attribues=groupes_attribues,
                            max_groupe_ins=MAX_GROUPE_INS,
                            page_max=page_max)

    else:
        if role == 1:
            if len(request.form) < 3:
                flash('Veuillez choisir exactement 3 projets.')
                return redirect(url_for('.liste_projets'))
            #groupe_id = User.query.filter_by(user_id=user_id).first().groupe_id
            user = load_user(user_id)
            #groupe = Groupe.query.filter_by(groupe_id=groupe_id).first()
            try:
                user.projets_inscrits = []
                for i in request.form:
                    values = request.form[i].split('-')
                    projet = Projet.query.filter_by(projet_id=int(values[0])).first()
                    if projet.groupes_inscrits.count() == MAX_GROUPE_INS:
                        flash('Projet ' + projet.projet_id + 'est déjà complet!')
                        return redirect(url_for('.liste_projets'))
                    '''
                    groupe.projets: an InstrumentedList object used to implement
                     a list-like object which is aware of insertions and deletions
                      of related objects to an object
                    '''
                    grou_pro = GrouPro(groupe_id=user.groupe_id,
                             projet_id=projet.projet_id, preference=int(values[1]))
                    projet.groupes_inscrits.append(grou_pro)
                db.session.commit()
            except Exception as e:
                flash('Errors occur when operating database: ', e)
            return redirect(url_for('.liste_projets'))
        else:
            for i in request.form:
                res = request.form[i]
                if res != '0':
                    projet = Projet.query.filter_by(projet_id=int(i)).first()
                    if projet.groupe_attribue:
                        flash('Projet ' + projet.projet_id + 'est déjà attribué!')
                        return redirect(url_for('.liste_projets'))
                    projet.groupe_attribue = int(res)
                    try:
                        db.session.commit()
                    except Exception as e:
                        flash('Errors occur when operating database: ', e)
                        return redirect(url_for('.liste_projets'))
                    else:
                        # send email
                        pass
                    finally:
                        pass
            flash('Modifacation appliquée!')
            return redirect(url_for('.liste_projets'))