def tipo_salsa(ingredientes, eleccion):

	if eleccion == 'T':
		ingredientes['salsa'] = 'Salsa de Tomate'
	elif eleccion == 'A':
		ingredientes['salsa'] = 'Salsa Alfredo'
	elif eleccion == 'B':
		ingredientes['salsa'] = 'Salsa Berbecue'
	elif eleccion == 'P':
		ingredientes['salsa'] = 'Salsa Pesto'

	if eleccion in ['T', 'A', 'B', 'P']:
		print(f"Su salsa se cambió a {ingredientes['salsa']}")
	else:
		print("No se ha cambiado su tipo de Salsa")

	return ingredientes

if __name__ == "__main__":

	ingredientes_prueba = {
		'masa': 'Masa Tradicional',
		'salsa': 'Salsa de Tomate',
		'ingredientes': ['queso']
	}

	eleccion = input('''Seleccione el tipo de Salsa:

(T) Salsa de Tomate
(A) Salsa Alfredo
(B) Salsa Berbecue
(P) Salsa Pesto

Otra opción no modificará el tipo de Salsa.
> ''')

	ingredientes = tipo_salsa(ingredientes_prueba, eleccion.upper())
	print(ingredientes)
