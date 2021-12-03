#frutas=['manzana','pera','platano','piña']
class frutas:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

def question():
    answer=input("Desea agregar alguna fruta? (Y/N)")
    if(answer=="Y"):
        return True
    else:
        return False
        
def print_report(fruits):
    total=0
    print("======== Reporte de Frutas =========")
    print("")
    print("Fruta            Precio")    
    for fruit in fruits:
        total=total+fruit.precio
        print(fruit.nombre+"            "+str(fruit.precio))
    print("Grand Total              "+str(total))    
     
canastaFrutas=[]     
while(question()):
    fruit_name=input("Ingrese nombre de fruta: ")
    price_fruit=float(input("Ingrese precio de fruta: "))
    canastaFrutas.append(frutas(fruit_name,price_fruit))        

if(len(canastaFrutas)>0):
    print_report(canastaFrutas)
else:
    print("\n  Hasta pronto!")
   
