from flask import request, session, Blueprint, json
from sqlalchemy import asc

chat = Blueprint('chat', __name__)
from base import db, Usuario, Pagina, Mensaje, Chateador

@chat.route('/chat/AElimContacto')
def AElimContacto():
    #GET parameter
    id = request.args['id']
    results = [{'label':'/VAdminContactos', 'msg':['Contacto eliminado']}, {'label':'/VAdminContactos', 'msg':['No se pudo eliminar contacto']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    idUsuario = session['idUsuario']
    user = Usuario.query.get(idUsuario)
    #print("Usuario 1: {}".format(user))
    user2 = Usuario.query.get(id)
    #print("Usuario 2: {}".format(user2))
    
    try:
        user.delContact(user2)
        user2.delContact(user)
        db.session.commit()
    except:
        res = results[1]
    
    res['label'] = res['label'] + '/' + str(idUsuario)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@chat.route('/chat/AElimMiembro')
def AElimMiembro():
    #GET parameter
    id = request.args['id']
    results = [{'label':'/VGrupo', 'msg':['Miembro eliminado']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    res['label'] = res['label'] + '/' + session['idGrupo']

    grupo = Grupo.query.get(session['idGrupo'])
    usuario = Usuario.query.get(id)
    grupo.delMember(usuario)
    db.session.commit()

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@chat.route('/chat/AEscribir', methods=['POST'])
def AEscribir():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VChat', 'msg':['Enviado']}, {'label':'/VChat', 'msg':['No se pudo enviar mensaje']}]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    res['idUsuario']=session['idUsuario']
    
    emisor = Usuario.query.get(res['idUsuario'])
    receptor = Chateador.query.get(session['idChat'])
    mensaje = Mensaje(params['texto'])
    
    db.session.add(mensaje)
    
    emisor.emisor.append(mensaje)
    receptor.receptor.append(mensaje)
    
    db.session.commit()
    
    db.session.close()
    
    try: #CON ESTO SE PUEDE VERIFICAR SI EL MENSAJE FUE GUARDADO CORRECTAMENTE
        test = Mensaje.query.filter_by(contenido=params['texto']).first()
        x = test.contenido
    except:
        res = results[1]
    
    res['label'] = res['label'] + '/' + str(session['idChat'])
    
    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@chat.route('/chat/ASalirGrupo')
def ASalirGrupo():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VAdminContactos', 'msg':['Ya no estás en ese grupo']}, {'label':'/VGrupo', 'msg':['Sigues en el grupo']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    grupo = Grupo.query.get(session['idGrupo'])
    
    try:
        usuario = Usuario.query.get(session['idUsuario'])
        grupo.delMember(usuario)
        
        if(grupo.miembros.count()==0):
            db.session.delete(grupo)
        
        db.session.commit()
    except:
        res = results[1]

    res['label'] = res['label'] + '/' + session['idUsuario']

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@chat.route('/chat/AgregContacto', methods=['POST'])
def AgregContacto():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VAdminContactos', 'msg':['Contacto agregado']}, {'label':'/VAdminContactos', 'msg':['No se pudo agregar contacto']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    
    idUsuario = session['idUsuario']

    user = Usuario.query.get(idUsuario)
    #print("Usuario 1: {}".format(user))
    user2 = Usuario.query.get(params['nombre'])
    #print("Usuario 2: {}".format(user2))
    
    if user.esContacto(user2)==0:
        user.addContact(user2)
        user2.addContact(user)
        db.session.commit()
    else:
        res = results[1]
    
    res['label'] = res['label'] + '/' + str(idUsuario)
    
    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@chat.route('/chat/AgregMiembro', methods=['POST'])
def AgregMiembro():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VGrupo', 'msg':['Nuevo miembro agregado']}, {'label':'/VGrupo', 'msg':['No se pudo agregar al nuevo miembro']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    
    res['label'] = res['label'] + '/' + session['idGrupo']

    grupo = Grupo.query.get(session['idGrupo'])
    usuario = Usuario.query.get(params['nombre'])
    grupo.addMember(usuario)
    db.session.commit()

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@chat.route('/chat/VAdminContactos')
def VAdminContactos():
    #GET parameter
    idUsuario = request.args['idUsuario']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    
    res['idContacto'] = 1
    
    user = Usuario.query.get(idUsuario)
    
    unknown = Usuario.query.filter(Usuario.nombre!=user.nombre).all()
    contacts = Usuario.query.get(idUsuario).contacto.all()
    
    for x in contacts:
        if x in unknown:
            unknown.remove(x)
    
    #print("Estos son mis contactos: {}".format(contacts))
    #print("Estos son los que desconozco: {}".format(unknown))

    res['data1'] = []
    for x in contacts:
        res['data1'].append({'idContacto':x.id, 'nombre':x.login, 'tipo':'usuario'})
    
    res['data2'] = [
      {'idContacto':56, 'nombre':'Grupo Est. Leng.', 'tipo':'grupo'},
    ]
    
    res['idGrupo'] = 1
    res['fContacto_opcionesNombre'] = []
    for x in unknown:
        res['fContacto_opcionesNombre'].append({'key':x.id, 'value':x.login})

    #Action code ends here
    return json.dumps(res)



@chat.route('/chat/VChat')
def VChat():
    #GET parameter
    idChat = request.args['idChat']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    res['idChat'] = 1
    res['idUsuario'] = session['idUsuario']
    session['idChat'] = int(idChat)
    
    mensajes = Mensaje.query.order_by(asc(Mensaje.timestamp)).all()
    #print(mensajes)
    
    res['mensajesAnt'] = []
    for msj in mensajes:
        #print("{} {} {}".format(msj.emisor_id, msj.receptor_id, msj.contenido))
        if ((msj.emisor_id==session['idUsuario'] and msj.receptor_id==int(idChat)) or
        (msj.emisor_id==int(idChat) and msj.receptor_id==session['idUsuario'])):
            res['mensajesAnt'].append({'texto':msj.contenido, 'usuario':msj.emisor.login, 'fecha':msj.timestamp})

    #Action code ends here
    return json.dumps(res)



@chat.route('/chat/VContactos')
def VContactos():
    #GET parameter
    idUsuario = request.args['idUsuario']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    usuario = Usuario.query.get(idUsuario)
    contacts = Usuario.query.get(idUsuario).contacto.all()
    #print(contacts)
    
    res['idContacto'] = 1
    res['idUsuario'] = idUsuario
    res['data1'] = []
    for x in contacts:
        res['data1'].append({'idContacto':x.id, 'nombre':x.login, 'tipo':'usuario'})

    #Action code ends here
    return json.dumps(res)



@chat.route('/chat/VGrupo')
def VGrupo():
    #GET parameter
    idGrupo = request.args['idGrupo']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    
    res["idUsuario"]= session['idUsuario']
    res['idGrupo'] = idGrupo

    grupo = Grupo.query.get(idGrupo)

    res['fMiembro_opcionesNombre'] = []
    res['data3'] = [] 
    
    usuario = Usuario.query.get(session['idUsuario'])


    for contacto in usuario.contacto:
        if(contacto not in grupo.miembros):
            res['fMiembro_opcionesNombre'].append({'key':contacto.id, 'value':contacto.nombre})
 
    for contacto in grupo.miembros:
        if(contacto.id != usuario.id):
            res['data3'].append({'idContacto':contacto.id, 'nombre':contacto.nombre, 'tipo':'usuario'})


    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here

