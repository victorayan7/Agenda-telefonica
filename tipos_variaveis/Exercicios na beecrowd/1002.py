from _decimal import Decimal

raio = Decimal(input())
n = 3.14159
area = Decimal(n) * (raio * raio)
area = Decimal(area)
print(f"A={area:.4f}")
