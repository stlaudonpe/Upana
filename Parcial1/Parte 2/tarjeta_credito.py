class TarjetaDeCredito:
    def __init__(self, numero_tarjeta, fecha_adquisicion, fecha_vencimiento, tipo, limite_credito):
        self.__numero_tarjeta = numero_tarjeta
        self.__fecha_adquisicion = fecha_adquisicion
        self.__fecha_vencimiento = fecha_vencimiento
        self.__tipo = tipo
        self.__limite_credito = limite_credito

    def mostrar_detalles(self):
        print(f"Tarjeta de Crédito: {self.__numero_tarjeta}, Fecha de Adquisición: {self.__fecha_adquisicion}, "
              f"Vencimiento: {self.__fecha_vencimiento}, Tipo: {self.__tipo}, Límite de Crédito: {self.__limite_credito}")
