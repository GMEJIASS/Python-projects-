from datetime import datetime
# Clase para representar a un usuario
class Usuario:
    def __init__(self, cedula, nombre, telefono, correo, direccion):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion= direccion 
# Clase para representar una incidencia 
class Indicencia:
    def __init__(self, codigo, descripcion, estado, fecha_registro, geolocalizacion, usuario):
        self.codigo = codigo
        self.descripcion = descripcion
        self.estado = estado
        self.fecha_registro = fecha_registro
        self.geolocalizacion = geolocalizacion
        self.usuario = usuario # Este es un objeto tipo usuario
# Base de datos simulada 
usuarios = {}
incidencias = {}
# Funciones para usuarios 
def agregar_usuarios ():
    cedula = input("cedula: ")
    if cedula in usuarios:
        print("El usuario ya esta registrado.")
        return
    nombre = input("Nombre: ")
    telefono = input ("Telefono: ")
    correo = input ("Correo: ")
    direccion = input ("Direccion: ")
    usuario = Usuario(cedula, nombre, telefono, correo, direccion )
    usuarios[cedula] = usuario
    print("Usuario agregado correctamente.")

def consultar_usuario():
    cedula = input("Ingrese la cedula del usuario: ")
    usuario = usuarios.get(cedula)
    if usuario:
        print(f"Nombre: {usuario.nombre}, telefono: {usuario.telefono}, correo: {usuario.correo}, direccion: {usuario.direccion}")
    else:
        print("Usuario no encontrado.")
# Funciones para incidencias 
def agregar_incidencia():
    codigo = input ("Codigo de incidencia: ")
    if codigo in incidencias:
        print("Ya existe una incidencia con este codigo.")
        return
    descripcion = input("Descripcion: ")
    estado = input("Estado: ")
    fecha_registro = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    geolocalizacion = input("Geolocalizacion (lat, long): ")
    cedula_usuario = input("Cedula del usuario que reporta: ")

    usuario = usuarios.get(cedula_usuario)
    if not usuario:
        print("Usuario no registrado, registre al usuario primero.")
        return
    incidencia = incidencia(codigo, descripcion, estado, fecha_registro, geolocalizacion, usuario)
    incidencias[codigo]= incidencia
    print("Incidencia registrada correctamente ")

def consultar_incidencias():
    codigo = input("Ingrese el codigo de incidencia: ")
    incidencia = incidencias.get(codigo)
    if incidencias:
        print(f"Descripcion: {incidencia.descripcion}")
        print(f"Estado: {incidencia.estado}")
        print(f"Fecha: {incidencia.fecha}")
        print(f"Geolocalizacion: {incidencia.geolocalizacion}")
        print(f"Reportado por: {incidencia.usuario.nombre}")
    else:
            print("incidencia no encontrada.")

def modificar_incidencia():
    codigo = input("codigo de la incidencia a modificar: ")
    incidencia = incidencias.get(codigo)
    if incidencia:
        incidencia.descripcion = input("Nueva descripcion: ")
        incidencia.estado = input("Nuevo estado: ")
        print("Incidencia modificada con exito.")
    else:
            print("Incidencia no encontrada.")

def eliminar_incidencia():
    codigo = input("Codigo de la incidencia a eliminar: ")
    if codigo in incidencias:
        del incidencias[codigo]
        print("Incidencia eliminada.")
    else:
        print("Incidencia no encontrada.")
# Menu Simple 
def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Agregar usuario")
        print("2. Consultar usuario")
        print("3. Agregar inicdencia")
        print("4. Consultar incidencia")
        print("5. Modificar incidencia")
        print("6. Eliminar incidencia")
        print("7. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_usuarios()
        elif opcion == "2":
            consultar_usuario()
        elif opcion == "3":
            agregar_incidencia()
        elif opcion == "4":
            consultar_incidencias()
        elif opcion == "5":
            modificar_incidencia()
        elif opcion == "6":
            eliminar_incidencia()
        elif opcion == "7":
            print("Saliendo del sistema.")
            break 
        else:
            print("Opcion Invalida.")
# Ejecutar menu 
if __name__ == "__main__":
    menu()



        



