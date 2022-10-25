""" def funcion_decoradora(function_parametro):
    def function_interna(numbers):
      print("incio del calculo del promedio de la lista")
      print(function_parametro(numbers))
      print("el calculo ha finalizado")
    return function_interna
  
  
def get_avg(number:list) -> float:
  return sum(number)/len(number) """
  
  

#Escriba un programa que dada una entrada numérica por el usuario, ingrese a una función que duplique el valor y sea retornado en forma de string o cadena. #Utilice tipos tanto para las variables como para las funciones.
""" def funcion_duplicadora()->str:
    numero: float=float(input("entrada en numero:"))
    return str(2*numero)
print(funcion_duplicadora()) """

#problema3
""" def funcion_duplicarletras()->list:
    palabra: str = input("Ingrese una palabra: ")
    palabra_duplicada: str = palabra * 2
    
    lista='holahola'

    res=[]
    cont=0
    for p in palabra_duplicada:
      if cont>=len(palabra):
        res.insert(res.index(p),p)
      else:
        res.append(p)
      cont+=1
    return res
print(funcion_duplicarletras()) """
#problema5

""" def deco1(funcionparametro)->None:
  
  def funcion_interna(n):
    print("Hola,estoy decorando esta funcion")
    funcionparametro(n)
    print("Termine de decorar")
  return funcion_interna

@deco1
def mostrar(n):
  print("ingresantes el numero",n)
  
mostrar(30) """