import os
os.system ("cls") 

print(" ==================== CODIGOS DE CADA TIPO DE PRODUCTO: ======================== ")
print("   - Cóigo 101")
print("   - Cóigo 102")
print("   - Cóigo 103")
print("   - Cóigo 104")

tipoProducto = float(input("Ingrese el código del producto que desea comprar: "))
if tipoProducto == 101 :
    nUnidades = float(input("Ingrese la cantidad de unidades que desea comprar: "))
    importedCompra = 17 * nUnidades
    if nUnidades >= 1 and nUnidades<= 10:
       descuento = (5*importedCompra)/100
       importePagar = importedCompra - descuento
       print(f"Importe de compra: {importedCompra: .2f}")
       print(f"Descuento: {descuento: .2f}")
       print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 11 and nUnidades <= 20:
        descuento = (8*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 21 and nUnidades <= 30:
        descuento = (10*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 31:
        descuento = (13*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")

if tipoProducto == 102 :
    nUnidades = float(input("Ingrese la cantidad de unidades a comprar: "))
    importedCompra = 25 * nUnidades
    if nUnidades >= 1 and nUnidades<= 10:
       descuento = (5*importedCompra)/100
       importePagar = importedCompra - descuento
       print(f"Importe de compra: {importedCompra: .2f}")
       print(f"Descuento: {descuento: .2f}")
       print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 11 and nUnidades <= 20:
        descuento = (8*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 21 and nUnidades <= 30:
        descuento = (10*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 31:
        descuento = (13*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")

if tipoProducto == 103 :
    nUnidades = float(input("Ingrese la cantidad de unidades a comprar: "))
    importedCompra = 16 * nUnidades
    if nUnidades >= 1 and nUnidades<= 10:
       descuento = (5*importedCompra)/100
       importePagar = importedCompra - descuento
       print(f"Importe de compra: {importedCompra: .2f}")
       print(f"Descuento: {descuento: .2f}")
       print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 11 and nUnidades <= 20:
        descuento = (8*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 21 and nUnidades <= 30:
        descuento = (10*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 31:
        descuento = (13*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")

if tipoProducto == 104 :
    nUnidades = float(input("Ingrese la cantidad de unidades a comprar: "))
    importedCompra = 27 * nUnidades
    if nUnidades >= 1 and nUnidades<= 10:
       descuento = (5*importedCompra)/100
       importePagar = importedCompra - descuento
       print(f"Importe de compra: {importedCompra: .2f}")
       print(f"Descuento: {descuento: .2f}")
       print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 11 and nUnidades <= 20:
        descuento = (8*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 21 and nUnidades <= 30:
        descuento = (10*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 31:
        descuento = (13*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")

elif tipoProducto != 101 and tipoProducto != 102 and tipoProducto != 103 and tipoProducto != 104:
    print(" Ingrese un código que sea válido")
    

