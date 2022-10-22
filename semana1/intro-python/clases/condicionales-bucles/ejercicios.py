""" ejercicio3 """
""" monto_salario= float(input("ingrese el monto"))
anio_servicio=int(input("ingrese años de servicio"))
total=monto_salario
if(anio_servicio>3):
  total=monto_salario+(5*monto_salario)/100
print(total) """
""" personas=1
edades=[]
while personas<=3:
  edad=int(input("ingrese su edad :"))
  edades.append(edad)
  personas+=1
print("El mayor es:",max(edades)) """

""" primerlado=int(input("ingrese el primer lado"))
segundolado=int(input("ingrese el segundo lado"))
tercerlado=int(input("ingrese el tercer lado"))

if primerlado==segundolado==tercerlado:
  print("el triangulo es equilatero")
elif primerlado==segundolado or segundolado==tercerlado or primerlado==tercerlado:
    print('el triangulo es isoseles')
else:
   print("triangulo es escaleno") """


""" tabla_numero=int(input("ingrese la tabla a mostrar :"))
for i in range(1,101):
  print(f" {tabla_numero} x {i}={(tabla_numero*i)}"); """

""" fibLista = [0, 1]
cont=3
while True:
    valor = fibLista[cont - 2] + fibLista[cont - 3]
    fibLista.append(valor)
    cont = cont + 1
    if cont==100:
      print("fibonacci")
      for i in fibLista:
        if i<100:
          print(i)
      break """
""" cadenauno=input("primera cadena :")
cadenados=input("segunda cadena :")
nuevacadenauno=""
nuevacadenados=""

for i in cadenauno:
  if i in['a','e','i','o','u']:
    continue
  nuevacadenauno+=i

for i in cadenados:
  if i in['a','e','i','o','u']:
    continue
  nuevacadenados+=i
  
print(f"{nuevacadenauno}  {nuevacadenados} ") """

""" lista=[500,100,200,300,200,100,600,400,800,400,500,900]
L=[]
for i in lista:
  if i not in lista:
    L.append(i)
print(L) """
""" sexo=input("sexo:S/M")
anio_experiencia=int(input("años de experiencia:"))
if anio_experiencia>10:
  print("ustede tiene un descuento del 5%")

if anio_experiencia>20:
  print("ustede tiene un descuento del 17%")

if anio_experiencia>25 and sexo.upper()=='F':
  print("ustede tiene un descuento del 17%")
   """
""" PENDIENTE 291001"""
esta_corriendo = False 
esta_bloqueando = True
esta_saltando = True

""" if not esta_corriendo:
    if not esta_bloqueando:
        if not esta_saltando:
            print("Drakarys")
        else:
            print("No puedo atacar mientras salto")
    else:
        print("No puedo atacar mientras bloqueo")
else:
    print("No puedo atacar mientras corro") """
    
""" imprimir= "Drakarys" if not esta_saltando else "No puedo atacar mientras salto" if not esta_bloqueando else "no puedo atacar mientras boqueo "  if not esta_corriendo else "No puedo atacar mientras corro"
print(imprimir) """
if esta_corriendo:
    print("No puedo atacar mientras corro")
elif esta_bloqueando:
    print("No puedo atacar mientras bloqueo")
elif esta_saltando:
    print("No puedo atacar mientras salto")
else: 
    print("Drakarys")
