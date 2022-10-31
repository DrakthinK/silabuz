""" Cree la clase Circulo la cual herede de la clase Figura, adicione los siguientes atributos:

Radio
Centro X
Centro Y
Nota: Con centro "X" y "Y", agregue una composición con la clase Punto.

Cree el método mostrar_circulo, el cual haga uso de mostrar_figura, además agregue las siguientes impresiones:

El círculo tiene un radio de "Radio"
Centro:
El punto de inicio esta en ( "Centro X", "Centro Y" )
Nota:

Para el centro utilice mostrar_punto
Utilice los mismo datos del ejecicio 3 y adicione lo siguiente.
Radio = 3
Centro X = 2
Centro Y = 3
Cree un objeto circulo, llame a mostrar_circulo y luego elimine el objeto """
class Figura:
  def __ini__(self):
    pass
  
  
class Punto:
  
  def __init__(self,x,y):
    self.x=x
    self.y=y
    
class Circulo(Figura):
  
  def __ini__(self,radio,x,y):
      self.radio=radio
      self.punto=Punto(x,y)

""" hola@silabuz.com
soporte@silabuz.com
 """