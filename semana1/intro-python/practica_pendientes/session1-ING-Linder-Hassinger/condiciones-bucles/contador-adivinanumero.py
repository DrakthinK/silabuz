#ejercicio
import random
numeroRandon= random.randint(0,1001)
print(f"numeroRandon {numeroRandon}")
cont=0
while True:
  cont+=1
  numero=int(input("ingrese un numero: "))
  if numero> numeroRandon:
      print("El numero es mayor")
  elif numero< numeroRandon:
      print("El numero es menor")
  else:
      print(f"Felicidades adivinastes el numero {numero} con {cont} intentos")
      break