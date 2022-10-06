# autor:
# Michel

# data: 05/10/2022

# importar contato
from contato import Contato as C 

class Agenda:
  
  pessoaD = dict()
  
  def add(self, nome, email, rua, cidade):
    self.pessoaD[nome] = C(nome, email, rua, cidade)
  
  def buscar(self, nome):
    if nome in self.pessoaD:
      self.pessoaD[nome].mostrar()
    else:
      print(f"{nome} -> não existe!")
      # print(self.pessoaD)      # print(self.pessoa) #se quiser ver o dicionário em memoria