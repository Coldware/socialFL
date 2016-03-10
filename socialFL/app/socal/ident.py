from flask import request, session, Blueprint, json

ident = Blueprint('ident', __name__)
from base import db, Usuario

@ident.route('/ident/AIdentificar', methods=['POST'])
def AIdentificar():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VPrincipal', 'msg':['Bienvenido usuario'], "actor":"duenoProducto"}, {'label':'/VLogin', 'msg':['Datos de identificación incorrectos']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    
    try: #If the information exists and is correct then u can login
        usuario = Usuario.query.filter_by(login=params['usuario']).first()
        if usuario.clave!=params['clave']:
            res = results[1]
    except:
        res = results[1]

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)




@ident.route('/ident/ARegistrar', methods=['POST'])
def ARegistrar():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VLogin', 'msg':['Felicitaciones, Ya estás registrado en la aplicación']}, {'label':'/VRegistro', 'msg':['Error al tratar de registrarse']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    usuario = Usuario(
        params['nombre'],
        params['usuario'],
        params['clave'],
        params['correo']
    ) #Create the table in the DB
    
    try: #If user is not in the DB it will register
        db.session.add(usuario)
        db.session.commit()
    except:
        res = results[1]
    db.session.close()
    
    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)




@ident.route('/ident/VLogin')
def VLogin():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@ident.route('/ident/VPrincipal')
def VPrincipal():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    
    res['idUsuario'] = 'Leo'
    
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

