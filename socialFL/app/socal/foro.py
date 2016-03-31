from flask import request, session, Blueprint, json
from sqlalchemy import asc

foro = Blueprint('foro', __name__)
from base import db, Foro


@foro.route('/foro/AComentar', methods=['POST'])
def AComentar():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VPrincipal', 'msg':['Comentario realizado']}, {'label':'/VComentariosPagina', 'msg':['Error al realizar comentario']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    #En caso de error
    #res['label'] = res['label'] + '/' + repr(1)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@foro.route('/foro/AElimForo')
def AElimForo():
    #GET parameter
    idForo = request.args['idForo']
    results = [{'label':'/VForos', 'msg':['Foro eliminado']}, {'label':'/VForo', 'msg':['No se pudo eliminar el foro']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    res['label'] =res['label'] + '/' + str(session['idUsuario'])
    foro = Foro.query.get(idForo)
    
    try:
        if session['idUsuario']==foro.autor:
            for hilo in foro.hilo:
                print(hilo)
                db.session.delete(hilo)
            db.session.delete(foro)
            db.session.commit()
        else:
            raise ValueError("No eres el dueño del foro")
    except ValueError as ve:
        res = results[1]
        res['label'] =res['label'] + '/' + idForo
    except:
        res = results[1]
        res['label'] =res['label'] + '/' + idForo
    finally:
        db.session.close()
    
    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@foro.route('/foro/APublicar', methods=['POST'])
def APublicar():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VForo', 'msg':['Publicación realizada']}, {'label':'/VPublicacion', 'msg':['Error al realizar publicación']}, ]
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



@foro.route('/foro/AgregForo', methods=['POST'])
def AgregForo():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VForos', 'msg':['Foro creado']}, {'label':'/VForos', 'msg':['No se pudo crear el foro']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    
    idUsuario = session['idUsuario']
    res['idUsuario'] = idUsuario
    
    titulo = params['titulo']
    
    foro = Foro(titulo, idUsuario)
    db.session.add(foro)
    db.session.commit()
    
    try: #Se prueba el exito de la creacion del foro
        test = Foro.query.filter_by(titulo=titulo).first()
        x = test.titulo #Si Test es None esto dara error e ira al except
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



@foro.route('/foro/VComentariosPagina')
def VComentariosPagina():
    #GET parameter
    idPaginaSitio = request.args['idPaginaSitio']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    res['idPagina'] = 1

    #Action code ends here
    return json.dumps(res)



@foro.route('/foro/VForo')
def VForo():
    #GET parameter
    idForo = request.args['idForo']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    res['idForo'] = idForo
    res['idUsuario'] = session['idUsuario']
    res['idMensaje'] = 0 #Nueva publicación
    
    foro = Foro.query.get(idForo)
    hilos = foro.hilo
    
    res['data0'] = [
        {'idMensaje':hilo.id, 'titulo':hilo.titulo} for hilo in hilos
    ]
    
    '''
    res['data0'] = [
      {'idMensaje':1, 'titulo':'Puntos por tarea'},
      {'idMensaje':2, 'titulo':'Re:Puntos por tarea'},
      {'idMensaje':3, 'titulo':'Voy adelantado'}
    ]
    '''
    
    #Action code ends here
    return json.dumps(res)



@foro.route('/foro/VForos')
def VForos():
    #GET parameter
    idUsuario = request.args['idUsuario']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    foros = Foro.query.order_by(asc(Foro.timestamp)).all()

    res['data0'] = [
        {'idForo':foro.id, 'nombre':foro.titulo} for foro in foros
    ]

    #Action code ends here
    return json.dumps(res)



@foro.route('/foro/VPublicacion')
def VPublicacion():
    #GET parameter
    idMensaje = request.args['idMensaje']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    res['idForo'] = 1

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here

