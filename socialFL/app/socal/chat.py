from flask import request, session, Blueprint, json
from sqlalchemy import asc
import time

chat = Blueprint('chat', __name__)
from base import db, Usuario, Pagina, Mensaje, Chateador, Grupo

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
    if grupo.duenio!=usuario.id:
        grupo.delMember(usuario)
        db.session.commit()
    else:
        res['msg'] = 'Miembro es dueño del grupo'
    

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
        else:
            grupo.duenio = grupo.miembros.first().id
        
        db.session.commit()
    except:
        res = results[1]

    res['label'] = res['label'] + '/' + str(session['idUsuario'])

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



@chat.route('/chat/AgregGrupo')
def AgregGrupo():
    #GET parameter
    idUsuario = request.args['idUsuario']
    results = [{'label':'/VAdminContactos', 'msg':['Grupo agregado']}, {'label':'/VAdminContactos', 'msg':['Error al crear grupo']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    res['label'] = res['label'] + '/' + str(idUsuario)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@chat.route('/chat/AgregGrupos', methods=['POST'])
def AgregGrupos():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VAdminContactos', 'msg':['Grupo agregado']}, {'label':'/VAdminContactos', 'msg':['Error al crear grupo']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    idUsuario = session['idUsuario']

    titulo = params['nombre']
    
    grupo = Grupo(titulo, idUsuario)
    
    try: #Se prueba el exito de la creacion del foro
        db.session.add(grupo)
        db.session.commit()
    except:
        res = results[1]
    finally:
        db.session.close()

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

    res['idUsuario'] = idUsuario
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
    
    groups = Grupo.query.all()
    
    #res['data2'] = [{'idContacto':56, 'nombre':'Grupo Est. Leng.', 'tipo':'grupo'},]
    res['data2'] = []
    for x in groups:
        #print("{} {}".format(user, x.miembros.all()))
        if user in x.miembros.all():
            res['data2'].append({'idContacto':x.id, 'nombre':x.nombre, 'tipo':'grupo'})
    
    res['idGrupo'] = 1
    res['fContacto_opcionesNombre'] = []
    for x in unknown:
        res['fContacto_opcionesNombre'].append({'key':x.id, 'value':x.login})
    res['fContacto'] = {'idCOntacto':1}
    

    #Action code ends here
    return json.dumps(res)



@chat.route('/chat/VChat')
def VChat():
    #GET parameter
    idChat = int(request.args['idChat'])
    idUsuario = session['idUsuario']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    res['idChat'] = idChat
    res['idUsuario'] = idUsuario
    session['idChat'] = idChat
    
    mensajes = Mensaje.query.order_by(asc(Mensaje.timestamp)).all()
    
    if Usuario.query.get(idChat)!=None:
        res['mensajesAnt'] = [
            {'texto':msj.contenido,'usuario':msj.emisor.login, 'fecha':msj.timestamp}
            for msj in mensajes
            if ( (msj.emisor_id==idUsuario and msj.receptor_id==idChat) or
            (msj.emisor_id==idChat and msj.receptor_id==idUsuario) )
        ]
    else:
        res['mensajesAnt'] = [
            {'texto':msj.contenido,'usuario':msj.emisor.login, 'fecha':msj.timestamp}
            for msj in mensajes
            if msj.receptor_id==idChat
        ]

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
    groups = Usuario.query.get(idUsuario).grupos.all()

    res['idContacto'] = 1
    res['idUsuario'] = idUsuario
    res['data1'] = []
    for x in contacts:
        res['data1'].append({'idContacto':x.id, 'nombre':x.login, 'tipo':'usuario'})
    for y in groups:
        res['data1'].append({'idContacto':y.id, 'nombre':y.nombre, 'tipo':'grupo'})

    #Action code ends here
    return json.dumps(res)



@chat.route('/chat/VGrupo')
def VGrupo():
    #GET parameter
    idGrupo = request.args['idGrupo']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    if "idUsuario" in session:
        res["idUsuario"]= session['idUsuario']
    #Action code goes here, res should be a JSON structure

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

    res['fMiembro'] = {'idUsuario':res["idUsuario"], 'idGrupo':idGrupo}

    session['idGrupo'] = res['idGrupo']
    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here

