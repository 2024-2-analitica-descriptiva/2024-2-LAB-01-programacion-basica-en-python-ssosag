"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    from homework.load_data import loadData

    data = loadData()
    dic = {}

    for linea in data:
        numero = int(linea[1])
        letras = linea[3].split(",")

        for letra in letras:
            if letra not in dic:
                dic[letra] = numero
            else:
                dic[letra] += numero
    return dict(sorted(dic.items()))
