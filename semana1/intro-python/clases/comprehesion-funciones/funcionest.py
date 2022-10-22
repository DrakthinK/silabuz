#ejercicio
""" cadena="sin nombre "

num= [i for i in cadena if i==' ']
print(len(num)) """
#ejercicio
""" lista1=[1,3,4,5]
lista2=[2,3,5,6]
numeros_comunes=[i for i in lista1 if i in lista2]
print(numeros_comunes) """
#ejercicio
""" numeros=[i for i in range(7,538) if i%10==7]
print(numeros) """
#ejercicio
""" ejercico 4 pendiente """
#ejercicio
""" M=[[1,2,3],[2,4,5],[1,1,1]]
def extra_column_n(M,n):
  if n<len(M):
   return M[n]
  else:
   return[]

print(extra_column_n(M,5)) """
#ejercicio
""" cadena="abbbccda"
subcadena="bbc"
def encontrar_2(cadena,subcadena):
  con=0
  for l in cadena:
     if con <=len(cadena) - len(subcadena):
        if cadena[con:con+len(subcadena)]==subcadena:
            return con
     con+=1  
  return -1
cadena="abbbccda"
subcadena="bbc"
print(encontrar_2(cadena,subcadena)) """
#ejercicio
""" 
matrix=[[1,2,3],[4,5],[6,7,8,9]]
def imprime_lista_anidada_1(matrix):
    for row in matrix:
          for c in row:
            print(c,end="\t")
          print(end="\n")
imprime_lista_anidada_1(matrix) """