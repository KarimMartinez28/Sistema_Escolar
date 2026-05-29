from Database import conexion
from Funciones import autenticacion

def dibujar_login():
    print("\n" + "="*36)
    print("         👤 [INICIO DE SESIÓN]        ")
    print("="*36)
    
    print(" Tipo de usuario:")
    print("  1. Alumno")
    print("  2. Maestro")
    print("  3. Administrador")
    opc_rol = input(" Selecciona una opción (1-3): ")
    
    if opc_rol == "1":
        rol_seleccionado = "Alumno"
    elif opc_rol == "2":
        rol_seleccionado = "Maestro"
    elif opc_rol == "3":
        rol_seleccionado = "Administrador"
    else:
        print("\n❌ Opción de usuario no válida.")
        return

    print("-" * 36)
    id_ingresado = input(" 🔑 ID / No. Control: ")
    contra_ingresada = input(" 🔒 Contraseña: ")
    print("-" * 36)
    print("          [ Entrando... ]            ")
    print("="*36)

    # Llamamos a la función que está dentro de la carpeta Funciones
    usuario = autenticacion.validar_login(id_ingresado, contra_ingresada, rol_seleccionado)

    if usuario:
        print(f"\n✅ ¡Bienvenido al sistema, {usuario.nombre}!")
        print(f" Acceso autorizado como: {usuario.cuenta.rol}")
    else:
        print("\n❌ Error: ID, contraseña o tipo de usuario incorrectos.")
        print(" ¿Olvidaste tu contraseña? Manda correo.")

if __name__ == "__main__":
    # Inicializamos la base de datos simulada antes de iniciar
    conexion.inicializar_datos()
    
    # Arranca la pantalla basada en tu diseño a lápiz
    dibujar_login()
