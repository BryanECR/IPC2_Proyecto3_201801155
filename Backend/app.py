from flask import Flask, jsonify, request
from Lista.Lista import ListaEnlazada

listadatos = ListaEnlazada()
app = Flask(__name__)

@app.route('/ping')
def ping():
    return "algo"

#TOMA UN ARREGLO DE DICCIONARIOS Y AGREGA LA INFORMACION A UNA LISTA ENLAZADA
@app.route('/setInformacion',methods=['POST'])
def setInformacion():
    datos = request.get_json()
    for info in datos:
        fecha = info['fecha']
        usuario = info['usuario']
        afectado = info['afectado']
        codigo = info['codigo']
        error = info['error']
        listadatos.incertar(fecha,usuario,afectado,codigo,error)

    print("Agregados correctamente")
    return jsonify({"mensage":"Informacion aceptada correctamente"})

#OBTIENE LA INFORMACION ANTERIORMENTE INGRESADA
@app.route('/getInformacion',methods=['GET'])
def getInformacion():
    datos = listadatos.retornarInfomacion()
    return jsonify(datos)

#POR MEDIO DE PARAMETROS ESPECIFICOS BUSCA LA INFORMACION EN LA LISTA
@app.route('/search/<string:dato1>/<string:dato2>',methods=['GET'])
def search(dato1,dato2):
    fecha = str(dato1).replace("-","/")
    data = listadatos.busqueda(fecha,str(dato2))
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)