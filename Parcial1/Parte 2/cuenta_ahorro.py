class CuentaDeAhorro:
    def __init__(self, numero_cuenta, fecha_adquisicion, interes_anual):
        self.__numero_cuenta = numero_cuenta
        self.__fecha_adquisicion = fecha_adquisicion
        self.__interes_anual = interes_anual

    def mostrar_detalles(self):
        print(f"Cuenta de Ahorro: {self.__numero_cuenta}, Fecha de Adquisición: {self.__fecha_adquisicion}, Interés Anual: {self.__interes_anual}")
