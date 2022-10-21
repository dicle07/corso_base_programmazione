media=0
contatore=0
numero=0
while True:
    numero=int(input("inserisci numero"))
    media=media+numero
    if numero==0:
        break
    contatore=contatore+1
media=media/contatore
print(media)