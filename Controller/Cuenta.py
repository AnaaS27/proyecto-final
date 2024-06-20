class Cuenta:
    def _init_(self, numero_cuenta, cedula_cliente, saldo=0):
        self.numero_cuenta = numero_cuenta
        self.cedula_cliente = cedula_cliente
        self.saldo = saldo

    def _str_(self):
        return f"Número de cuenta: {self.numero_cuenta}, Saldo: {self.saldo}, Usuario: {self.cedula_cliente}"