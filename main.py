# autor:
# Michel

# data: 05/10/2022

# importar agenda

from agenda import Agenda as A

a1 = A()
a1.add("Davi", "eelessandro@contato.com", "rua da casas", "Cajazeiras")
a1.add("Pedro", "email@contato.com", "rua sem saída", "JP")

# busca
a1.buscar("Davi")
a1.buscar("David")
a1.buscar("paulo")
a1.buscar("pedro")


# desafio
# 1- explicar o que aconteceu que na minha busca só imprimi duas 
# informações da pessoa? 
# 2- apresentem uma solução a esse problema.