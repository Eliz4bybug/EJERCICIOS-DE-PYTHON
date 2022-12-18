import os
os.system("cls")

#Entrada

juanD = float(input("Ingrese la cantidad que aportará Juan en dólares: "))
rosaD = float(input("Ingrese la cantidad que aportará Rosa en dólares: "))
danielS = float(input("Ingrese la cantidad que aportará Daniel en Soles: "))

#Proceso

    #Convertir el dinero de daniel de soles a dólares

danielD = danielS / 3.00

    #Total en dólares

TotalD = juanD + rosaD + danielD

    # Hallando el porcentaje de Juan
PorcentajeJuan = (juanD * 100) / TotalD
    # Hallando el porcentaje de Rosa
PorcentajeRosa = (rosaD * 100) / TotalD
    # Hallando el porcentaje de Daniel
PorcentajeDaniel = (danielD * 100) / TotalD
    


#salida
print("    ===== RESULTADOS =========")
print(f"conversión de soles a dolares de Daniel {danielD:.2f}")
print ( f"Total de Aportes: {TotalD:.2f} ")
print( f"Parte de Juan :  {PorcentajeJuan:.2f}")
print( f"Parte de Rosa :  {PorcentajeRosa:.2f}")
print( f"Parte de Daniel :  {PorcentajeDaniel:.2f}")

