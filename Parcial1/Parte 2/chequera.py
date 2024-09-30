class Chequera:
    def __init__(self, numero_chequera, fecha_adquisicion, fecha_vencimiento, cantidad_cheques):
        self.__numero_chequera = numero_chequera
        self.__fecha_adquisicion = fecha_adquisicion
        self.__fecha_vencimiento = fecha_vencimiento
        self.__cantidad_cheques = cantidad_cheques
        self.__cheques_entregados = []

    def agregar_cheque(self, numero_cheque):
        if len(self.__cheques_entregados) < self.__cantidad_cheques:
            self.__cheques_entregados.append(numero_cheque)
            print(f"Cheque {numero_cheque} entregado.")
        else:
            print("No se pueden entregar más cheques, la chequera está completa.")

    def mostrar_detalles(self):
        print(f"Chequera - Número: {self.__numero_chequera}, Fecha de Adquisición: {self.__fecha_adquisicion}, "
              f"Fecha de Vencimiento: {self.__fecha_vencimiento}, Cantidad de Cheques: {self.__cantidad_cheques}")
        print(f"Cheques Entregados: {self.__cheques_entregados}")
