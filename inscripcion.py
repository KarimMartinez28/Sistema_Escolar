class Inscripcion:

    def __init__(self, id_inscripcion, alumno, materia, fecha_registro="21/05/2026"):
        self.id_inscripcion = id_inscripcion
        self.alumno = alumno           # Recibe el objeto Alumno completo
        self.materia = materia         # Recibe el objeto Materia completo
        self.fecha_registro = fecha_registro
        self.estatus = "Activo"        # Puede ser: Activo o Dado de Baja
