"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    from homework.load_data import loadData

    data = loadData()

    letras = {}

    for fila in data:
        letra = fila[0]
        numero = int(fila[1])

        if letra not in letras:
            letras[letra] = [numero, numero]
        else:
            if numero > letras[letra][0]:
                letras[letra][0] = numero
            if numero < letras[letra][1]:
                letras[letra][1] = numero
    return sorted(
        [(letra, maximo, minimo) for letra, (maximo, minimo) in letras.items()]
    )
