from CuentaBancaria import CuentaBancaria


usuario1 =CuentaBancaria (0.01,1000)
usuario2 = CuentaBancaria (0.02,3000)


usuario1.depósito(10).depósito(20).depósito(30).retiro(100).generar_interés().mostrar_info_cuenta()

usuario2.depósito(15).depósito(25).depósito(35).retiro(50).generar_interés().mostrar_info_cuenta()

CuentaBancaria.mostrar_las_cuentas()