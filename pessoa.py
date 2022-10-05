#
from msilib import MSIDBOPEN_PATCHFILE


# autor:
# Michel

# data: 05/10/2022

# nome, email
class Pessoa:
  
  #
  def __init__(self, nome, email):
    self.nome = nome
    self.email = email
    
  def mostrar(self):
    print(f"{self.nome} -> {self.email}")