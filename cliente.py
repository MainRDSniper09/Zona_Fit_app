class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self.id = id
        self._nombre = nombre
        self._apellido = apellido
        self._membresia = membresia

    # Gets and Sets
    def get_nombre(self):
        return self._nombre
    def get_apellido(self):
        return self._apellido
    def get_membresia(self):
        return self._membresia

    def set_nombre(self, nombre):
        self._nombre = nombre
    def set_apellido(self, apellido):
        self._apellido = apellido
    def set_membresia(self, membresia):
        self._membresia = membresia

    def __str__(self):
        return f'Id: {self.id}, Nombre: {self.get_nombre()}, Apellido: {self.get_apellido()}, Membresia: {self.get_membresia()}'  # Se imprime los datos