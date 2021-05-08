from Lista.Nodo import Nodo

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    #CONVIERTE UNA TUPLA EN UN STRING
    def convetTuple(tup):
        cadena = ''.join(tup)
        return cadena

    def vacia(self):
        return self.primero == None

    def incertar(self,fecha,usuario,afectado,codigo,DescripcionError):
        if self.vacia():
            self.primero = self.ultimo = Nodo(fecha,usuario,afectado,codigo,DescripcionError)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(fecha,usuario,afectado,codigo,DescripcionError)

    def retornarInfomacion(self):
        aux = self.primero
        datos = []
        while(aux != None):
            fecha = ListaEnlazada.convetTuple(aux.fecha) 
            usuario = ListaEnlazada.convetTuple(aux.usuario)
            afectado = ListaEnlazada.convetTuple(aux.afectado)
            codigo = ListaEnlazada.convetTuple(aux.codigo)
            DescripcionError = ListaEnlazada.convetTuple(aux.DescripcionError)
            informacion = {"fecha":fecha,"usuario":usuario,"afectado":afectado,"codigo":codigo,"error":DescripcionError}
            datos.append(informacion)

            aux = aux.siguiente
        
        return datos

    def busqueda(self,dato1,dato2):
        aux = self.primero
        datos = []
        while(aux != None):
            fecha = ListaEnlazada.convetTuple(aux.fecha)
            usuario = ListaEnlazada.convetTuple(aux.usuario)
            afectado = ListaEnlazada.convetTuple(aux.afectado)
            codigo = ListaEnlazada.convetTuple(aux.codigo)
            DescripcionError = ListaEnlazada.convetTuple(aux.DescripcionError)

            if(str(fecha).strip() == str(dato1) and str(usuario).strip() == str(dato2) ) or (str(fecha).strip() == str(dato1).strip() and str(codigo) == str(dato2) ):
                informacion = {"fecha":fecha,"usuario":usuario,"afectado":afectado,"codigo":codigo,"error":DescripcionError}
                datos.append(informacion)

            aux = aux.siguiente
        
        return datos
