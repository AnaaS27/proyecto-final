class Transaccion:
    def _init_(self, numero_transaccion, cuenta, monto):
        self.numero_transaccion = numero_transaccion
        self.cuenta = cuenta
        self.monto = monto

    def realizar_transaccion(self, monto):
        raise NotImplementedError("Debes implementar esta función en la clase hija")