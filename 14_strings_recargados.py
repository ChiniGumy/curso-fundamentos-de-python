text = 'Aqui con mi compa el sech, ete sech'
print('JavaScript' in text)
print('sech' in text)

if 'sech' in text:
	print('\nSi existe el sech')
else:
	print('\nNo existe el sech :(')

text2 = 'El pepe, Maicol mamahuevaso'
size = len(text2)
print(text2)
print(size)

print(text2.upper())	# Convierte todo a mayuscula
print(text2.lower())	# Covierte todo a minuscula
print(text2.count('e'))	# Cuenta cuantos caracteres que nosotros especifiquemos hay en el string
print(text2.swapcase()) # minuscula a mayuscula y en biceversa
print(text2.startswith('El'))
print(text2.endswith('sech'))
print(text2.replace('Maicol', 'Sech'))

text3 = 'esto es un titulo'
print(text3)
print(text3.capitalize())	# Primer caracter en Mayus
print(text3.title()) 		# Inicio de cada palabra en Mayus
