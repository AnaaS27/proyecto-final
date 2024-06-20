from Model.ConexionUsuario import ConexionUsuario
from tkinter import messagebox

class Cajero():
    def __init__(self, cedula, nombre, apellidos, telefono, email):
        self.cedula = cedula
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email
    
    def ingresarCliente(self, cedulaCliente, nombreCliente, telefonoCliente):
        miConexion = ConexionUsuario()
        miConexion.crearConexion()
        con = miConexion.getConexion()
        cursor = con.cursor()
        cursor.execute("INSERT INTO cliente (cedula,nombre,telefono) VALUES (?, ?, ?)",
                       (cedulaCliente, nombreCliente, telefonoCliente))
        messagebox.showinfo("Confirmacion", "El nuevo cliente se registro exitosamente!")
        miConexion.cerrarConexion()
    def modificarCliente(self):
        pass
    def eliminarCliente(self):
        pass