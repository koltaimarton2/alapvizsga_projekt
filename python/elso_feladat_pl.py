felhasznalonev = input("Adja meg a Steam felhasználónevét! ")
jelszo = "a"
while True:
    jelszo = input("Adja meg a jelszavát! ")
    if len(jelszo) >= 5 and felhasznalonev not in jelszo:
        print("Megfelelő jelszó.")
        print(f"A(z) {felhasznalonev} nevű Steam fiókhoz tartozó jelszó '{jelszo}'.")
        break
    if len(jelszo) < 5:
        print("A jelszó nem hosszabb 5 karakternél.")
    if felhasznalonev in jelszo:
        print("A jelszó tartalmazza a felhasználónevet.")
    
