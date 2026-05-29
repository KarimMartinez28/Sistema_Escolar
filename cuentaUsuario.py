class cuentaUsuario:
    
    def __init__(self, correo, contrasenia, rol):
        self.correo = correo
        self.contrasenia = contrasenia
        self.rol = rol              
        self.activo = True          
