from Transaccion import Transaccion

class Deposito(Transaccion):
    def realizar_transaccion(self, monto):
        self.cuenta.saldo += monto
        print(f"Depósito de {monto} realizado con éxito en la cuenta {self.cuenta.numero_cuenta}")