print("Bienvenid@")
while True:
    nombre=input("Inserte su nombre (Mas de 3 letras): ")
    if len(nombre)>=3:
        break
    else:
        print("Ingrese nombre correcto")
while True:
    numtel=input("Ingrese su numero de contacto (8 a 9 numeros): ")
    if  len(numtel)>=8 and  len(numtel)<=9 and numtel.isdigit() :
        break
    else:
        print("Ingrese numero correcto")
horastot=input("Inserte cantidad de horas de uso de maquinaria: ")
horastot=int()
maquican=input("Cuantas maquinas planea usar?: ")
while True:
    loop=0
    maqval=0+maqval
    maqtot=0+maqtot
    maqval=int(maqtot)
    
    if maquican==loop :
        break
    loop=loop+1
    maq=input(f"Ingrese maquina {loop} A.-Excavadora B.-Grua C.- Mezcladora : ")
    horas=input("Ingrese cantidad de horas a usar: ")
    horas=int()

    if horastot<horas:
        print("Horas maximas alcanzadas")
    if maq=="A":
        maqtot=maqval+200000*horas
    elif maq=="B":
        maqtot=maqval+250000*horas
    elif maq=="C":
        maqtot=maqval+150000*horas
print(maqtot)    