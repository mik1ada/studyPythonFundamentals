spizarnia = {
    "Maka kg": 2,
    "Cukier kg": 1,
    "Mleko szt": 3,
    "Chleb szt": 1
}
print("Zawartosc spizarni to:", spizarnia)

spizarnia["Mleko szt"] += 2
spizarnia["Jajka szt"] = 10
print(spizarnia)

if "Maka kg" in spizarnia and spizarnia["Maka kg"] > 0:
    print("Mozna robic ciasto!")
else:
    print("Brakuje maki na ciasto!")

iloscSoli = spizarnia.get("Sol kg", 0)
print("Ilosc soli w lodowce wynosi:", iloscSoli, "kg")

zuzytyChleb = spizarnia.pop("Chleb szt")
print("Na kolacje zuzyto", zuzytyChleb, "sztuki chleba")

print("Koncowy stan spizarni: ")
for produkt, ilosc in spizarnia.items():
    print(f"Produkt: {produkt}, Ilosc: {ilosc} " )
