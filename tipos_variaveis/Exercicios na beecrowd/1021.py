N = float(input())

print(N)

notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
    qtd = N // nota
    qtd = int(qtd)
    print(f"{qtd} nota(s) de R$ {nota}")
    N = N % nota

print("MOEDAS:")
for moeda in moedas:
    qtd = N // moeda
    qtd = int(qtd)
    print(f"{qtd} moeda(s) de R$ {moeda:.2f}")
    N = N % moeda
