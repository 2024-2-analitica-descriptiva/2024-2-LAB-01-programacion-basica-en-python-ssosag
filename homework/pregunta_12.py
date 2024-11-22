"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    from homework.load_data import loadData

    data = loadData()
    dicRta = {}

    for linea in data:
        letra = linea[0]
        dic = linea[4].split(",")
        suma = 0
        for claveValor in dic:
            _, valor = claveValor.split(":")
            suma += int(valor)

        if letra not in dicRta:
            dicRta[letra] = suma
        else:
            dicRta[letra] += suma

    return dict(sorted(dicRta.items()))


print(pregunta_12())
