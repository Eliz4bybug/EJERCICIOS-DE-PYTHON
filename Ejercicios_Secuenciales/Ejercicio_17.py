import os
os.system ("Cls")

#Entrada
donación = float(input("Ingrese el monto de la donación: "))

#Proceso
monto_centroSalud = ((25*donación)/100)
monto_ComedorInfantil = ((35*donación))/100
monto_escuelaInfantil = ((25*donación))/100 
monto_asiloAncianos = ((15*donación))/100

#Salida
print(" =================== RESULTADOS =================== ")
print(f"25% Monto para el Centro de Salud: {monto_centroSalud: .2f} soles")
print(f"35% Monto para el Comedor Infantil: {monto_centroSalud: .2f} soles")
print(f"25% Monto para la Escuela Infantil: {monto_escuelaInfantil: .2f} soles")
print(f"Monto para el Asilo de Ancianos: {monto_asiloAncianos: .2f} soles")