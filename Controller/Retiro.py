from Transaccion import Transaccion
class Retiro(Transaccion):
    def realizar_transaccion(self, monto):
        if self.cuenta.saldo >= monto:
            self.cuenta.saldo -= monto
            print(f"Retiro de {monto} realizado con éxito en la cuenta {self.cuenta.numero_cuenta}")
        else:
            print("No hay suficiente saldo en la cuenta")