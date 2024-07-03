usuario=input("escriba una palabra polindromo:")
palabra=usuario
palabra_2=""
contador=0
for i in palabra:
    palabra_2=i+palabra
    contador+=1
    if contador<=10:
        print(palabra_2)
        
print()

usuari_tex=input("¿desea 'codificar' o 'decodificar'?:")
abc="abdefghijklmnñopqrstuvxyz"
abc_total=""
if usuari_tex=='codificar':
    primo=[]
    contador=1
    while contador<=104:
        
        print()


tex=input("escriba una oración:")
    