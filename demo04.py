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
        
capacidad_columna=15
def agregar_espacios(texto):
    cant_espacios=capacidad_columna-len(texto)
    if(cant_espacios>=0):
        for i in range(cant_espacios):
            texto=texto+" "
        return texto
    else:
        nuevo_texto=""
        for i in range(capacidad_columna):
            nuevo_texto=nuevo_texto+texto[i]
            #if((i+1)>=(capacidad_columna-2)):
            #    nuevo_texto=nuevo_texto+"."
            #else:
            #    nuevo_texto=nuevo_texto+texto[i]
        return nuevo_texto
        
def print_report(fruits):
    total=0
    print("======== Reporte de Frutas =========")
    print("")
    print(agregar_espacios("FRUTA")+"|"+agregar_espacios("PRECIO"))    
    for fruit in fruits:
        total=total+fruit.precio
        print(agregar_espacios(fruit.nombre)+"|"+agregar_espacios(str(fruit.precio)))
    print(agregar_espacios("Grand Total")+"|"+agregar_espacios(str(total)))    
     
canastaFrutas=[]     
while(question()):
    fruit_name=input("Ingrese nombre de fruta: ")
    price_fruit=float(input("Ingrese precio de fruta: "))
    canastaFrutas.append(frutas(fruit_name,price_fruit))        

if(len(canastaFrutas)>0):
    print_report(canastaFrutas)
else:
    print("\n  Hasta pronto!")
    