from Modulos.UsuarioGeneral import UsuarioGeneral

class maestro(UsuarioGeneral):
    
    def __init__(self, id_usuario, nombre, correo, contrasenia):
        super().__init__(id_usuario, nombre, correo, contrasenia, "Maestro")
        self.horario = None      
        self.materia = None 