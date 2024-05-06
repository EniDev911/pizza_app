from masa import tipo_masa
from salsa import tipo_salsa
from add import agregar_ingrediente
from remove import quitar_ingrediente
from show import mostrar_ingredientes
from tiempo import estimar_tiempo

ingredientes_orden = {
	'masa': 'Masa Tradicional',
	'salsa': 'Salsa de Tomate',
	'ingredientes': ['Queso']
}

print("¡Gracias por ordenar con nosotros!")
while True:

	opcion = input('''¿Qué desea realizar?

(1) Cambiar tipo de Masa
(2) Cambiar tipo de Salsa
(3) Agregar Ingredientes
(4) Eliminar Ingredientes
(5) Ordenar con los Ingredientes Actuales

(0) Consultar ingredientes de la pizza

Otro Número cancelará el pedido.
> ''')

	if opcion == '1':
		eleccion = input('''Seleccione el tipo de Masa:

(T) Masa Tradicional
(D) Masa Delgada
(B) Masa con Bordes de Queso

Otra opción no modificará el tipo de Masa
> ''')

		ingredientes_orden = tipo_masa(ingredientes_orden, eleccion.upper())

	elif opcion == '2':
		eleccion = input('''Seleccione el tipo de Salsa:

(T) Salsa de Tomate
(A) Salsa Alfredo
(B) Salsa Berbecue
(P) Salsa Pesto

Otra opción no modificará el tipo de Salsa.
> ''')

		ingredientes_orden = tipo_salsa(ingredientes_orden, eleccion.upper())

	elif opcion == '3':
		eleccion = int(input('''Seleccione el ingrediente que desea agregar:

(1) Tomate
(2) Champiñones
(3) Aceituna
(4) Cebolla
(5) Pollo
(6) Jamón
(7) Carne
(8) Tocino
(9) Queso

Otra opción no modificará los ingredientes actuales.
> '''))

		ingredientes_orden = agregar_ingrediente(ingredientes_orden, eleccion)

	elif opcion == '4':
		eleccion = int(input('''Seleccione el ingrediente que desea quitar:

(1) Tomate
(2) Champiñones
(3) Aceituna
(4) Cebolla
(5) Pollo
(6) Jamón
(7) Carne
(8) Tocino
(9) Queso

Otra opción no modificará los ingredientes actuales.
> '''))

		ingredientes_orden = quitar_ingrediente(ingredientes_orden, eleccion)

	elif opcion == '5':

		tiempo = estimar_tiempo(ingredientes_orden, eleccion)
		print(f"Su pizza estará lista en {tiempo} minutos")
		ordenar = input("Desea ordenar ahora S/N: ").upper()

		if ordenar == 'S':
			print("Gracias por ordenar en Pizza JAT")
			print("Disfrute su Pizza")
			exit()

	elif opcion == '0':
		mostrar_ingredientes(ingredientes_orden)
	else:
		print("Su pedido ha sido cancelado. Gracias por contactarse a Pizza Jat")
		exit()
