numero= int(input("introduzca un numero:"))

if numero%2==0 and numero%3==0:
    print("el numero es divisible por 6")
    
elif numero>100:
    print("el numero es mayor que 100")
elif numero%2==0:
    print("el numero es divisible por 2")
elif numero%3==0: 
    print("el numero es divible por 3") 
elif numero<0:
    print("el numero es negativo")

else: 
    print("no cumple ninguna condicion")
    