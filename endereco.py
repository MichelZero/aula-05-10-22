# autor:
# Michel

# data: 05/10/2022

# rua, cidade
class Endereco:
  
  #
  def __init__(self, rua, cidade):
    self.rua = rua
    self.cidade = cidade
    
  def mostrar(self):
    print(f"{self.rua} -> {self.cidade}")