print("Hola, bienvenid@")
while True:
    nombre=input("Como te llamas?: ")
    if len(nombre)>3:
        break
    else :
        print ("Nombre debe ser más largo")
while True:
    precios=(input("Inserte valor de su producto: "))
   
    if precios.isdigit() :
        precio=int(precios)
        if(precio)>=0 :
            
            break
    else :
        print("Ingresa un monto mayor a 0 o ingrese cifra correcta")
if precio<10000:
    descuento=precio*0
elif precio>=10000 or precio<=50000:
    descuento=precio*0.10
elif precio>50000:
    descuento=precio*0.20

total=precio-descuento

print(f"Hola! {nombre}, tu total es: ${total}, ahorraste ${descuento}")
