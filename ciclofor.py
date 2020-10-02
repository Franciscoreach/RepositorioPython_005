#Crear ciclo for que permita ingresar para n números, donde n es un número ingresado por teclado.
#Calcular y mostrar: cantidad de números pares y cantidad de números impares.

veces=int(input("¿Cuantos números ingresa?: "))
par=0
impar=0
for x in range(veces):
    num=int(input("Ingrese un número: "))
    if(num%2==0):
        par=par+1
    elif(num%2==1):
        impar=impar+1

print("La cantidad de números pares es " + str(par))
print("La cantidad de números impares es " + str(impar))
