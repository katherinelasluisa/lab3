a= int(input("ingrese un numero"))
b=int(input("ingrese el segundo numero:"))

def suma():
    resp=a+b
    print ("suma"+str(resp))
def resta():
    resp=a-b
    print ("resta:"+str(resp))
def division():
    if b==0:
        print ("no hay divison para 0")
    else:
        res=a/b
        print ("division:"+str(res))
      

suma()
resta()
division()
