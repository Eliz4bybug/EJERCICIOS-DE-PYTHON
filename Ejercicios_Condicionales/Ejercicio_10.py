'''Un curso se evalúa sobre la base de 5 notas de las cuales se elimina las notas de mayor y menor
puntaje. Desarrolle el programa que muestre las notas eliminadas y el promedio aprobatorio.'''
import os
os.system ("cls") 

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))
n5 = float(input("Nota 5: "))

#Eliminar menor nota
if n1 != n2 != n3 != n4 != n5:
    if n1>n2 and n1>n3 and n1>n4 and n1>n5 : 
        print ("Se elimina la siguiente nota mayor: ", n1)
        if n2<n3 and n2<n4 and n2<n5 : 
            print("Se elimina la siguiente nota menor: ",n2)
            promedio = (n3+n4+n5)/3
            print("Promedio: ", promedio)
        if n3<n2 and n3<n4 and n3<n5 : 
            print("Se elimina la siguiente nota menor: ",n3)
            promedio = (n2+n4+n5)/3
            print("Promedio: ", promedio)
        if n4<n2 and n4<n3 and n4<n5 : 
            print("Se elimina la siguiente nota menor: ",n4)
            promedio = (n2+n3+n5)/3
            print("Promedio: ", promedio)
        else: 
            print("Se elimina la nota menor: ",n5)
            promedio = (n2+n3+n4)/3
            print("Promedio: ", promedio)
    elif n2>n1 and n2>n3 and n2>n4 and n2>n5 : 
        print ("Se elimina la siguiente nota Mayor:", n2)
        if n1<n3 and n1<n4 and n1<n5 : 
            print("Se elimina la siguiente nota menor: ",n1)
            promedio = (n3+n4+n5)/3
            print("Promedio: ", promedio)
        if n3<n2 and n3<n4 and n3<n5 : 
            print("Se elimina la siguiente nota menor: ",n3)
            promedio = (n1+n4+n5)/3
            print("Promedio: ", promedio)
        if n4<n1 and n4<n3 and n4<n5 : 
           print("Se elimina la siguiente nota menor: ",n4)
           promedio = (n1+n3+n5)/3
           print("Promedio: ", promedio)
        else: 
            print("Se elimina la nota menor: ",n5)
            promedio = (n1+n3+n4)/3
            print("Promedio: ", promedio)
    elif n3>n1 and n3>n2 and n3>n4 and n3>n5 : 
        print ("Se elimina la siguiente nota:", n3)
        if n1<n2 and n1<n4 and n1<n5 : 
            print("Se elimina la siguiente nota menor: ",n1)
            promedio = (n2+n4+n5)/3
            print("Promedio: ", promedio)
        if n2<n1 and n2<n4 and n2<n5 : 
            print("Se elimina la siguiente nota menor: ",n2)
            promedio = (n1+n4+n5)/3
            print("Promedio: ", promedio)
        if n4<n1 and n4<n2 and n4<n5 : 
           print("Se elimina la siguiente nota menor: ",n4)
           promedio = (n1+n2+n5)/3
           print("Promedio: ", promedio)
        else: 
            print("Se elimina la nota menor: ",n5)
            promedio = (n1+n2+n4)/3
            print("Promedio: ", promedio)
    elif n4>n1 and n4>n2 and n4>n3 and n4>n5 : 
        print ("Se elimina la siguiente nota:", n4)
        if n1<n2 and n1<n3 and n1<n5 : 
            print("Se elimina la siguiente nota menor: ",n1)
            promedio = (n2+n3+n5)/3
            print("Promedio: ", promedio)
        if n2<n1 and n2<n3 and n2<n5 : 
            print("Se elimina la siguiente nota menor: ",n2)
            promedio = (n1+n3+n5)/3
            print("Promedio: ", promedio)
        if n3<n1 and n3<n2 and n3<n5 : 
           print("Se elimina la siguiente nota menor: ",n3)
           promedio = (n1+n2+n5)/3
           print("Promedio: ", promedio)
        else: 
            print("Se elimina la nota menor: ",n5)
            promedio = (n1+n2+n3)/3
            print("Promedio: ", promedio)
    else:  
        print ("Se elimina la siguiente nota Mayor:", n5)
        if n1<n2 and n1<n3 and n1<n4 : 
            print("Se elimina la siguiente nota menor: ",n1)
            promedio = (n2+n3+n4)/3
            print("Promedio: ", promedio)
        if n2<n1 and n2<n3 and n2<n4 : 
            print("Se elimina la siguiente nota menor: ",n2)
            promedio = (n1+n3+n4)/3
            print("Promedio: ", promedio)
        if n3<n1 and n3<n2 and n3<n4 : 
           print("Se elimina la siguiente nota menor: ",n3)
           promedio = (n1+n2+n4)/3
           print("Promedio: ", promedio)
        elif n4<n1 and n4<n2 and n4<n3 :
            print("Se elimina la nota menor: ",n4)
            promedio = (n1+n2+n3)/3
            print("Promedio: ", promedio)
else:
    print("Ingrese notas diferentes") 


