class Pago:
    def __init__(self, monto, fecha):
        self.monto = monto
        self.fecha = fecha
        
    def generar_recibo(self):
        return f"Recibo de pago: {self.monto} en fecha {self.fecha}"
         
class PagoTarjeta(Pago):
    def __init__(self, monto, fecha, numero_tarjeta, titular, saldo):
        super().__init__(monto, fecha)
        self.numero_tarjeta = numero_tarjeta
        self.titular = titular
        self.saldo = saldo
    
    def retirar(self, retiro):
        if self.saldo >= retiro:
            self.saldo -= retiro
            return print(f"Pago realizado con tarjeta {self.numero_tarjeta}. Saldo restante: {self.saldo}")
        else:
            return print("Saldo insuficiente para realizar el pago")
        
    def ingresar(self, ingreso):
        self.saldo += ingreso
        return print(f"Pago ingresado con tarjeta {self.numero_tarjeta}. Nuevo saldo: {self.saldo}")
    
    def generar_recibo(self):
        return print(f"Numero tarjeta: {self.numero_tarjeta}, Titular: {self.titular}, Saldo: {self.saldo}, {super().generar_recibo()}")
        
    
class PagoPaypal(Pago):
    def __init__(self, monto, fecha, email, saldo):
        super().__init__(monto, fecha)
        self.email = email
        self.saldo = saldo

    def generar_recibo(self):
        return print(f"Email: {self.email}, Saldo: {self.saldo}, {super().generar_recibo()}")
    
    def retirar(self, retiro):
        if self.saldo >= retiro:
            self.saldo -= retiro
            return print(f"Pago realizado a {self.email}. Saldo restante: {self.saldo}")
        else:
            return print("Saldo insuficiente para realizar el pago")
    
    def ingresar(self, ingreso):
        self.saldo += ingreso
        return print(f"Pago ingresado a {self.email}. Nuevo saldo: {self.saldo}")
        
               
if __name__ == "__main__":
    TP = PagoTarjeta(100, "2025-10-01", "1234-5678-9012-3456", "Juan Perez", 500)
    TE = PagoPaypal(100, "2025-10-02", "ejemplo@gmail.com", 500)
    TP.generar_recibo()
    TP.retirar(500)
    TP.ingresar(200)
    TP.generar_recibo()
    print()
    TE.generar_recibo()
    TE.retirar(600)
    TE.retirar(500)
    TE.ingresar(200)
    TE.generar_recibo()
