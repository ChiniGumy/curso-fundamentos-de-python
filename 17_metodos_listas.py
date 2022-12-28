# CRUD : Create Read Update Delete

# Create
numbers = [1, 2, 3, 4, 5]
tasks = ['Todo 1', 'Todo 2','Todo 3']

# Read
print(numbers[1])

# Update
numbers[0] = 0
print(numbers)

numbers.append(100)
print(numbers)

numbers.insert(0, 'Ola')	# insert no remplaza
print(numbers)

numbers.insert(3, 'mundo')
print(numbers)

new_list = numbers + tasks 
print(new_list)

new_list[new_list.index('Todo 2')] = 'Todo 2 Completed' 
print(new_list)

# Delete
new_list.remove('Todo 1')	# Exactamente el mismo
print(new_list)

new_list.pop()				# El ultimo
print(new_list)

new_list.pop(0)				# El elemento 0
print(new_list)


# Otros metodos

new_list.reverse()
print(new_list)

numbers_a =[1,4,7,2]
numbers_a.sort()	# ordena de menor a mayor
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort()		# ordena de forma alfabetica
print(strings)

# El metodo sort no sirve cuando una lista tiene mas de un tipo de dato.