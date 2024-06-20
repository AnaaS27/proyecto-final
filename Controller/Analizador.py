class Analizador:
    def _init_(self, fecha=None):
        self.fecha = fecha

def calcular_saldo_promedio(self, cuentas):
        suma_saldos = sum(cuenta.saldo for cuenta in cuentas)
        return suma_saldos / len(cuentas)