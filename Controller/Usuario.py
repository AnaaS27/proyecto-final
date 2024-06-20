from Model.ConexionUsuario import ConexionUsuario
from tkinter import messagebox
from View.MenuCajero import MenuCajero
from Controller.Cajero import Cajero

class Usuario():
    def __init__(self):
        self.cedula = ""
        self.nombre = ""
        self.apellidos = ""
        self.telefono = ""
        self.email = ""
        self.rol = ""
    
    def getCedula(self):
        return self.cedula
    def getNombre(self):
        return self.nombre
    def getApellidos(self):
        return self.apellidos
    def getTelefono(self):
        return self.telefono
    def getEmail(self):
        return self.email
    def getRol(self):
        return self.rol
    
    def setCedula(self, cedula):
        self.cedula = cedula
    def setNombre(self, nombre):
        self.nombre = nombre
    def setApellidos(self, apellidos):
        self.apellidos = apellidos
    def setTelefono(self, telefono):
        self.telefono = telefono
    def setEmail(self, email):
        self.email = email
    def setRol(self, rol):
        self.rol = rol
    
    def iniciarSesion(self, nombreUsuario, password, loggin):
        miConexion = ConexionUsuario()
        miConexion.crearConexion()
        con = miConexion.getConexion()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM usuario")
        listaUsuarios = cursor.fetchall()
        for usuario in listaUsuarios:
            userName = usuario[1]+"."+usuario[2]
            if(userName == nombreUsuario and usuario[0] == password):
                if(usuario[5] == "cajero"):
                    messagebox.showinfo("Mensaje", "Bienvenido Cajero")
                    miCajero = Cajero(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4])
                    miMenu = MenuCajero(loggin, miCajero)
                    break

                else:
                    messagebox.showinfo("Mensaje", "Bienvenido Cliente")
                    break
            else:
                messagebox.showwarning("Advertencia", "El nombre de Usuario y/o Contraseña no existe, verifique e intente nuevamente...")
        miConexion.cerrarConexion()






