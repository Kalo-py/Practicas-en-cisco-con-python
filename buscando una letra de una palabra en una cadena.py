def buscar(pal1,pal2):
    bol=False
    for i in pal1:
        if pal2.find(i)==-1:
            bol=False
            break
        else:
            bol=True

    if bol==True:
        return "Si"
    else:
        return "No"

pal1=str(input("Ingresa la palabra que quieres buscar: "))
pal2=str(input("Ingresa la palabra en la que buscaras la primera: "))
print(buscar(pal1,pal2))