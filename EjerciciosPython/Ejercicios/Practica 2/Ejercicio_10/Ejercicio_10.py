""" 10. Dada una lista de nombres de estudiantes y dos listas con sus notas en un curso, escriba un
        programa que manipule dichas estructuras de datos para poder resolver los siguientes puntos:
        A. Generar una estructura con todas las notas relacionando el nombre del estudiante con las
           notas. Utilizar esta estructura para la resolución de los siguientes items.
        B. Calcular el promedio de notas de cada estudiante.
        C. Calcular el promedio general del curso.
        D. Identificar al estudiante con la nota promedio más alta.
        E. Identificar al estudiante con la nota más baja.
Nota:
• Las 3 estructuras están ordenadas de forma que los elementos en la misma posición corresponden
a un mismo alumno.
• Realizar funciones con cada item """

nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás',  'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 
           85, 73, 37, 42, 95, 18, 7,     74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

def listar (nombres): # Item "A"
    ''' Tomamos las tres listas: 'nombres, notas_1, notas_2' y creamos un 
        diccionario con (clave=nommbre, y valor [nota_1, nota_2])  '''
    lista = nombres.replace("'","").replace(" ","").replace("\n","").split(",")
    '''con el for itero en las tres listas, y con zip tomo el primer valor de cada una y creo clave, valor '''
    alumnos = {name:[note1,note2] for name, note1,note2 in zip(lista,notas_1,notas_2)}
    return alumnos

def promedio_notas(alumnos): # Item "B"
    '''sacamos el promedio por alumno'''
    promedio_alumnos = {}
    for name in alumnos.keys():
        promedio = sum(alumnos[name])/len(alumnos[name])
        promedio_alumnos[name]= promedio
    return promedio_alumnos

def promedio_general(promedio_alumnos): # Item "C"
    '''sacamos promedio general de los alumnos'''
    promedio_total = sum(promedio_alumnos.values())/len(promedio_alumnos)
    return promedio_total

def promedio_maximo(promedio_alumnos): # Item D
    '''sacamos el alumno de promedio maximo '''
    promedio_alumno_ordenado = sorted(promedio_alumnos.items(), key=lambda x: x[1])
    mayor_promedio = promedio_alumno_ordenado[-1][0]
    return mayor_promedio

def menor_nota(alumnos):
    """ calculamos el alumno de menor nota """
    nota_minima = int(110)
    nombre = None
    for nombre,notes in alumnos.items():
        #Buscamos el mínimo entre ambas notas
        minimo = min(notes)
        if minimo < nota_minima:
            nombre_del_estudiante = nombre
            nota_minima = minimo
    print(f'El alumno {nombre_del_estudiante}, tiene la nota mínima = {nota_minima}')

def main():
    alumnos = listar(nombres)
    print(alumnos) # alumnos con sus respectivas notas "A"
    pro_de_notas = promedio_notas(alumnos)
    print(pro_de_notas) # listado con el promedio de cada alumno "B" 
    pro_gral = promedio_general(pro_de_notas)
    print(pro_gral) #promedio general del curso "C"
    alu_mayor_promedio = promedio_maximo(pro_de_notas)
    print('el alumno con mayor promedio es: ' , alu_mayor_promedio) # alumno de mayor promedio "D"
    menor_nota(alumnos) # estudiante con la nota más baja "E"

main()