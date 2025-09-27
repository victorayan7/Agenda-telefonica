print("Exemplo de importação de um módulo padrão: ")
#import math or from math import sqrt
from math import sqrt

raiz_quadrada = sqrt(25)
print(f"A raiz quadrada de 25 é {raiz_quadrada}")

print("\n Exemplo de criação e utilização de um módulo personalizado: ")

import meu_modulo
#from meu_modulo import saudcao, dobro

mensagem = meu_modulo.saudcao("Gabriel")
resultad_dobro = meu_modulo.dobro(5)

print(mensagem)
print(f"O dobro de 5 é {resultad_dobro}")