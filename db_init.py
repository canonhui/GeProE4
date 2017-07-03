#!/usr/bin/env python3
from app import db
from app.models import User, Projet, Resp, Groupe
import csv
import re

def name_firstname_login(x):

    s = x.split()
    name = s[0]
    firstname = ''
    ls = len(s)
    k = 0
    while k < ls:
        k = k + 1
        if s[k].isupper():
            name = name + ' ' + s[k]
        else:
            break
    firstname = ' '.join(s[k::])
    # login = name.split('-')[0].replace(' ', '')[:7] + firstname[0]
    login = name.replace('-', '').replace(' ', '')[:7] + firstname[0]
    return (name, firstname, login.lower())


def resp_to_db():
    dept_dic = {}
    with open('csv/resp_depts.csv', 'r', encoding='utf-8') as csvfile:
        user_id=0
        reader = csv.DictReader(csvfile, delimiter=',')     
        for row in reader:
            user_id+=1
            name = row['Nom']
            firstname = row['Prenom']
            login = row['Login']
            email = row['email']
            dept =  row['Dept'].split('Dept. ')[1]
            
            role=2 # => responsable
            soldeVacs=0
            soldeVacsEnCours=0
            u = User.query.filter_by(login=login).first() # does user already exist ? 
            if(u is None):
                u = User(login=login, nom=name, prenom=firstname, email=email, resp_id=user_id, soldeVacs=soldeVacs, soldeVacsEnCours=soldeVacsEnCours, role=role)            
                db.session.add(u)
            else:
                u.role = 2    
                u.email = email

            dept_dic[dept]  = user_id
            d = Resp(dept=dept, resp_id=dept_dic[dept])
            db.session.add(d)    
    db.session.commit()
    return dept_dic


def get_department():
    dept_dic = {}
    with open('csv/resp_depts.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')     
        for row in reader:
            #name, firstname, login = name_firstname_login(row['NOM Prenom'])
            name = row['Nom']
            firstname = row['Prenom']
            login = row['Login']
            email = row['email']
            dept =  row['Dept'].split('Dept. ')[1]
            dept_dic[dept]  = User.query.filter_by(login=login, role=2).first().user_id
            d = Resp(dept=dept, resp_id=dept_dic[dept])
            db.session.add(d)
    db.session.commit()            
    return dept_dic


def admins_to_db():
    user_id = 999
    with open('upload/admins.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')     
        for row in reader:
            user_id += 1
            #name, firstname, login = name_firstname_login(row['NOM Prenom'])
            nom = row['Nom']
            prenom = row['Prenom']
            login = row['Login']
            email = row['email']
            role = 77 # => admin
            #resp_id = dept_dic.get(dept, user_id)
            
            u = User.query.filter_by(login=login).first() # does user already exist ? 
            if(u is None):
               u = User(login=login, nom=nom, prenom=prenom, email=email, user_id=user_id, role=role)
               db.session.add(u)
            else:
               u.role = 77
               #u.resp_id = resp_id
               u.email = email
            d = Resp(dept='dir', resp_id=resp_id)
            db.session.add(d)

    db.session.commit()


def user_to_db():
    with open('upload/liste_etudiants.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        # next(reader, None)  # skip the headers
        for row in reader:
            #name, firstname, login = name_firstname_login(row['NOM Prenom'])
            nom = row['Nom']
            prenom = row['Prenom']
            login = row['Login']
            groupe_id = row['Groupe']
            email = login + "@esiee.fr"
            role = row['Role']
            #dept = row['Dept'].split('EP : Dept. ')[1]
            #dept = row['Dept'].split('Dept. ')[1]
            #resp_id = dept_dic[dept]

            u = User.query.filter_by(login=login).first() # does user already exist ? 
            if(u is None):
                u = User(login=login, nom=nom, prenom=prenom, groupe_id=groupe_id, email=email, role=role)            
                db.session.add(u)

        nb_groupes = db.session.query(db.func.max(User.groupe_id)).scalar()
        for i in range(1, nb_groupes + 1):
            db.session.add(Groupe())
    db.session.commit()

def projets_to_db():
    with open('upload/liste_projets.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            titre = row['Titre']
            lien = row['Lien']

            p = Projet(titre=titre, lien=lien)
            db.session.add(p)
    db.session.commit()

def groupes_to_db():
    pass#nb_groupes = User.query.filter_by()

def user_to_db_old():
    with open('csv/liste_enseignants_2016-17.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None)  # skip the headers
        for row in reader:
            name, firstname, login = name_firstname_login(row[0])
            email = login + "@esiee.fr"
            role=1
            dept = row[1].split('EP : Dept. ')[1]
            resp_id = dept_dic[dept]
            soldeVacs=int(row[2]) if row[2] != '' else 0
            soldeVacsEnCours=int(row[3]) if row[3] != '' else 0
            
            u = User.query.filter_by(login=login).first() # does user already exist ? 
            if(u is None):
                u = User(login=login, nom=name, prenom=firstname, email=email, resp_id=resp_id, soldeVacs=soldeVacs, soldeVacsEnCours=soldeVacsEnCours, role=role)            
                db.session.add(u)
            else:
                u.soldeVacsEnCours = soldeVacsEnCours
                u.soldeVacs = soldeVacs

    
    db.session.commit()

#dept_dic = resp_to_db()
#dept_dic = get_department()
user_to_db()
#admins_to_db()
projets_to_db()