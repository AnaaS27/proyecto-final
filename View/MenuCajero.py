import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip

from View.AgregarCliente import AgregarCliente

class MenuCajero():
    def agregarCliente(self):
        vistaAgregar = AgregarCliente(self.ventana, self.cajero)

    def __init__(self, loggin, cajero):
        self.ventana = tk.Toplevel(loggin)
        self.ventana.resizable(0,0)
        self.ventana.config(width=400, height=400)
        self.ventana.title("Menú")

        self.cajero = cajero

        self.lblTitulo = tk.Label(self.ventana, text="Menú Cajero")
        self.lblTitulo.place(relx= 0.5, rely=0.1, anchor="center")

        self.btnAgregar = tk.Button(self.ventana, text="Agregar Cliente", command= lambda: self.agregarCliente())
        self.btnAgregar.place(relx= 0.5, rely=0.4, anchor="center")
        Tooltip(self.btnAgregar, "Presione para agregar un nuevo Cliente")

        self.btnModificar = tk.Button(self.ventana, text="Modificar Cliente", command= lambda: self.modificarCliente())
        self.btnModificar.place(relx= 0.5, rely=0.6, anchor="center")
        Tooltip(self.btnModificar, "Presione para modificar un Cliente")

        self.btnEliminar = tk.Button(self.ventana, text="Eliminar Cliente", command= lambda: self.eliminarCliente())
        self.btnEliminar.place(relx= 0.5, rely=0.8, anchor="center")
        Tooltip(self.btnEliminar, "Presione para eliminar un Cliente")

        self.ventana.mainloop()