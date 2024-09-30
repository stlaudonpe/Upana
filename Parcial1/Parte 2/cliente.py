class Cliente:
    def __init__(self, nombre_completo, fecha_nacimiento, municipio_residencia, numero_usuario):
        self.__nombre_completo = nombre_completo
        self.__fecha_nacimiento = fecha_nacimiento
        self.__municipio_residencia = municipio_residencia
        self.__numero_usuario = numero_usuario
        self.__servicios = []

    def agregar_servicio(self, servicio):
        from tarjeta_credito import TarjetaDeCredito
        if isinstance(servicio, TarjetaDeCredito):
            for s in self.__servicios:
                if isinstance(s, TarjetaDeCredito):
                    print(f"{self.__nombre_completo} ya tiene una tarjeta de crédito.")
                    return
        self.__servicios.append(servicio)
        print(f"Servicio agregado para {self.__nombre_completo}.")

    def listar_servicios(self):
        print(f"Servicios de {self.__nombre_completo}:")
        for servicio in self.__servicios:
            servicio.mostrar_detalles()

    def get_nombre_completo(self):
        return self.__nombre_completo

    def get_numero_usuario(self):
        return self.__numero_usuario
