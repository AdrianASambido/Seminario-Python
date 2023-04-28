import pandas as pd

def obtener_actividad(usuario, info="TODO"):
    
    df = pd.read_csv("Actividad_Python_plus_21-04_23\log_catedras.csv")
    df = df[df['Usuario afectado'] == usuario]

    if info == "EXPLICACION":
        df = df[df['Contexto del evento'].str.contains('BigBlueButton: Sala de VC de explicaciones de práctica')]
    elif info == "TEORIA":
        df = df[df['Contexto del evento'].str.contains('Página: Material de las clases')]

    return df

nombre = str(input("Ingrese el nombre de usuario para ver su actividad: "))
tipoInfo = str(input("Ingrese:\n 'TODO' para la informacion completa del usuario.\n 'EXPLICACION' para accesos a explicaciones de practica.\n 'TEORIA' para accesos relacionados al material de teoria.\n"))
listaAct = obtener_actividad(nombre, tipoInfo)

print(f"Usuario: {nombre}")
print("-" * 48)
print("Dia/hora", "" * 11, "Recurso accedido", "" * 3, "Dir IP")
print("-" * 48)
for indice, fila in listaAct.iterrows():
        print(f"{fila[0]} {fila[1]} {fila[6]}") 