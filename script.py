import math
import pandas as pd
import numpy as np
import networkx as nx
from collections import Counter
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from tabulate import tabulate

dataset = pd.read_csv('./dataset.csv', index_col=None) # Importamos el dataset

# Se crea un grafo con los datos del dataset
TRANSMI = nx.from_pandas_edgelist(dataset, source='origen', target='destino', edge_attr='longitud de interaccion')
# TRANSMI.nodes() Nodos
# TRANSMI.edges() Aristas
# TRANSMI.order() Ordenar elementos

# Se utiliza el algoritmo de Dijkstra para saber la ruta más rápida entre destinos A y B
destinos = [
    ['Portal Norte', 'Portal 80'],
    ['Ricaurte', 'General Santander'],
    ['Perdomo', 'Flores'],
    ['Tercer Milenio', 'Portal Tunal'],
    ['Calle 100', 'Madelena']
]

posibles_rutas = []
for destino in destinos:
  opcion = nx.dijkstra_path(TRANSMI, source=f"{destino[0]}", target=f"{destino[1]}", weight=True)
  posibles_rutas.append(opcion)

# Result
print(tabulate(posibles_rutas, tablefmt="pretty"))

# Traemos algunas estaciones destino del dataset
algunas_estaciones = dataset[['destino']]
# Lo convertidos a un Array
destinos = algunas_estaciones.to_numpy()
# Definimos un array vacio para guardar el numero de rutas por estacion
rutas = []
# Eliminamos los valores repetidos del array
portales = np.unique(destinos)

# Iteramos sobre el array para saber la cantidad de rutas
for portal in portales:
  # Contamos las coincidencias de la estación en las rutas destino
  cantidad_rutas = np.count_nonzero(destinos == portal)
  # Guardamos el valor
  rutas.append(cantidad_rutas)
  
#plt.ion()
plt.plot(portales,rutas,lw=5, c='y', marker='o', ms=10, mfc='b')


# Cambiamos el tamaño de la gráfica
#plt.figure(figsize=(15, 7))
# Definimos los valores de la gráfica de dispersión
#plt.scatter(portales, rutas)


#Colocamos las etiquetas de los ejes
plt.xlabel("Estaciones")
plt.ylabel("Cantidad De Rutas")

#Colocamos la leyenda
#plt.legend(['Rutas','Estaciones'])

#Colocamos el título del gráfico
plt.title("Gráfica De Dispersión")
plt.show()