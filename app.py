import xml.etree.ElementTree as ET
from flask import Flask, jsonify, request
from Lista.Lista import ListaEnlazada

listadatos = ListaEnlazada()
app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({"mensage":"Exito"})

#OBTIENE LA INFORMACION ANTERIORMENTE INGRESADA
@app.route('/getInformacion',methods=['GET'])
def getInformacion():
    data = listadatos.retornarInfomacion()

    salida = '<?xml version="1.0" encoding="UTF-8"?>\r\n<ESTADISTICAS>\t\n<CANTIDAD_MENSAJES>'+str(len(data))+'</CANTIDAD_MENSAJES>\t\n</ESTADISTICA>'
    for i in range(len(data)):
        salida += '\t\t<FECHA>'+str(data[i]['fecha'])+'</FECHA>\n\t\t<USUARIO>'+str(data[i]['usuario'])+'</USUARIO>\t\t<CODIGO>'+str(data[i]['codigo'])+'</CODIGO>\t\t<AFECTADOS>'+str(data[i]['afectado'])+'</AFECTADOS>\t\t<ERROR>'+str(data[i]['error'])+'</ERROR>\n'

    salida += '\t</ESTADISTICA>\n</ESTADISTICAS>'

    return jsonify(salida) 

#POR MEDIO DE PARAMETROS ESPECIFICOS BUSCA LA INFORMACION EN LA LISTA
@app.route('/search/<string:dato1>/<string:dato2>',methods=['GET'])
def search(dato1,dato2):
    fecha = str(dato1).replace("-","/")
    data = listadatos.busqueda(fecha,str(dato2))

    salida = '<?xml version="1.0" encoding="UTF-8"?>\n<ESTADISTICAS>\t\n<CANTIDAD_MENSAJES>'+str(len(data))+'</CANTIDAD_MENSAJES>\t\n</ESTADISTICA>'
    for i in range(len(data)):
        salida += '\t\t<FECHA>'+str(data[i]['fecha'])+'</FECHA>\n\t\t<USUARIO>'+str(data[i]['usuario'])+'</USUARIO>\t\t<CODIGO>'+str(data[i]['codigo'])+'</CODIGO>\t\t<AFECTADOS>'+str(data[i]['afectado'])+'</AFECTADOS>\t\t<ERROR>'+str(data[i]['error'])+'</ERROR>\n'

    salida += '\t</ESTADISTICA>\n</ESTADISTICAS>'
    
    return jsonify(salida)

#TOMA LA INFORMACION DEL XML LOCAL Y GUARDA LA INFORMACION EN UNA LISTA ENLAZADA SIMPLE
@app.route('/setInformacion',methods=['GET'])
def setInformacion():
    tree = ET.parse('data.xml')
    root = tree.getroot()

    for elem in root:
        datos = str(elem.text).strip().replace('\t','').split('\n')
        fecha = str(datos[0]).split(",")
        #print("fecha: "+str(fecha[1]) )
        usuario = str(datos[1]).split(':')
        #print("usuario: "+str(usuario[1]) )
        afectados = str(datos[2]).split(':')
        #print("afectados: "+str(afectados[1]) )
        codigo = str(datos[3]).replace('-',":").split(':')
        #print("codigo: "+str(codigo[1]) )
        contador = 4
        error = str(codigo[2])+" "
        while(contador < len(datos)):
            error += str(datos[contador])+" "
            contador += 1
        #print("Descripcion del error: "+str(descripcionError))
        listadatos.incertar(str(fecha[1]).strip(),str(usuario[1]).strip(),afectados[1],str(codigo[1]).strip(),error)

    return jsonify({"message":"Datos Guardados con exito en la base de datos"})

#TOMA EL XML Y LO CONVIERTE EN UN ARCHIVO LOCAL
@app.route('/post_xml', methods=['POST'])
def post_xml():
    print("Solicitud aceptada con exito")
    cuerpo = request.data
    file = open('data.xml',"wb")
    file.write(cuerpo)
    file.close()

    return jsonify({"message":"added"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)