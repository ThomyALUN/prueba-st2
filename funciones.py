from io import StringIO

def leerArchivo(archivo, separador:str=","):
    datosDecod = StringIO(archivo.getvalue().decode("utf-8"))
    datos=datosDecod.readlines()

    for i in range(len(datos)):
        datos[i]=datos[i].strip().split(separador)

    return datos