import math
radio=int(input("Ingrese el del radio:" ))

def circulo():
	resp=round((math.pi*(radio**2)),2)
	print ("Rspuesta:"+str(resp))

circulo()