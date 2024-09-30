class TarjetaDeDebito:
    def __init__(self, numero_tarjeta, fecha_adquisicion, fecha_vencimiento, numero_cuenta_asociada):
        self.__numero_tarjeta = numero_tarjeta
        self.__fecha_adquisicion = fecha_adquisicion
        self.__fecha_vencimiento = fecha_vencimiento
        self.__numero_cuenta_asociada = numero_cuenta_asociada

    def mostrar_detalles(self):
        print(f"Tarjeta de Débito: {self.__numero_tarjeta}, Fecha de Adquisición: {self.__fecha_adquisicion}, "
              f"Vencimiento: {self.__fecha_vencimiento}, Cuenta Asociada: {self.__numero_cuenta_asociada}")
