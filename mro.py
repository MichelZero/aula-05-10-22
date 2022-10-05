#
#
###############################
# classes
class A:
  def falar(self):
    print("o objeto A está falando ....")

class B():
  def falar(self):
    print("o objeto B está falando ....")
    
class C(B, A):
  pass

###############################
# criar os objetos (instanciar)
a1 = A()
b1 = B()
c1 = C()

###############################
# usar os métodos
a1.falar()
b1.falar()
c1.falar()

#################################
# MRO - Ordem de Resolução de Método 
print(A.__mro__)
print(B.__mro__)
print(C.__mro__)