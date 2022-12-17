# lives: int = 3
# print(lives)
# print(type(lives))

# temperature: float = 273.15
# print(temperature)
# print(type(temperature))

# Calcular promedio de gastos de ciertos meses (los tres primeros)

gasto_total: float = 0

for i in range(1, 4):

	gasto_mes: float = int(input(f'Ingresa el gasto (0{i}):  '))

	gasto_total += gasto_mes

print(f'Tu promedio de gasto: ${gasto_total / 3}')
