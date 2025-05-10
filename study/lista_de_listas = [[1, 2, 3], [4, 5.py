lista_de_listas = [[1, 2, 3], [4, 5], [6, 7, 8]]
aplanada = [elemento for sublista in lista_de_listas for elemento in sublista]
print(aplanada)
# Salida: [1, 2, 3, 4, 5, 6, 7, 8]