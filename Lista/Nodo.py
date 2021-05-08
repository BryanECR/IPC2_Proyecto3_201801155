class Nodo:
    def __init__(self,fecha,usuario,afectado,codigo,DescripcionError):
        self.fecha = fecha,
        self.usuario = usuario,
        self.afectado = afectado,
        self.codigo = codigo,
        self.DescripcionError = DescripcionError,
        self.siguiente = None