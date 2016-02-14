from flask import Flask, session
from flask.ext.script import Manager, Server
from random import SystemRandom
from datetime import timedelta
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
import os

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
    app.permanent_session_lifetime = timedelta(minutes=45)
    session.modified = True

@app.route('/')
def root():
    return app.send_static_file('index.html')

#Application code starts here
basedir = os.path.abspath(os.path.dirname(__file__))

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

