
#ejercico 1
#misolucion
from numpy import number
from pyrsistent import inc


""" def revidar_ordenado(s)->bool:
    listanumeros=s.split()
    ultimo=listanumeros[len(listanumeros)-1]
    ordenado='cred'
    for i in listanumeros:
       
        if int(ultimo)<int(i):
          ordenado="decre"
    return ordenado=='cred'
    #return True  #si lo numeros estan ordenado de manera creciente
    #false
s='1 2 3 4 5 6 15 21' 
s1='21 15 6 5 4 3 2 1' 
print(revidar_ordenado(s1)) """
#solucion
""" s='1 2 3 4 5 6 15 21' 
s1='21 15 6 5 4 3 2 1' 
def increasingString(string:str)-> bool:
    numbers:list[int]=[int(number) for number in string.split()]
    for i in range(1,len(numbers)):
      if numbers[i-1]>numbers[i]:
         return False
       
    return True

print(increasingString(s)) """
#ejercicio 2
""" def mayusculas(funcion_param):
    def axu(nombre):
        r= funcion_param(nombre.upper())
        return r
        
    return axu
@mayusculas
def saludar(nombre):
    return f"Hola {nombre}"
  
print(saludar("Jorge")) #Hola Jorge (sin decorar)
#print(saludar("Jorge")) #Hola  JORGE """
#ejercicio 3
def bold(funcion_param):
    def axu (texto):
      string_aux=f"<b>{funcion_param(texto)}</b>"
      return string_aux

    return axu
def italitic(funcion_param):
    def axu (texto):
      string_aux=f"<i>{funcion_param(texto)}</i>"
      return string_aux
    return axu
  
  
def underline(funcion_param):
    def axu (texto):
      string_aux=f"<u>{funcion_param(texto)}</u>"
      return string_aux
    return axu

  
#deveria ir de abajo hacia arriba
@bold
@italitic
@underline
def  escribir(texto):
     return texto
   
print(escribir("piero"))