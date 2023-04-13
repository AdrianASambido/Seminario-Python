#1. Tomando el texto del README.md de numpy, copiar y pegar el texto en una variable, 
#   luego imprima todas las líneas que contienen 'http' o 'https'.

import collections
texto = """ Website: https://www.numpy.org
Documentation: https://numpy.org/doc
Mailing list: https://mail.python.org/mailman/listinfo/numpy-discussion

Source code: https://github.com/numpy/numpy
Contributing: https://www.numpy.org/devdocs/dev/index.html
Bug reports: https://github.com/numpy/numpy/issues
Report a security vulnerability: https://tidelift.com/docs/security)
It provides:

a powerful N-dimensional array object
sophisticated (broadcasting) functions
tools for integrating C/C++ and Fortran code
useful linear algebra, Fourier transform, and random number capabilities
Testing:

NumPy requires pytest and hypothesis. Tests can then be run after installation with:
repito repito repito

"""

caracter = "http"
lista = texto.lower().split("\n")
for elem in lista:
    if caracter in elem:
        print(elem)