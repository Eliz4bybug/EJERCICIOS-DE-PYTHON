import os
os.system ("Cls")

#Entrada
sueldoBásico = 500
Monto_TotalVendido = float(input("Ingrese el monto total vendido: "))

#Proceso
comisión9 = (9*Monto_TotalVendido)/100
sueldoBruto = sueldoBásico + comisión9
Leydescuento11 = (11*sueldoBruto)/100
sueldoNeto = sueldoBruto - Leydescuento11

#SALIDA 
print( "========== RESULTADOS ============")
print(f"La comisión será: {comisión9: .2f} soles.")
print(f"Sueldo Bruto: {sueldoBruto: .2f} soles.")
print(f"Descuento : {Leydescuento11: .2f} soles.")
print(f"Sueldo Neto del vendedor será: {sueldoNeto: .2f} soles.")