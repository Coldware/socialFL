from flask import Flask, session
from flask.ext.script import Manager, Server, prompt_bool
from random import SystemRandom
from datetime import timedelta
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
import os

#CONFIGURE MANAGER
app = Flask(__name__, static_url_path='')
manager = Manager(app)
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0', port = 8080)
)

@manager.command
def initdb():
    db.create_all()
    print("La base de datos ha sido inicializada.")
    
@manager.command
def dropdb():
    if prompt_bool("Estas seguro que quieres borrar toda la data?"):
        db.drop_all()
        print("Base de datos borrada.")

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=45)
    session.modified = True

@app.route('/')
def root():
    return app.send_static_file('index.html')

#Application code starts here
basedir = os.path.abspath(os.path.dirname(__file__))

#CONFIGURE DATA BASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'apl.db')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)




user_to_user = db.Table('user_to_user',
    db.Column("follower_id", db.Integer, db.ForeignKey("usuario.id")),
    db.Column("followed_id", db.Integer, db.ForeignKey("usuario.id"))
)

member_to_group = db.Table('member_to_group',
    db.Column('member_id', db.Integer, db.ForeignKey('usuario.id')),
    db.Column('group_id', db.Integer, db.ForeignKey('grupo.id'))
)

class Grupo(db.Model):
    __tablename__ = 'grupo'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    miembros = db.relationship("Usuario",
                    secondary=member_to_group,
                    primaryjoin=id==member_to_group.c.member_id,
                    secondaryjoin=id==member_to_group.c.group_id,
                    backref=db.backref("grupo", lazy='dynamic'),
                    lazy='dynamic'
                    )
    '''duenio = db.relationship("Usuario", uselist=False,
    backref=db.backref("duenioGrupo", lazy='dynamic'), lazy='dynamic'
    )'''
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __repr__(self):
        return '<GRUPO --> id:{} nombre:{}>'.format(self.id, self.nombre)
        
    def addMember(self, miembro):
        if not self.esMiembro(miembro):
            self.miembros.append(miembro)
            return self
    
    def delMember(self, miembro):
        if self.esMiembro(miembro):
            self.miembros.remove(miembro)
            return self
    
    def esMiembro(self, miembro):
        return self.miembros.filter(member_to_group.c.member_id == miembro.id).count() > 0


class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(15))
    login = db.Column(db.String(15), index=True, unique=True)
    clave = db.Column(db.String(15))
    correo = db.Column(db.String(20))
    pagina = db.relationship('Pagina', backref='usuario', lazy='dynamic')
    grupo_id = db.Column(db.Integer, db.ForeignKey('grupo.id'))
    #duenioGrupo_id = db.Column(db.Integer, db.ForeignKey('grupo.id'))
    contacto = db.relationship("Usuario",
                    secondary=user_to_user,
                    primaryjoin=id==user_to_user.c.follower_id,
                    secondaryjoin=id==user_to_user.c.followed_id,
                    backref=db.backref("followed_by", lazy='dynamic'),
                    lazy='dynamic'
    )

    def __init__(self, nombre, login, clave, correo):
        self.nombre = nombre
        self.login = login
        self.clave = clave
        self.correo = correo
    
    def __repr__(self):
        return '<USUARIO --> id:{} login:{}>'.format(self.id, self.login)
    
    def addPage(self, pagina):
        self.pagina.append(pagina)
    
    def delPage(self, pagina):
        self.pagina.remove(pagina)
    
    def addContact(self, usuario):
        if not self.esContacto(usuario):
            self.contacto.append(usuario)
            return self
    
    def delContact(self, usuario):
        if self.esContacto(usuario):
            self.contacto.remove(usuario)
            return self
    
    def esContacto(self, usuario):
        return self.contacto.filter(user_to_user.c.followed_id == usuario.id).count() > 0

class Pagina(db.Model):
    __tablename__ = 'pagina'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(20), index=True, unique=True)
    contenido = db.Column(db.Text)
    pagina_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

    def __init__(self, titulo, contenido, usuario):
        self.titulo = titulo
        self.contenido = contenido
        self.usuario = usuario
    
    def __repr__(self):
        return '<PAGINA --> id:{} titulo:{} usuario:{}>'.format(self.id, self.titulo, self.usuario.login)

class Mensaje(db.Model):
    __tablename__ = 'mensaje'
    id = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.Text)
    fecha = db.Column(db.DateTime)
    
    def __init__(self, contenido, fecha):
        self.contenido = contenido
        self.fecha = fecha
    
    def __repr__(self):
        return '<MENSAJE --> id:{} contenido:{} fecha:{}>'.format(self.id, self.contenido, self.fecha)




#Application code ends here

from app.socal.ident import ident
app.register_blueprint(ident)
from app.socal.paginas import paginas
app.register_blueprint(paginas)
from app.socal.chat import chat
app.register_blueprint(chat)

if __name__ == '__main__':
    app.config.update(
      SECRET_KEY = repr(SystemRandom().random())
    )
    manager.run()
