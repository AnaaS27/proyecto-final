from Controller.Usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nombre, apellido, cedula, telefono, correo):
        super().__init__(nombre, apellido, cedula, telefono, correo)
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
