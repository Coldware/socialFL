# -*- coding: utf-8 -*-

import unittest, time, re 
from base import db, Usuario, Pagina, Mensaje, Chateador, Grupo


class unitTest(unittest.TestCase):
    def setUp(self):
        pass    
    
    def test1_crear_Usuario(self):
        usuario = Usuario('nombrePrueba','loginPrueba','clavePrueba','correo@prueba.com')
        db.session.add(usuario)
        db.session.commit()
    
        # Vemos si se agrego
        user = Usuario.query.filter_by(login='loginPrueba').first()

        if (user == None) or (user.nombre != 'nombrePrueba'):
            verif = 'Error'
        else:
            verif = 'Exito'
            #print(repr(usuario))
            db.session.delete(usuario)
            db.session.commit()
        self.assertEqual(verif, 'Exito')

    def test2_add_contacts(self):
        user1 = Usuario('nombre1Prueba','user1','clavePrueba','correo@prueba.com')
        user2 = Usuario('nombre2Prueba','user2','clavePrueba','correo2@prueba.com')
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
    
        # Vemos si se agregaron
        user1 = Usuario.query.filter_by(login='user1').first()
        user2 = Usuario.query.filter_by(login='user2').first()
        if (user1 == None) or (user1.nombre != 'nombre1Prueba') or \
            (user2 == None) or (user2.nombre != 'nombre2Prueba'):
            verif = 'Error'
        else:
            verif = 'Exito'
        self.assertEqual(verif, 'Exito')


        if not (user1.esContacto(user2)): # Verificamos que no son contactos
            user1.addContact(user2) # Agregamos a contactos
            user2.addContact(user1)
            db.session.commit()
        else:
            verif = 'Error'
        self.assertEqual(verif, 'Exito')

        if user1.esContacto(user2) and user2.esContacto(user1): # Verificamos que son contactos
            verif = 'Exito'
            user1.contacto.remove(user2) # Borramos de contactos y usuarios
            user2.contacto.remove(user1) 
            db.session.delete(user1)
            db.session.delete(user2)
            db.session.commit()
        else:
            verif = 'Error'

        self.assertEqual(verif, 'Exito')


    def test3_crear_Grupo(self):        
        # Creamos usuarios de prueba     
        user1 = Usuario('nombre1Prueba','user1','clavePrueba','correo@prueba.com')
        db.session.add(user1)
        db.session.commit()
    
        # Vemos si se agregaron
        user1 = Usuario.query.filter_by(login='user1').first()
        if (user1 == None) or (user1.nombre != 'nombre1Prueba'):
            verif = 'Error'
        else:
            verif = 'Exito'
        self.assertEqual(verif, 'Exito')

        grupo = Grupo('Grupo Prueba',user1.id)
        db.session.add(grupo)
        db.session.commit()
    
        # Vemos si se agrego
        group = Grupo.query.filter_by(nombre='Grupo Prueba').first()   

        if (group == None) or (group.nombre != 'Grupo Prueba'):
            verif = 'Error'
        else:
            verif = 'Exito'
        self.assertEqual(verif, 'Exito')   

        # Vemos si user1 es duenio y miembro
        if (group.duenio == user1.id) and (group.esMiembro(user1)) :
            verif = 'Exito'
        else:
            verif = 'Error'    
        self.assertEqual(verif, 'Exito') 

        db.session.delete(group) # Borramos grupo y usuarios
        db.session.delete(user1)
        db.session.commit()   




    def test4_addMember(self):   
        # Creamos usuarios de prueba     
        user1 = Usuario('nombre1Prueba','user1','clavePrueba','correo@prueba.com')
        user2 = Usuario('nombre2Prueba','user2','clavePrueba','correo2@prueba.com')
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
    
        # Vemos si se agregaron
        user1 = Usuario.query.filter_by(login='user1').first()
        user2 = Usuario.query.filter_by(login='user2').first()
        if (user1 == None) or (user1.nombre != 'nombre1Prueba') or \
            (user2 == None) or (user2.nombre != 'nombre2Prueba'):
            verif = 'Error'
        else:
            verif = 'Exito'
        self.assertEqual(verif, 'Exito')

        grupo = Grupo('Grupo Prueba',user1.id)
        db.session.add(grupo)
        db.session.commit()
    
        # Vemos si se agrego
        group = Grupo.query.filter_by(nombre='Grupo Prueba').first()   

        if (group == None) or (group.nombre != 'Grupo Prueba'):
            verif = 'Error'
        else:
            verif = 'Exito'
        self.assertEqual(verif, 'Exito')   

        # Vemos si user1 es duenio y miembro
        if (group.duenio == user1.id) and (group.esMiembro(user1)) :
            verif = 'Exito'
        else:
            verif = 'Error'    
        self.assertEqual(verif, 'Exito')        

        group.addMember(user2) # Agregamos a user2 como miembro

        if group.esMiembro(user2): # Verificamos
            verif = 'Exito'
        else:
            verif = 'Error'

        self.assertEqual(verif, 'Exito')           


    def test5_delMember(self): 
        # Vemos si se agregaron los usuarios de test_addMember
        user1 = Usuario.query.filter_by(login='user1').first()
        user2 = Usuario.query.filter_by(login='user2').first()
        if (user1 == None) or (user1.nombre != 'nombre1Prueba') or \
            (user2 == None) or (user2.nombre != 'nombre2Prueba'):
            verif = 'Error'
        else:
            verif = 'Exito'
        self.assertEqual(verif, 'Exito')       
    
        # Vemos si se agrego el grupo de test_addMember
        group = Grupo.query.filter_by(nombre='Grupo Prueba').first()   

        if (group == None) or (group.nombre != 'Grupo Prueba'):
            verif = 'Error'
        else:
            verif = 'Exito'
        self.assertEqual(verif, 'Exito')  
    
        group.delMember(user1) # Quitamos user1 como miembro
        group.delMember(user2) # Quitamos user2 como miembro

        if group.esMiembro(user1) or group.esMiembro(user2): # Verificamos
            verif = 'Error'
        else:
            verif = 'Exito'    
        self.assertEqual(verif, 'Exito')

        db.session.delete(group) # Borramos grupo y usuarios
        db.session.delete(user1) 
        db.session.delete(user2)  
        db.session.commit()   




    
    def tearDown(self):
        pass

if __name__ == "__main__":
     unittest.main(verbosity=2)
