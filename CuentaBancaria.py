class CuentaBancaria:
    # ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    cuentas =[]
    def __init__(self, tasa_interés, balance): 
        # tu código aquí (recuerda, los atributos de instancia van aquí)
        # no te preocupes por la información del usuario aquí; pronto involucraremos la clase de usuario
        self.tasa_interés = tasa_interés
        self.balance = balance
        CuentaBancaria.cuentas.append(self)

    def depósito(self, amount):
        # tu código aquí
        self.balance += amount
        return self

    def retiro(self, amount):
        # tu código aquí
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print ("Fondos insuficientes: cobrando una tarifa de $5")    
            self.balance -= 5
        return self

    def mostrar_info_cuenta(self):
        # tu código aquí
        print (f"Balance:{self.balance}")
        return self

    def generar_interés(self):
        # tu código aquí
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interés)
        return self    
    

    @classmethod
    def mostrar_las_cuentas(cls):
        for cuentas in cls.cuentas:
            cuentas.mostrar_info_cuenta()