#Para los números entre 10 y 500, expresar en un diccionario el número y su respectivo dígito más alto por el cuál es divisible.
#Por ejemplo para 328 es 8.
dicionario={x:int(max(list(str(x)))) for x in range(10,501) if x % int(max(list(str(x))))==0}
print(dicionario)