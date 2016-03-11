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
    
    res['label'] = res['label'] + '/' + session['idUsuario']
    usuario = Usuario.query.filter_by(login=session['idUsuario']).first()
    
    pagina = Pagina(
        params["titulo"],
        params["contenido"],
        usuario
    ) #Create the table in the DB
    
    try: #If user is not in the DB it will register
        res['idUsuario'] = usuario.login
        db.session.add(pagina)
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
        res['label'] = res['label'] + '/' + session['idUsuario']
        print('PAGINA EXISTE Y ES %s'%idPagina)
    else: #Si no exite ir al editor de páginas.
        print('PAGINA NO EXISTEY ES %s'%idPagina)
        res['label'] = res['label'] + '/' + session['idUsuario']

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
    
    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here



