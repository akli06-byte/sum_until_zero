somme = 0

while True:
    num = int(input("Entrez un nombre: "))
    if num == 0:
        break
    somme += num

print("La somme des nombres précédemment saisis est :", somme)