text = 'El pepe sabe Python'

for i in range(len(text)):
	print(text[i])

print(f'\nLast char: {text[len(text) - 1]}')
print(f'\nNegatives char: {text[-1]}')

print(text[0:5])
print(text[10:16])
print(text[:10])	# Sin valor inicial, es desde el index 0
print(text[5:])		# Sin valor final, llega hasta el final index
print(text[1:3:12])