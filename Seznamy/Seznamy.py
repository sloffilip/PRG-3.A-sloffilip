zavodnici = ["Vettel", "Schumacher", "Ocon", "Alonso", "Verstappen"]

otazka = input("Co chcete dál udělat?:\na. Přidat další jméno\nb. Vypsat seznam\nc. Vymazat zvolené jméno ze seznamu\nd. vypsat počet jmen v seznamu\ne. Vypsat seznam jmen seřazený podle abecedy")

if otazka == "a" or otazka == "A":
    zavodnici.append(input("Jaké jméno chcete přidat?"))
    print(zavodnici)

if otazka == "b" or otazka == "B":
    print(zavodnici)

if otazka == "c" or otazka == "C":
    zavodnici.pop(int(input("Jaké jméno chcete odebrat? (Zadejte pozici na kterém se nachází)")))
    print(zavodnici)

if otazka == "d" or otazka == "D":
    pocet = len(zavodnici)
    print("V závodě se nachází", pocet, "závodníků")

if otazka == "e" or otazka == "E":
    zavodnici.sort()
    print(zavodnici)










