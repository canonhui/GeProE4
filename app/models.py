from . import db, login_manager
from .forms import LoginForm


#from app.ldap import Ldap


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(64), index=True, unique=True)
    nom = db.Column(db.String(64), index=True, unique=False)
    prenom = db.Column(db.String(64), index=True, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)
    groupe_id = db.Column(db.Integer, db.ForeignKey('groupe.groupe_id'))
    role = db.Column(db.Integer)
    #projet = db.relationship('Projet', backref='user', lazy='dynamic')

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.user_id

    def get_name(self):
        return self.prenom+' '+self.nom

    def get_role(self):
        return self.role

    @staticmethod
    def create_user():
       # actual_user = Ldap.connect()
        if actual_user is not None:
            user = User(
                login=LoginForm().login.data,
                nom=actual_user[0],
                prenom=actual_user[1],
                email=actual_user[2],
                resp_id=actual_user[3],
                role=actual_user[4],
                soldeVacs=0,
                soldeVacsEnCours=0
            )
            return user
        return None

    @property
    def is_authenticated(self):
        return True

    @property
    def is_resp(self):
        if self.resp_id >= 1:
            return True
        else:
            return False

    def __repr__(self):
        return '<User %r>' % self.user_id


'''
A association model GrouPro, which means many-to-one relashinship with Groupe, 
and one-to-many with Projet:
'''
class GrouPro(db.Model):
    groupe_id = db.Column(db.Integer, db.ForeignKey('user.groupe_id'), primary_key=True)
    projet_id = db.Column(db.Integer, db.ForeignKey('projet.projet_id'), primary_key=True)
    preference = db.Column(db.Integer)
    groupe = db.relationship('User', backref=db.backref(
                    'projets_inscrits', lazy='dynamic', cascade='all, delete-orphan'))
    #projet = db.relationship('Projet', backref='groupes_inscrits', lazy='dynamic')


class Projet(db.Model):
    projet_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titre = db.Column(db.Text(320))
    lien = db.Column(db.String(100))
    groupe_attribue = db.Column(db.Integer)
    groupes_inscrits = db.relationship('GrouPro',
                        backref='projet', lazy='dynamic', cascade='all, delete-orphan')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Une table ridicule
class Resp(db.Model):
    key_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dept = db.Column(db.String(64))
    resp_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))


class Groupe(db.Model):
    groupe_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.relationship('User', backref='groupe', lazy='dynamic')









class Association(db.Model):
    __tablename__ = 'association'
    left_id = db.Column(db.Integer, db.ForeignKey('left.id'), primary_key=True)
    right_id = db.Column(db.Integer, db.ForeignKey('right.id'), primary_key=True)
    extra_data = db.Column(db.String(50))
    child = db.relationship("Child", back_populates="parents")
    parent = db.relationship("Parent", back_populates="children")

class Parent(db.Model):
    __tablename__ = 'left'
    id = db.Column(db.Integer, primary_key=True)
    children = db.relationship("Association", back_populates="parent", cascade='all, delete-orphan')

class Child(db.Model):
    __tablename__ = 'right'
    id = db.Column(db.Integer, primary_key=True)
    parents = db.relationship("Association", back_populates="child", cascade='all, delete-orphan')