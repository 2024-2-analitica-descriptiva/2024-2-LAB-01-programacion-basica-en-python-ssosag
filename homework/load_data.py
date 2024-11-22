def loadData():
    import glob

    data = []
    for filepath in glob.glob("files/input/*.csv"):
        with open(filepath, "r") as archivo:
            lineas = archivo.read().splitlines()

        for linea in lineas:
            data.append(linea.split("\t"))

    return data
