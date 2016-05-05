import math
lado1= int(input("Ingresar el primer lado del triangulo:"))
lado2= int(input("Ingresar el segundo lado del trinagulo"))
lado3= int(input("Ingresar el tercer lado del triangulo"))
s=(lado1+lado2+lado3)/2
def perimetrot():
	per=lado1+lado2+lado3
	print("el perimetro es:"+str(per))	
def areat():
	ar= math.sqrt(s*(s-lado1)*(s-lado2)*(s-lado3))
	print ("el area es:"+ str(ar))

perimetrot()
areat()
