def mostrar_ingredientes(ingredientes):
	print(f"Su masa es: {ingredientes['masa']}")
	print(f"Su salsa es: {ingredientes['salsa']}")
	print("Los ingredientes son:")
	[print(f"- {ingr}") for ingr in ingredientes['ingredientes']]
	
if __name__ == "__main__":

	ingredientes_prueba = {
		'masa': 'Masa Tradicional',
		'salsa': 'Salsa de Tomate',
		'ingredientes': ['Queso', 'Tomate', 'Pollo']
	}
	mostrar_ingredientes(ingredientes_prueba)
