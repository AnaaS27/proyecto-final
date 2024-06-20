import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip

class AgregarCliente():
    def agregarCliente(self):
        pass

    def __init__(self, menu, cajero):
        self.ventana = tk.Toplevel(menu)
        self.ventana.resizable(0,0)
        self.ventana.config(width=400, height=400)
        self.ventana.title("Agregar Cliente")

        self.cajero = cajero

        self.lblTitulo = tk.Label(self.ventana, text="Agregar Cliente")
        self.lblTitulo.place(relx= 0.5, rely=0.1, anchor="center")

        self.lblCedula = tk.Label(self.ventana, text="Cédula*: ")
        self.lblCedula.place(relx= 0.2, rely=0.3)

        self.txtCedula = tk.Entry(self.ventana)
        self.txtCedula.place(relx= 0.5, rely=0.3, width= 150, height= 25)

        self.lblNombre = tk.Label(self.ventana, text="Nombre*: ")
        self.lblNombre.place(relx= 0.2, rely=0.5)

        self.txtNombre = tk.Entry(self.ventana)
        self.txtNombre.place(relx= 0.5, rely=0.5, width= 150, height= 25)

        self.lblTelefono = tk.Label(self.ventana, text="Telefono*: ")
        self.lblTelefono.place(relx= 0.2, rely=0.7)

        self.txtTelefono = tk.Entry(self.ventana)
        self.txtTelefono.place(relx= 0.5, rely=0.7, width= 150, height= 25)

        self.btnAgregar = tk.Button(self.ventana, text="Agregar Cliente", command= lambda: self.agregarCliente())
        self.btnAgregar.place(relx= 0.5, rely=0.9, anchor="center")
        Tooltip(self.btnAgregar, "Presione para agregar un nuevo Cliente")

        self.ventana.mainloop()