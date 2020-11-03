import requests
import json

def dolar_value():

	request = requests.get('https://s3.amazonaws.com/dolartoday/data.json')
	charge = json.loads(request.text)

	usd = charge['USD']
	dolar = usd['transferencia']
	dolar = int(dolar)

	main(dolar)


def main(dolar):

	print("Programa para gestión de dolares a través de consola, Bienvenido!!")
	print("Seleccione la transacción que desea realizar")


	print("1.Calcular N° de $")
	print("2.Calcular el valor de Bolivares en $")

	try:	
		selection = int(input(""))

		if selection == 1:
			one(dolar)
		elif selection == 2:
			two(dolar)
		else:
			print("La selección que hiciste es incorrecta")

	except ValueError:
		print("Tienes que seleccionar algo")

def one(dolar):

	print("El dolar hoy es: ", dolar,"Bs.S.")

	number = int(input(" ¿Cuántos dolares desea calcular? "))

	result = dolar * number

	print("El valor es de : ", result)


def two(dolar):
	value = int(input("¿Cuantos Bolivares va a calcular?: "))
	print("El dolar esta hoy a: ", dolar)

	result_2 = value / dolar

	print("El valor es de:  ", result_2)



dolar_value()

