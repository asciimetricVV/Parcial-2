from random import randint

num1=int(input("ingresa limite inferior "))
num2=int(input("ingresa limite superior "))

while num1>=num2:
    print("error, limite inferior debe ser menor a superior")

    num1=int(input("ingresa limite inferior"))
    num2=int(input("ingresa limite superior"))

numero=1
numero1=2
numero2=3

while True:
    print("_______________________")
    numero=0
    numero1=0
    numero2=0
    numero=randint(num1,num2)
    numero1=randint(num1,num2)
    numero2=randint(num1,num2)
   
    print(numero,numero1,numero2)
    
    print("_______________________")
    if numero==numero1==numero2:
        print("GANASTE!!!!!!!!!!!!!!!!!")
        break
    sn=input("Desea continuar? S/N: ").upper()
    if sn=="N":
        print("Saliendo...")
        break