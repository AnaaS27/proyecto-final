import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip
from Controller.Usuario import Usuario

class Loggin():

    def validarIngreso(self):
        miUsuario = Usuario()
        miUsuario.iniciarSesion(self.txtUsuario.get(), self.txtPassword.get(), self.ventana)

    def __init__(self):
            self.ventana = tk.Tk()
            self.ventana.resizable(0,0)
            self.ventana.title("Loggin")

            tk.Label(self.ventana, text="Inicio de Sesión").grid(row=0, columnspan=2)
            tk.Label(self.ventana, text="Usuario*:", width=20).grid(row=1)
            tk.Label(self.ventana, text="Password*:", width=20).grid(row=2)

            self.txtUsuario = tk.Entry(self.ventana, width=25)
            self.txtUsuario.grid(row=1, column=1)
            Tooltip(self.txtUsuario, "Ingrese su nombre de Usuario")
            self.txtPassword = tk.Entry(self.ventana, show="*", width=25)
            self.txtPassword.grid(row=2, column=1)
            Tooltip(self.txtPassword, "Ingrese su nombre de Contaseña")

            self.btnIngresar = tk.Button(self.ventana, text="Ingresar", command= lambda: self.validarIngreso())
            self.btnIngresar.grid(row=3, columnspan=2)
            Tooltip(self.btnIngresar, "Presione para ingresar al Sistema")

            self.txtUsuario.insert(END, '')
            self.txtPassword.insert(END, '')
            

            self.ventana.mainloop()