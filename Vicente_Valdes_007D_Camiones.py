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

while True:
    horastot=input("Inserte cantidad de horas de uso de maquinaria: ")
    if horastot.isdigit():
        horastot=int(horastot)
        break
    else:
        print("Insertar numero correcto")
while True:
    maquican=input("Cuantas maquinas planea usar?: ")
    if maquican.isdigit():
        maquican=int(maquican)
        break
    else:
        print("No es un numero!!!!")
loop=0
maqval1=0
maqval2=0
maqval3=0
maqtot=int(0)
horasc=int()
while loop<maquican:
    
   
    maqval=int(maqtot)
    
    if maquican==loop :
        break
    loop=loop+1
    while True:
        maq=input(f"Ingrese maquina {loop} A.-Excavadora B.-Grua C.- Mezcladora : ").upper()
        if maq=="A" or maq=="B" or maq=="C":
            break
        
        else :
            print("Error al seleccionar")

    
    while True:
        horas=input("Ingrese cantidad de horas a usar: ")
        if horas.isdigit():
            horas=int(horas)
            break
        else:
            print("Insertar hora adecuada")
        
    horasc=0+horas
    
    if horastot<=horasc:
        print("Horas maximas alcanzadas")
    if maq=="A":
        maqval1=200000*horas
    elif maq=="B":
        maqval2=250000*horas
    elif maq=="C":
        maqval3=150000*horas
maqtot=0+maqval1+maqval2+maqval3
print(maqtot)    
