from Modulos.cuentaUsuario import cuentaUsuario

class UsuarioGeneral:
    def __init__(self, id_usuario, nombre, correo, contrasenia, rol):
        self.id = id_usuario
        self.nombre = nombre
        # Tu línea 7 original ya funcionará sin problemas:
        self.cuenta = cuentaUsuario(correo, contrasenia, rol)