#Crear menú con 3 opciones con 1. Números 2. Personas, 3. Finalizar

import os
def Numeros():
    #Ingresar n números donde n es un número ingresado por el usuario.
    #Mostrar la cantidad de números positivos, cantidad de números negativos y cantidad de númeross iguales a cero
    n=int(input("Ingrese cuantos números necesita: "))
    a=0
    b=0
    c=0
    d=0
    for i in range(n):
        a=int(input("ingrese un número: "))
        if(a>0):
       	    b=b+1
        elif(a==0):
       	    c=c+1
        elif(a<0):
            d=d+1
        
    print("Positivos: "+ str(b)+ " Negativos: "+ str(d)+ " Cero: "+ str(c))

    pausa=input("Presione una tecla para continuar..")

def Personas():
    #Ingresar nombre y edad para n Personas .N es un número ingresado por teclado.
    #Mostrar: Promoedio de todas las edad ingresadas
    veces=int(input("¿Cuantos personas ingresa?: "))
    edad=0
    sum=0
    for i in range(veces):
        nombre = input("Ingrese Nombre de la Persona: ")
        edad = int(input("Ingrese Edad de la Persona: "))
        sum=sum+edad

    print("Promedio: " + str(sum/veces))

    pausa=input("Presione una tecla para continuar...")

seguir=True
while(seguir):
    os.system('cls')
    print(" ---- Menú Principal ---- ")
    print("1. Números")
    print("2. Personas")
    print("3. Finalizar")
    op=int(input("Digite opción 1,2,3: "))
    if(op==1):
        Numeros()   #invocamos a un def
    if(op==2):
        Personas()  #invocamos a un def
    if(op==3):
        print("¡Programa Finalizado!")
        seguir=False
        break