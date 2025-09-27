# Exemplo
def saudacao(nome):
    print(f"Olá, {nome}!")

print("\n Chamando a função saudação: ")
saudacao("Alice")
saudacao("Bob")


# Função com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\n Chamando função quadrado: ")
resultado_quadrado = quadrado(5)
print("Resultado da função quadrado ", resultado_quadrado)


# Função com multiplos parametros

def soma (numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\nChamando a função soma")
#resultado_soma = soma(20, 50)
#print("A soma do numero 20 e numero 50 é", resultado_soma)

numero1 = 20
numero2 = 50
resultado_soma = soma(numero1, numero2)
print("A soma do numero %s e o numero %s é %s" % (numero1, numero2, resultado_soma))
 
