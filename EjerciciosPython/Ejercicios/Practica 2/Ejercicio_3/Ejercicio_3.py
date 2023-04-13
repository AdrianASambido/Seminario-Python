# 3. Dado el siguiente texto guardado en la varible jupyter_info, solicite por teclado una letra
# e imprima las palabras que comienzan con dicha letra. En caso que no se haya ingresado un letra,
# indique el error. Ver: módulo string
import string
from typing import List

jupyter_info = """ JupyterLab is a web-based interactive development
environment for Jupyter notebooks,
code, and data. JupyterLab is flexible: configure and arrange the user
interface to support a wide range
of workflows in data science, scientific computing, and machine learning.
JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing
ones.
"""
# creo una lista con el texto
lista = jupyter_info.split()
letra = input("ingrese una letra")
if letra in string.ascii_letters:
    for elem in lista:
        if (elem.startswith(letra)):
            print(elem)
else:
    print("El caracter ingresado no es una letra ")