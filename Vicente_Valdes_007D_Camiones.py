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

horastot=int(input("Inserte cantidad de horas de uso de maquinaria: "))

maquican=input("Cuantas maquinas planea usar?: ")
loop=0
while True:
    
    maqtot=int()
    maqval=int(maqtot)
    
    if maquican==loop :
        break
    loop=loop+1
    while True:
        maq=input(f"Ingrese maquina {loop} A.-Excavadora B.-Grua C.- Mezcladora : ").upper()
        if maq=="A" or "B" or "C":
            break
        
        else :
            print("Error al seleccionar")

    
    horasc=int()
    horas=int(input("Ingrese cantidad de horas a usar: "))
    horasc=0+horas
    
    if horastot<=horasc:
        print("Horas maximas alcanzadas")
    if maq=="A":
        maqtot=maqval+200000*horas
    elif maq=="B":
        maqtot=maqval+250000*horas
    elif maq=="C":
        maqtot=maqval+150000*horas
print(maqtot)    
