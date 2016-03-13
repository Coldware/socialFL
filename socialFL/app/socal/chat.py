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

    res['label'] = res['label'] + '/' + repr(1)


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

    res['label'] = res['label'] + '/' + repr(1)

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
    results = [{'label':'/VChat'+ '/' + str(session['idChat']), 'msg':['Enviado']}, {'label':'/VChat' + '/' + str(session['idChat']), 'msg':['No se pudo enviar mensaje']}]
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

    res['label'] = res['label'] + '/' + repr(1)


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

    res['label'] = res['label'] + '/' + repr(1)

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
    
    print(params)
    res['label'] = res['label'] + '/' + repr(1)


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
    res['data1'] = [
      {'idContacto':34, 'nombre':'ana', 'tipo':'usuario'},
      {'idContacto':23, 'nombre':'leo', 'tipo':'usuario'},
      {'idContacto':11, 'nombre':'distra', 'tipo':'usuario'},
      {'idContacto':40, 'nombre':'vane', 'tipo':'usuario'},
    ]
    res['data2'] = [
      {'idContacto':56, 'nombre':'Grupo Est. Leng.', 'tipo':'grupo'},
    ]
    res['idGrupo'] = 1
    res['fContacto_opcionesNombre'] = [
      {'key':1, 'value':'Leo'},
      {'key':2, 'value':'Lauri'},
      {'key':3, 'value':'Mara'},
    ]

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
        print(msj.emisor_id, end=" ")
        print(msj.receptor_id, end=" ")
        print(msj.contenido)
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
    
    res['data1'] = []
    for x in contacts:
        res['data1'].append({'idContacto':x.id, 'nombre':x.login, 'tipo':'usuario'})
    
    '''res['data1'] = [
      {'idContacto':34, 'nombre':'ana', 'tipo':'usuario'},
      {'idContacto':23, 'nombre':'leo', 'tipo':'usuario'},
      {'idContacto':11, 'nombre':'distra', 'tipo':'usuario'},
      {'idContacto':40, 'nombre':'vane', 'tipo':'usuario'},
      {'idContacto':56, 'nombre':'Grupo Est. Leng.', 'tipo':'grupo'},
    ]'''

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

    res['idGrupo'] = 1
    res['fMiembro_opcionesNombre'] = [
      {'key':1, 'value':'Leo'},
      {'key':2, 'value':'Lauri'},
      {'key':3, 'value':'Mara'},
    ]
    res['data3'] = [
      {'idContacto':34, 'nombre':'ana', 'tipo':'usuario'},
      {'idContacto':23, 'nombre':'leo', 'tipo':'usuario'},
      {'idContacto':11, 'nombre':'distra', 'tipo':'usuario'},
      {'idContacto':40, 'nombre':'vane', 'tipo':'usuario'},
    ]

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here

