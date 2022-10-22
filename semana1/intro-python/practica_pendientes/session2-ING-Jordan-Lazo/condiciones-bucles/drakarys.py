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
