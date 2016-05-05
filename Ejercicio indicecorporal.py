#calcular el indice de masa corporal
peso=float(input("Ingrese su peso en kilogramos"))
estatura=float(input("Ingrese su altura en metros"))

def calculo():
	indice=peso/estatura**2
	print("el indice de masa corporal:"+ str(indice))
	obesidad(indice)


def obesidad(indice):
	if indice >40:
		print ("Obesidad morbida")
	elif indice >=35:
		print ("Obesidad media")
	elif indice >=30:
		print("Obesidad leve")
	elif indice >=25:
		print (" Sobre peso")
	elif indice >=18.50:
		print ("Peso normal")
	elif indice >=18.49:
		print ("Infra peso")

calculo()