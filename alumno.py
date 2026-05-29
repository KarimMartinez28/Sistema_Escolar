from Modulos.UsuarioGeneral import UsuarioGeneral

class alumno(UsuarioGeneral):

       def __init__(self, numero_control, nombre, correo, contrasenia):
        super().__init__(numero_control, nombre, correo, contrasenia, "alumno") 
        self.grupo = None        
        self.horario = None      
        self.promedio = 0.0 