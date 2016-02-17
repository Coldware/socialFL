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

class Usuario(db.Model):
    idUsuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(15))
    login = db.Column(db.String(15), index=True, unique=True)
    clave = db.Column(db.String(15))
    correo = db.Column(db.String(20))
    
    def __init__(self, nombre, login, clave, correo):
        self.nombre = nombre
        self.login = login
        self.clave = clave
        self.correo = correo
    
    def __repr__(self):
        return '<USUARIO --> id:{} login:{}>'.format(self.idUsuario, self.login)

class Pagina(db.Model):
    idPagina = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(20), index=True, unique=True)
    contenido = db.Column(db.Text)
    idUsuario = db.Column(db.Integer, db.ForeignKey('usuario.idUsuario'))
    usuario = db.relationship('Usuario', backref=db.backref('pagina', lazy='dynamic'))

    
    def __init__(self, titulo, contenido, usuario):
        self.titulo = titulo
        self.contenido = contenido
        self.usuario = usuario
    
    def __repr__(self):
        return '<PAGINA --> id:{} titulo:{} usuario:{}>'.format(self.idPagina, self.titulo, self.usuario.login)

#Application code ends here

from app.socal.ident import ident
app.register_blueprint(ident)
from app.socal.paginas import paginas
app.register_blueprint(paginas)


if __name__ == '__main__':
    app.config.update(
      SECRET_KEY = repr(SystemRandom().random())
    )
    manager.run()