# 4. Para la aceptación de un artículo en un congreso se definen las siguientes
#    especificaciones que deben cumplir y recomendaciones de escritura:
#       • título: 10 palabras como máximo
#       • cada oración del resumen:
#       ▪ hasta 12 palabras: fácil de leer
#       ▪ entre 13-17 palabras: aceptable para leer
#       ▪ entre 18-25 palabras: difícil de leer
#       ▪ mas de 25 palabras: muy difícil
#       Dado un artículo en formato string, defina si cumple las especificaciones del título y cuántas oraciones
#       tiene de cada categoría. El formato estándar en que recibe el string tiene la siguiente forma:
#import string
#from posixpath import split
#from time import process_time_ns
evaluar = """ título: Experiences in Developing a Distributed Agent-based
Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance
computing resources provides the promise of capturing unprecedented details
of large-scale complex systems. However, the specialized knowledge required
for developing such ABMs creates barriers to wider adoption and utilization.
Here we present our experiences in developing an initial implementation of
Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High
Performance Computing (Repast HPC), to identify the key elements of a useful
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages
and the Python C-API to create a scalable modeling system that can exploit
the largest HPC resources and emerging computing architectures.
"""

#texto = evaluar.split("\n")
list_of_values = [0,0,0,0]
def titulo():
    """
    Procesa el titulo del texto
    """
    #Saco el titulo
    titulo = (((evaluar.split("\n")[0])).split())
    #Elimino el titulo
    titulo.remove(titulo[0])
    if(len(titulo)<11):
        print("El titulo esta bien")
    else:
        print("El titulo excede la longitud minima")

#Obtengo el resumen
resumen = (((evaluar.split("\n")[0])).split())
#resumen = evaluar.split(".")[:]
resumen.remove(resumen[0])
print(resumen)

def resumen():

    #Elimino la parte del titulo del resumen

    resumen.remove(resumen[0])
    resumen = resumen.split()
    for palabra in resumen:

        if (len(palabra) <= 12):
            list_of_values[0] +=1
        elif(len(palabra) <= 17):
            list_of_values[1] +=1
        elif(len(palabra)<= 25):
            list_of_values[2] +=1
        elif(len(palabra)>25):
            list_of_values[3] +=1
    print("El texto posee", list_of_values[0], "faciles de leer", list_of_values[1], "aceptables para leer",list_of_values[2],"dificil de leer",list_of_values[2],"muy dificiles de leer")

def start():
    """Ejecuta el programa"""
    titulo()
  #  resumen()

start()