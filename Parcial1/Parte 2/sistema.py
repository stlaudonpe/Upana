from cliente import Cliente

class Sistema:
    def __init__(self):
        self.__clientes = {}

    def crear_cliente(self, nombre, fecha_nacimiento, municipio, numero_usuario):
        nuevo_cliente = Cliente(nombre, fecha_nacimiento, municipio, numero_usuario)
        self.__clientes[numero_usuario] = nuevo_cliente
        print(f"Cliente {nombre} creado con número de usuario {numero_usuario}.")

    def agregar_servicio(self, numero_usuario, servicio):
        cliente = self.__clientes.get(numero_usuario)
        if cliente:
            cliente.agregar_servicio(servicio)
        else:
            print("Cliente no encontrado.")

    def listar_usuarios(self):
        for cliente in self.__clientes.values():
            print(f"Nombre: {cliente.get_nombre_completo()}, Número de usuario: {cliente.get_numero_usuario()}")

    def mostrar_informacion_usuario(self, numero_usuario):
        cliente = self.__clientes.get(numero_usuario)
        if cliente:
            cliente.listar_servicios()
        else:
            print("Cliente no encontrado.")
