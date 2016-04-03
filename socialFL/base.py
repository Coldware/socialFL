from flask import Flask, session
from flask.ext.script import Manager, Server
from random import SystemRandom
from datetime import timedelta
from datetime import datetime
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

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)
    session.modified = True

@app.route('/')
def root():
    return app.send_static_file('index.html')

#Application code starts here
basedir = os.path.abspath(os.path.dirname(__file__))

#CONFIGURE DATA BASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'apl.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)




followers = db.Table('followers',
    db.Column("follower_id", db.Integer, db.ForeignKey("usuario.id")),
    db.Column("followed_id", db.Integer, db.ForeignKey("usuario.id"))
)

miembros = db.Table('miembros',
    db.Column("member_id", db.Integer, db.ForeignKey("usuario.id")),
    db.Column("group_id", db.Integer, db.ForeignKey("grupo.id"))
)


class Chateador(db.Model):
    __tablename__ = 'chateador'
    __mapper_args__ = {'polymorphic_identity': 'chateador'}
    id = db.Column(db.Integer, primary_key=True)
    receptor = db.relationship("Mensaje", backref="receptor", lazy='dynamic', foreign_keys='Mensaje.receptor_id')


class Usuario(Chateador):
    __tablename__ = 'usuario'
    __mapper_args__ = {'polymorphic_identity': 'usuario'}
    id = db.Column(db.Integer, db.ForeignKey('chateador.id'), primary_key=True)
    nombre = db.Column(db.String(15))
    login = db.Column(db.String(15), index=True, unique=True)
    clave = db.Column(db.String(15))
    correo = db.Column(db.String(20), unique=True)
    pagina = db.relationship('Pagina', backref="usuario", lazy='dynamic')
    grupo_id = db.Column(db.Integer, db.ForeignKey('grupo.id'))
    contacto = db.relationship("Usuario",
                    secondary=followers,
                    primaryjoin=(followers.c.follower_id == id),
                    secondaryjoin=(followers.c.followed_id == id),
                    backref=db.backref("followers", lazy='dynamic'),
                    lazy='dynamic'
    )
    emisor = db.relationship("Mensaje", backref="emisor", lazy='dynamic', foreign_keys='Mensaje.emisor_id')

    def __init__(self, nombre, login, clave, correo):
        self.nombre = nombre
        self.login = login
        self.clave = clave
        self.correo = correo
    
    def __repr__(self):
        return '<USUARIO {}>'.format(self.login)
    
    def addContact(self, usuario):
        if not self.esContacto(usuario):
            self.contacto.append(usuario)
            return self
    
    def delContact(self, usuario):
        if self.esContacto(usuario):
            self.contacto.remove(usuario)
            return self
    
    def esContacto(self, usuario):
        return self.contacto.filter(followers.c.followed_id == usuario.id).count() > 0


class Grupo(Chateador):
    __tablename__ = 'grupo'
    __mapper_args__ = {'polymorphic_identity': 'grupo'}
    id = db.Column(db.Integer, db.ForeignKey('chateador.id'), primary_key=True)
    nombre = db.Column(db.String(20))
    duenio = db.Column(db.Integer)
    miembros = db.relationship("Usuario",
                    secondary=miembros,
                    #primaryjoin=(miembros.c.member_id == id),
                    #secondaryjoin=(miembros.c.group_id == id),
                    backref=db.backref("grupos", lazy='dynamic'), 
                    lazy='dynamic'
                    )
    
    def __init__(self, nombre, duenio):
        self.nombre = nombre
        self.duenio = duenio
        self.miembros.append(Usuario.query.get(duenio))
    
    def __repr__(self):
        return '<GRUPO {}>'.format(self.nombre)
        
    def addMember(self, miembro):
        if not self.esMiembro(miembro):
            self.miembros.append(miembro)
            return self
    
    def delMember(self, miembro):
        if self.esMiembro(miembro):
            self.miembros.remove(miembro)
            return self
    
    def esMiembro(self, miembro):
        return self.miembros.filter(miembros.c.member_id == miembro.id).count() > 0


class Mensaje(db.Model):
    __tablename__ = 'mensaje'
    id = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    emisor_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    receptor_id = db.Column(db.Integer, db.ForeignKey('chateador.id'))
    
    def __init__(self, contenido, timestamp=None):
        self.contenido = contenido
        if timestamp is None:
            self.timestamp = datetime.utcnow()
        else:
            self.timestamp = timestamp
    
    def __repr__(self):
        return '<MENSAJE --> {}>'.format(self.contenido)


class Pagina(db.Model):
    __tablename__ = 'pagina'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(20), index=True, unique=True)
    contenido = db.Column(db.Text)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

    def __init__(self, titulo, contenido, usuario):
        self.titulo = titulo
        self.contenido = contenido
        self.usuario = usuario
    
    def __repr__(self):
        return '<PAGINA --> titulo:{} usuario:{}>'.format(self.titulo, self.usuario.login)


class Comentable(db.Model):
    __tablename__ = 'comentable'
    __mapper_args__ = {'polymorphic_identity': 'comentable'}
    id = db.Column(db.Integer, primary_key=True)
    publicacion = db.relationship('Publicacion', backref=db.backref("comentable", enable_typechecks=False), lazy='dynamic')


class Foro(Comentable):
    __tablename__ = 'foro'
    id = db.Column(db.Integer, db.ForeignKey('comentable.id'), primary_key=True)
    titulo = db.Column(db.String(20), index=True, unique=True)
    timestamp = db.Column(db.DateTime)
    autor = db.Column(db.Integer)
    
    def __init__(self, titulo, autor, timestamp=None):
        self.titulo = titulo
        self.autor = autor
        if timestamp is None:
            self.timestamp = datetime.utcnow()
        else:
            self.timestamp = timestamp
    
    def __repr__(self):
        return '<FORO --> titulo:{} autor:{}>'.format(self.titulo, 
        Usuario.query.get(self.autor).login)


class PaginaSitio(Comentable):
    __tablename__ = 'paginasitio'
    id = db.Column(db.Integer, db.ForeignKey('comentable.id'), primary_key=True)
    url = db.Column(db.String(30), index=True, unique=True)
    titulo = db.Column(db.String(20), index=True, unique=True)
    contenido = db.Column(db.Text)
    
    def __init__(self, titulo, contenido, url=None):
        self.titulo = titulo
        self.contenido = contenido
        self.url = url
        
    
    def __repr__(self):
        return '<PAGINA SITIO --> titulo:{}>'.format(self.titulo)


class Publicacion(db.Model):
    __tablename__ = 'publicacion'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(20), index=True)
    contenido = db.Column(db.Text)
    autor = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)
    anterior_id = db.Column(db.Integer, db.ForeignKey('publicacion.id'), index=True)
    hijos = db.relationship('Publicacion', backref=db.backref('anterior', remote_side='Publicacion.id'))
    comentable_id = db.Column(db.Integer, db.ForeignKey('comentable.id'))
    
    def __init__(self, titulo, contenido, autor, anterior=None, timestamp=None):
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        if anterior is not None:
            self.anterior = anterior
        if timestamp is None:
            self.timestamp = datetime.utcnow()
        else:
            self.timestamp = timestamp
    
    def __repr__(self):
        return '<PUBLICACION --> titulo:{} autor:{}>'.format(self.titulo, 
        Usuario.query.get(self.autor).login)
    
    def imprimirhijos(self, array, nivel):
        for hijo in self.hijos:
            espacios = '&nbsp'*nivel
            titulo = espacios + hijo.titulo
            array.append({'idMensaje':hijo.id, 'titulo':titulo, 'contenido': hijo.contenido})
            hijo.imprimirhijos(array, nivel+4)
        return array

#Application code ends here

from app.socal.ident import ident
app.register_blueprint(ident)
from app.socal.paginas import paginas
app.register_blueprint(paginas)
from app.socal.chat import chat
app.register_blueprint(chat)
from app.socal.foro import foro
app.register_blueprint(foro)

if __name__ == '__main__':
    app.config.update(
      SECRET_KEY = repr(SystemRandom().random())
    )
    manager.run()
