class Cuenta:
    def _init_(self, numero_cuenta, saldo=0, usuario=None):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.usuario = usuario

    def _str_(self):
        return f"Número de cuenta: {self.numero_cuenta}, Saldo: {self.saldo}, Usuario: {self.usuario.cedula}"