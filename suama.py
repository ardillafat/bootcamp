#suma con valores constantes
a = 5 
b = 10 
suma = a+b 
print("La suma es",suma)

#suma con valores dinamicos 
a = int(input("ingrese un numero"))
b = int(input("ingrese el numero de B"))
suma = a + b
print (suma)

#en una sola linea 
print(int(input("ingrese A"))+ int(input("ingrese B")))

#como funcion
def suma(a,b):
    return a+b

#las mas usadas en e, a,bito profecional
#consunmiedno la funcion con constantes
s = suma(2,4)
print (s)

#consumiendo la funcion del mismo nombre
a = int(input("ingrese A:"))
b = int(input("ingrese B:"))
s = suma(a,b)
print(s)
