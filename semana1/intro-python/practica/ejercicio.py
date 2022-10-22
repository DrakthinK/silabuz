#icionario={x:str(x) for x in range(10,501) if x % int(max(list(str(x))))==0}
dicionario={x:int(max(list(str(x)))) for x in range(10,501) if x % int(max(list(str(x))))==0}
print(dicionario)