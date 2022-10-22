
#ejercicio 
""" lista=["Hola","Amigos","Hoy","True"]
palabra=input("ingrese la palabra :")
lista.append(palabra)
lista.insert(0,palabra)
print(lista) """
#ejercicio
""" lista_numeros=[15,20,50,80,40,60]
dato=int(input("ingrese dato:"))
lista_numeros.remove(dato)
print(lista_numeros) """
""" elemento_usuario=int(input("ingrese elemento:")) """
#ejercicio
""" tupla_numeros=(1,3,5,2,7,5,5,8,4,8,4,8,4)
print("SALIDA :",tupla_numeros.count(int(input("ingrese elemento:"))),"veces") """
#ejercicio
""" print(dicionario_talla_personas[nombre]) """
#ejercicio
""" dicionario_talla_personas= {'Marcelo':1.80,'Jose':1.50,'Oscar':1.70,'Jorge':1.40}
nombre=input("ingrese nombre:")
print(dicionario_talla_personas[nombre] if nombre in list(dicionario_talla_personas.keys()) else "nombre no encotrado") """
#ejercicio
""" talla_personas= {'Marcelo':1.80,'Jose':1.50,'Oscar':1.70,'Jorge':1.40}
talla=float(input("ingrese talla:"))
lista_key = list(talla_personas.keys())
lista_value = list(talla_personas.values())
posicion = lista_value.index(talla)
print(lista_key[posicion]) """
#ejercicio
""" 
nombre=input("mi nombre es :")
apellido=input("mi apellido es:")
edad=input("mi edad es:")
diccionario_persona={
  "nombre":nombre,
  "apellido":apellido,
  "edad":edad
}
print(f'Hola mi nombres es [{diccionario_persona["nombre"]}] [{diccionario_persona["apellido"]}] y tengo [{diccionario_persona["edad"]}] años') """
#ejercicio
""" candidato=input("Candidato Elegido:")
respueta="opcion erronea"
if candidato.upper() in["A","B"]:
    respueta="Usted a votado por el partido rojo"
elif candidato.upper() =="c":
    respueta="Usted ha votado por el partido verde"
print(respueta) """
#ejercicio
""" for i in range(10,51):
  if i%2==0:
    print(i)
  else:
    print(i) """
#ejercicio
""" tabla_numero=input("ingrese la tabla a mostrar")
for i in range(1,13):
  print(f" {tabla_numero} x {i}={(tabla_numero*i)}");
   """
#ejercicio
""" sumapositivos=[]
sumanegativos=[]
cantidad=0

while True:
    numero=int(input("ingrese numero:"))
    if numero>0:
      sumapositivos.append(numero)
    else:
      sumanegativos.append(numero)
    cantidad+=1
    if numero==0:
      print(f"suma positivos {sum(sumapositivos)} \n suma negativos:{sum(sumanegativos)}, cantidad {cantidad}")
      break """
#ejercicio
    