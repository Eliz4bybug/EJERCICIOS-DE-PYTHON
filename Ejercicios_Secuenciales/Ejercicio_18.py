import os
os.system ("Cls")

nUnidades = float(input("Ingrese la cantidad de articulos que desea comprar: "))
precioU = float(input("Ingrese el precio por unidad del artículo: "))

#Proceso
importe = nUnidades * precioU
descuento1 = (15* importe)/100
descuento2 = ((15*importe)/100) + descuento1 
importePagar =  importe - descuento2 

'''importe = nUnidades * precioU
descuento1 = (15* importe)/100
descuento2 = importe - descuento1 - ((15*importe)/100)
importePagar = descuento2 '''

#Salida
print(" ==================== RESULTADOS ===================")
print(f"Importe de la compra: {importe: .2f} soles")
print(f"Descuento: {descuento2: .2f} soles")
print(f"Importe a pagar: {importePagar: .2f} soles")