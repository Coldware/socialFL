from flask import request, session, Blueprint, json

ident = Blueprint('ident', __name__)
from base import db, Usuario#, Pagina


@ident.route('/ident/AIdentificar', methods=['POST'])
def AIdentificar():
    #POST/PUT parameters
    params = request.get_json()
    results = [
        {'label':'/VPrincipal', 'msg':['Bienvenido usuario'], 
        "actor":params['usuario']}, 
        {'label':'/VLogin', 'msg':['Datos de identificación incorrectos']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    
    login = params['usuario']
    clave = params['clave']

    #Verification of existing account
    flag = VerificarCuentaExiste(login)

    #Registration
    if flag:#If the login exists then u can login successfully
        usuario = Usuario.query.filter_by(login=login).first()
        if usuario.clave!=clave:
            res = results[1]
            print("Clave incorrecta.")
    else:#If the login doesn't exist then u can't login to the app
        res = results[1]

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
            print("session: "+str(session))
    return json.dumps(res)



@ident.route('/ident/ARegistrar', methods=['POST'])
def ARegistrar():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VLogin', 'msg':['Felicitaciones, Ya estás registrado en la aplicación']}, 
    {'label':'/VRegistro', 'msg':['Error al tratar de registrarse']},]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    nombre = params['nombre']
    login = params['usuario']
    clave = params['clave']
    correo = params['correo']
    
    #Verification of Non existing account
    flag = VerificarCuentaExiste(login)
    
    #Registration
    if flag:#If login is already in use it wont let u register
        res = results[1]
        print("Ya hay un usuario registrado con ese login.")
    else:#If login is free to use u will register successfully
        usuario = Usuario(nombre,login,clave,correo)#Create the table in the DB
        db.session.add(usuario)#Add the table without the ID
        db.session.commit()#Confirm the adding of the table in the DB
        print("El usuario fue registrado exitosamente.")
    
    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

def VerificarCuentaExiste(login):
    #To show every user in the data base
    usuarios = Usuario.query.all()
    for usr in usuarios:
        print(usr)
    
    print("Login: " + login)#To show who's trying to log in or register
    
    usuario = Usuario.query.filter_by(login=login).first()
    print(usuario)#To show if the user exists or not
    if usuario==None:
        return False
    return True




@ident.route('/ident/VLogin')
def VLogin():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
        session.pop("actor")
    print(session)
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@ident.route('/ident/VPrincipal')
def VPrincipal():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
        usuario = Usuario.query.filter_by(login=res['actor']).first()
    #Action code goes here, res should be a JSON structure

    res['idUsuario'] = usuario.login

    #Action code ends here
    return json.dumps(res)



@ident.route('/ident/VRegistro')
def VRegistro():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here

