class Figura:
  def __init__(self,nombre,area,coordenadaX,coordenadaY) -> None:
    self.nombre=nombre
    self.__area=area
    self.coordenadaX=coordenadaX
    self.coordenadaX=coordenadaX
  def getnombre(self):
    
    return self.nombre
  
  def getarea(self):
    
    return self.area
  
  def getcoordenadaX(self):
    
    return self.coordenadaX
  
  def getcoordenadaY(self):
    
    return self.coordenadaY
  
  def setnombre(self,nombre):
    
    self.nombre=nombre
  
  def setarea(self,area):
    
     self.__area=area
  
  def setcoordenadaX(self,coordenadaX):
    
     self.coordenadaX=coordenadaX
  
  def setcoordenadaY(self,coordenadaX):
    
     self.coordenadaX=coordenadaX
  
  def mostrar_figura(self):
    va=f"La figura se llama {self.nombre} \nTiene un área de 'Área': {self.__area} \
    y inicia en las coordenadas ('{self.coordenadaX}', '{self.coordenadaX}' )"
    print(va)

figura=Figura("circulo",30.5,-1,2)
figura.mostrar_figura()