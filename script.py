import pandas as pd
import numpy as np
import networkx as nx
from collections import Counter
import matplotlib.pyplot as plt
from tabulate import tabulate

dataset = pd.read_csv('./dataset.csv', index_col=None) # Importamos el dataset

# Se crea un grafico con los datos del dataset
TRANSMI = nx.from_pandas_edgelist(dataset, source='origen', target='destino', edge_attr='longitud de interaccion')

# Se utiliza el algoritmo de Dijkstra para saber la ruta más rápida entre destinos A y B
destinos = [
    ['Portal Tunal', 'Portal Suba'],
    ['Olaya', 'Portal Suba'],
    ['Gratamira', 'Flores'],
    ['General Santander', 'Portal Tunal'],
    ['Portal Norte', 'Portal 80']
]

posibles_rutas = []
for destino in destinos:
  opcion = nx.dijkstra_path(TRANSMI, source=f"{destino[0]}", target=f"{destino[1]}", weight=True)
  posibles_rutas.append(opcion)

# Result
print(tabulate(posibles_rutas, tablefmt="pretty"))

# Se Traen algunas estaciones destino del dataset
algunas_estaciones = dataset[['destino']]
# Se convierte a un Array
destinos = algunas_estaciones.to_numpy()
# Se define un array vacio para guardar el numero de rutas por estacion
rutas = []
# Se eliminan los valores repetidos del array
portales = np.unique(destinos)

# se Itera sobre el array para saber la cantidad de rutas
for portal in portales:
# se cuentan las coincidencias de la estación en las rutas destino
  cantidad_rutas = np.count_nonzero(destinos == portal)
  # se guarda el valor
  rutas.append(cantidad_rutas)

# Se cambia el tamaño de la gráfica
plt.figure(figsize=(15, 5))
# se Define los valores de la gráfica de dispersión
plt.scatter(portales, rutas)
plt.show()
