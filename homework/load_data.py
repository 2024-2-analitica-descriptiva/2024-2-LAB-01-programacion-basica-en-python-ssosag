def loadData():
    data = []
    with open("/files/input/data.csv", "r") as archivo:
        lineas = archivo.read().splitlines()

    for linea in lineas:
        data.append(linea.split("\t"))

    return data
