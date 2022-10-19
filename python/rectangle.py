h = int(input("donner hauteur : "))
l = int(input("donner la largeur : "))
c = "|"
e = "-"

for i in range (h):
    if i == 0 or i == h -1:
        e = "-"
    else : 
        e = " "
    print (c + e * l + c)
