#ingresar dos numeros, mostrar la suma y la multiplicacion de ambos

a=int(input("Digite un número: "))
b=int(input("Digite otro número: "))
suma=a+b
multi=a*b
print("La suma de de "+ str(a)+ "y de "+ str(b) + " Es igual a: " + str(suma))
print("La multiplicacion de " + str(a) + " y de " + str(b) + " Es igual a: " +str(multi))

#estructura if

if(a>b):
    print("El número " + str(a)+ " Es mayor que: " + str(b))
elif (a<b):
    print("El número " + str(b)+ " Es mayor que: " + str(a))
else:
    print("Los números son iguales!")