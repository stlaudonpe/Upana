from sistema import Sistema
from cuenta_ahorro import CuentaDeAhorro
from tarjeta_credito import TarjetaDeCredito
from tarjeta_debito import TarjetaDeDebito
from chequera import Chequera

# Crear el sistema
sistema = Sistema()

# Crear clientes
sistema.crear_cliente("Luis Audon", "1990-04-15", "Guatemala", "A001")
sistema.crear_cliente("Gaby Matheu", "1985-10-22", "Peten", "B002")

# Crear servicios
cuenta_ahorro = CuentaDeAhorro("2841057473", "2023-01-01", 1.5)
tarjeta_credito = TarjetaDeCredito("1564617970033028", "2023-05-01", "2025-05-01", "Sol", 5000)
tarjeta_debito = TarjetaDeDebito("1277899624910881", "2023-06-15", "2025-06-15", "123456")
chequera = Chequera("789456", "2023-07-01", "2025-07-01", 25)

# Agregar servicios a los clientes
sistema.agregar_servicio("A001", cuenta_ahorro)
sistema.agregar_servicio("A001", tarjeta_credito)
sistema.agregar_servicio("B002", tarjeta_debito)
sistema.agregar_servicio("B002", chequera)

# Listar clientes y mostrar información
sistema.listar_usuarios()
sistema.mostrar_informacion_usuario("A001")
sistema.mostrar_informacion_usuario("B002")
