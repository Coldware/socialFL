from flask import request, session, Blueprint, json

paginas = Blueprint('paginas', __name__)
from base import db, Pagina, Usuario

@paginas.route('/paginas/AModificarPagina', methods=['POST'])
def AModificarPagina():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VPagina', 'msg':['Cambios almacenados']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    res['label'] = res['label'] + '/' + str(session['idUsuario'])
    usuario = Usuario.query.get(session['idUsuario'])
    paginaAnterior = Pagina.query.filter_by(pagina_id=usuario.id).first()
    #print(paginaAnterior)

    if paginaAnterior is None: # Vemos si esta modificando o creando
        pagina = Pagina( 
            params["titulo"],
            params["contenido"],
            usuario
        ) #Create the table in the DB
        try: #If user is not in the DB it will register
            db.session.add(pagina)
            db.session.commit()
        except:
            res['msg'] = 'Ya existe el titulo en la base de datos.'
    else: # Caso Modificar
        try: #If user is not in the DB it will register    
            paginaAnterior.titulo = params["titulo"]
            paginaAnterior.contenido = params["contenido"]
            db.session.commit()
        except:
            res['msg'] = 'Ya existe el titulo en la base de datos.'    
    db.session.close()

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@paginas.route('/paginas/APagina')
def APagina():
    #GET parameter
    idPagina = request.args['idPagina']
    results = [{'label':'/VPagina', 'msg':[]}, {'label':'/VMiPagina', 'msg':[]}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    #Cuando la página exista, ir directamente a ella. 
    if idPagina != 'Sin Pagina':
        res = results[1]
        res['label'] = res['label'] + '/' + str(session['idUsuario'])
        #print('PAGINA EXISTE Y ES %s'%idPagina)
    else: #Si no exite ir al editor de páginas.
        #print('PAGINA NO EXISTEY ES %s'%idPagina)
        res['label'] = res['label'] + '/' + str(session['idUsuario'])

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@paginas.route('/paginas/VMiPagina')
def VMiPagina():
    #GET parameter
    idUsuario = request.args['idUsuario']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    try: #Busco si tiene pagina
        usuario = Usuario.query.get(idUsuario)
        pagina = Pagina.query.filter_by(pagina_id=usuario.id).first()
        res['titulo'] = pagina.titulo   #Devolvemos titulo y contenido
        res['contenido'] = pagina.contenido
        res['idUsuario'] = idUsuario
    except: # Si no encontramos pagina colocamos datos por defecto
        res['titulo'] = "El título de mi página"
        res['contenido'] = "<h3>¿No es bella mi página?</h3><p>Claro que <b>si</b>.</p>" 
    

    #Action code ends here
    return json.dumps(res)



@paginas.route('/paginas/VPagina')
def VPagina():
    #GET parameter
    idUsuario = request.args['idUsuario']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    res['idPagina'] = 1
    try: #Busco si tiene pagina
        usuario = Usuario.query.get(idUsuario)
        pagina = Pagina.query.filter_by(pagina_id=usuario.id).first()
        res['titulo'] = pagina.titulo   #Devolvemos titulo y contenido
        res['contenido'] = pagina.contenido
        res['idUsuario'] = idUsuario
    except: # Si no encontramos pagina colocamos datos por defecto
        res['titulo'] = 'Sin Pagina'
        res['contenido'] = 'Sin Pagina'

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here

