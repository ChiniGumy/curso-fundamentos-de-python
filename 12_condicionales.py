if True:
	print('Deberia ejecusarse')

if False:
	print('Nunca se va a ejecutar')


# Ejercicio de Dome =========================

# En una boda, solo son permitidos los adultos, si son adultos mayores, o niños, no estan permitidos.

user_age: int = int(input('Ingresa tu edad:  '))

if user_age > 18 and user_age < 65:
	print('Puedes pasar')

elif user_age < 18:
	print('No puedes pasar, eres un niño')

elif user_age > 65:
	print('No puedes pasar, eres un anciano')
