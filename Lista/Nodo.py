class Nodo:
    def __init__(self,fecha,usuario,afectado,codigo,error):
        self.fecha = fecha,
        self.usuario = usuario,
        self.afectado = afectado,
        self.codigo = codigo,
        self.error = error,
        self.siguiente = None