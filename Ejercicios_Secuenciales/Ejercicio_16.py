''' El cálculo del pago mensual de un empleado de una empresa se efectúa de la siguiente manera:
el sueldo básico se calcula sobre la base del número total de horas trabajadas basado 
en una
tarifa horaria, al sueldo básico, se le aplica una bonificación del 
20% obteniéndose el sueldo
bruto; al sueldo bruto, se le aplica un descuento del 10% obteniéndose 
el sueldo neto. Desarrolle
el programa que muestre el sueldo básico, bruto y neto de un trabajador '''
import os 
os.system ("cls")

 #Entrada 
nhoras_trabajadas = float(input("Ingrese la cantidad de horas trabajadas: "))
print("Se pagará 10 soles por cada hora trabajada")
    #Proceso
sueldoBasico = nhoras_trabajadas * 10
# sueldo Bruto será un aumento del 20 % a el sueldoBasico
sueldoBruto = ((20*sueldoBasico)/100) + sueldoBasico
# sueldoBruto descuento del 10% 
sueldoNeto = sueldoBruto - ((10*sueldoBruto)/100) 

#Salida
print(" ===================== Resultados =================")
print(f"Sueldo Básico: {sueldoBasico: .2f} soles. ")
print(f"Sueldo Bruto: {sueldoBruto: .2f} soles. ")
print(f"Sueldo Neto: {sueldoNeto: .2f} soles.")
