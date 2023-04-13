from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-","/","*"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
intentos_InCorrectos = 0
intentos_Correctos = 5
for i in range(0, times):
# Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    if(operator == "/")and(number_2 == 0):
        print("No se puede dividir por cero")
        number_2 = randrange(1,10)
        operator = choice(operators)
    match operator:
        case "+":
            operation = number_1 + number_2
        case "-":
            operation = number_1 - number_2
        case "*":
            operation = number_1 * number_2
        case "/":
            operation = number_1 / number_2
    # Se imprime la cuenta.
    print(f"{i+1}-¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    result = float(input("resultado: "))
    if(result != operation):
        intentos_InCorrectos += 1
        print("Resultado incorrecto")
    else:
        print("Resultado correcto")
    # Al terminar toda la cantidad de cuentas por resolver.
    # Se vuelve a tomar la fecha y la hora.
    end_time = datetime.now()
    # Restando las fechas obtenemos el tiempo transcurrido.
    total_time = end_time - init_time
    # Mostramos ese tiempo en segundos.
    print(f"\n Tardaste {total_time.seconds} segundos.")
print(f"\n Intentos fallidos {intentos_InCorrectos}")
intentos_Correctos = intentos_Correctos - intentos_InCorrectos
print(f"\n Intentos validos {intentos_Correctos}")

#SAMBIDO ADRIAN
