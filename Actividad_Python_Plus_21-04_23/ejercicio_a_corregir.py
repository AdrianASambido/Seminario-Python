#EJERCICIO 10: dado el archivo denominado log_catedras que contiene el registro de accesos al entorno 
#  catedras.linti, se desea:
#Generar una función que retorne la actividad de un usuario dado como parámetro. Esta función recibe
#un parámetro opcional que indica: "TODO" para retornar la información completa, "EXPLICACION", 
#solo los accesos relacionados a las explicaciones de práctica (chequear si en la columna 
#"Contexto del evento" aparece el texto "BigBlueButton: Sala de VC de explicaciones de práctica"),
#"TEORIA", solo los accesos relacionados al material de clases la teoría (chequear si en la columna
#"Contexto del evento" aparece el texto "Página: Material de las clases"). Por defecto la función 
#retorna toda la información.
#Escribir un programa que, utilizando la función anterior, muestre un listado similar al siguiente, 
#donde sólo se muestra la información sobre fecha y hora de acceso, recurso accedido y dirección IP. 
#Notar que la columna "Recurso accedido" no muestra todo el texto sino los primeros caracteres de modo
#que quede prolijo el listado.
#Usuario: Hypno
#------------------------------------------------
#Dia/hora             Recurso accedido     Dir IP
#------------------------------------------------
#3/04/23, 09:22:22    BigBlueButton: Sala  190.19.24.34
#3/04/23, 19:22:22    Tarea: Entrega 2     190.19.24.34
            
#Actividad_Python_Plus_21-04_23\
import csv
import os

ruta = os.path.abspath("")
ruta_completa = os.path.join(ruta, "Actividad_Python_Plus_21-04_23\log_catedras.csv")# "log_catedras.csv")

archivo = open(ruta_completa, "r")# ABRE EL ARCHIVO EN MODO LECTURA
csvreader = csv.reader(archivo, delimiter = ",")# LO DELIMITA CON COMAS

def actividad(usuario, info = "TODO"):
    listaActividad = []
    
    encabezado = next(csvreader)# SACA EL ENCABEZADO
    
    match info:
        case "TODO":
            for linea in csvreader:                
                if linea[1] == usuario:                    
                    listaActividad.append(linea)
            
        case "EXPLICACION":
            for linea in csvreader:
                if linea[3] == "BigBlueButton: Sala de VC de explicaciones de práctica":                                
                    listaActividad.append(linea)
            
        case "TEORIA":
            for linea in csvreader:
                if linea[3] == "Página: Material de las clases":
                    listaActividad.append(linea)
    
    archivo.close()
    
    return listaActividad

nombre = str(input("Ingrese el nombre de usuario para ver su actividad: "))
tipoInfo = str(input("Ingrese:\n 'TODO' para la informacion completa del usuario.\n 'EXPLICACION' para accesos a explicaciones de practica.\n 'TEORIA' para accesos relacionados al material de teoria.\n"))
listaAct = actividad(nombre, tipoInfo)

print(f"Usuario: {nombre}")
print("-" * 48)
print("Dia/hora", "" * 11, "Recurso accedido", "" * 3, "Dir IP")
print("-" * 48)
for linea in listaAct:
    print(f"{linea[0]}  {linea[3]}   {linea[6]}")# FALTA LINEA 1 {linea[1]}   