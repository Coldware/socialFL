from flask import request, session, Blueprint, json
ident = Blueprint('ident', __name__)
from base import db, Usuario , Pagina, PaginaSitio

@ident.route('/ident/AIdentificar', methods=['POST'])
def AIdentificar():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VPrincipal', 'msg':'¡Bienvenido '+params['usuario']+'!', "actor":"duenoProducto","idUsuario":params['usuario']},{'label':'/VLogin','msg':['Datos de identificación incorrectos']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    try: #If the information exists and is correct then u can login
        usuario = Usuario.query.filter_by(login=params['usuario']).first()
        if usuario.clave!=params['clave']:
            res = results[1]
        res['idUsuario'] = usuario.id
    except:
        res = results[1]

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']            
            session['idUsuario'] = res['idUsuario'] # Este idUsuario es el id 
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

    session.clear()

    #Action code ends here
    return json.dumps(res)



@ident.route('/ident/VPrincipal')
def VPrincipal():
    res = {}
    if 'idPaginaSitio' in session:
        del session['idPaginaSitio']
    if "actor" in session:
        res['actor']=session['actor']
        res['idPagina'] = 'Sin Pagina'
        
    #Action code goes here, res should be a JSON structure
    if 'idUsuario' in session: # Veo si el id de usuario esta en la sesion 
        res['idUsuario'] = session['idUsuario']
        try: #Si esta busco si tiene pagina
            usuario = Usuario.query.get(res['idUsuario'])
            pagina = Pagina.query.filter_by(usuario_id=res['idUsuario']).first()
            res['idPagina'] = pagina.id
        except: 
            print ('SIN PAGINA')     
    else:
        print(session)    
        

    # Funcion de comentarios
    try: #Busco si exite pagina sitio principal
        paginaSitio = PaginaSitio.query.filter_by(url='/VPrincipal').first()
        publicaciones = paginaSitio.publicacion    
        res['data0'] = []
        for publicacion in publicaciones:
            autor = Usuario.query.get(publicacion.autor).login
            res['data0'].append({'idMensaje':publicacion.id, 'titulo':publicacion.titulo, 'autor':autor, 'contenido':publicacion.contenido})
    except: 
        paginaSitio = PaginaSitio('/VPrincipal')
        try: #Se prueba el exito de la creacion de pagina
            db.session.add(paginaSitio)
            db.session.commit()
            test = PaginaSitio.query.filter_by(url='/VPrincipal').first()
            x = test.url #Si Test es None esto dara error e ira al except
        except:
            pass
        finally:
            db.session.close()
    #print(res['data0'])  
    
    try:
        res['idPaginaSitio'] = paginaSitio.id 
    except:
        res['idPaginaSitio'] = 1                
    session['idPaginaSitio'] = res['idPaginaSitio']

    # Creacion de paginas de prueba
    for i in range(3):
        try: #Busco si exite
            stringUrl = '/VPrueba' + str(i)
            paginaSitio = PaginaSitio.query.filter_by(url=stringUrl).first()
            test = PaginaSitio.query.filter_by(url=stringUrl).first()
            x = test.url #Si Test es None esto dara error e ira al except
        except: # Si no existe se crea
            paginaSitio = PaginaSitio(stringUrl)
            try: #Se prueba el exito de la creacion de pagina
                db.session.add(paginaSitio)
                db.session.commit()
                test = PaginaSitio.query.filter_by(url=stringUrl).first()
                x = test.url #Si Test es None esto dara error e ira al except
            except:
                pass
            finally:
                db.session.close()

    # Funcion de otras paginas de sitios
    res['data1'] = []
    paginas = PaginaSitio.query.all()
    paginaActual = PaginaSitio.query.filter_by(id=res['idPaginaSitio']).first()
    paginas.remove(paginaActual) # Quitamos pagina actual de la lista

    res['data1'] = [
        {'idPagina':pag.id, 'url':pag.url} for pag in paginas
    ] 
    #print(res['data1'])

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


