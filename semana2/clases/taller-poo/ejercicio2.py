""" Cree una clase Automovil con los siguientes atributos.

Marca
Año
Placa
Número de Asientos
Escriba los getters y setter del atributo marca.

Cree dos métodos, mostrar_carro y tipo_carro.

mostrar_carro imprime: """

class Vehiculo:
  def __init__(self,marca,anio,placa,n_asientos) -> None:
    self.__marca=marca
    self.anio=anio
    self.placa=placa
    self.n_asientos=n_asientos
    
  def get_marca(self):
    return self.__marca
  
  def set_marca(self,marca):
    self.__marca=marca
    
  def mostrar_carro(self):
    
    print(f'El carro es de marca "{self.__marca} " del año "{self.anio}" Y tiene placa número "{self.placa} "')
  
  def tipo_carro(self):
      message=" El automovil es un carro normal"
      if self.n_asientos > 20:
          message="El automovil es un bus"
      elif self.n_asientos > 10:
          message="El automovil es un combi"

      print(message)
  def __del__(self):
      
      print("el objeto se eliminara")
      
vehiculo=Vehiculo("Suzuki",2010,"ABC-456",4)
vehiculo.mostrar_carro()
vehiculo.__del__()