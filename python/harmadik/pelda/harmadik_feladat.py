from jatekos import Jatekos
from math import inf

jatekosok :list[Jatekos] = []

def main():
    load_file("jatekosok.csv")     
    print(f"3. feladat: Játékosok száma: {len(jatekosok)}")
    legkisebb_ert = legkisebb_ertekeles()
    print(f"4. feladat: A(z) {legkisebb_ert.nev} nevű játékosnak van a legkisebb értékelése: {legkisebb_ert.ertekeles}")
    orszag = input("5. feladat: Adjon meg egy országot: ").capitalize()
    orszagiak = orszag_jatekosok(orszag)
    if len(orszagiak) == 0:
        print("Nincs ilyen nemzetiségű játékos.")
    else:
        for orszagi in orszagiak:
            print(f"\t{orszagi.nev} - {orszagi.csapat} - {orszagi.ertekeles}")
    eredmeny, igaz_jatekosok = fejhalal_szazalek()
    print("6. feladat:")
    if eredmeny:
        print("Van(vak) ilyen játékos(ok):")
        for igaz_jatekos in igaz_jatekosok:
            print(f"\t{igaz_jatekos.nev} - {igaz_jatekos.halal}% - {igaz_jatekos.fejloves}%")
    else:
        print("Nincs ilyen játékos.")
    jok = nagyobb_nyito(10.0)
    print("7. feladat:")
    for jo in jok:
        print(f"\t{jo.nev} - {jo.csapat} - {jo.nyito}%")
    csapat = input("8. feladat: Adjon meg egy csapatot: ")
    letezik = letezo_csapat(csapat)
    if letezik:
        new_file(csapat)
        print("Fájl létrehozva.")
    else:
        print("Jelenleg nincs olyan játékos, aki ennél a csapatnál játszana.")


def load_file(filename) -> None:
    file = open(filename, encoding='utf-8')
    file.readline()
    for row in file:
        jatekosok.append(Jatekos(row))
    file.close()

def legkisebb_ertekeles() -> Jatekos:
    lk_jatekos = None
    lk_ertekeles = inf
    for jatekos in jatekosok:
        if jatekos.ertekeles < lk_ertekeles:
            lk_ertekeles = jatekos.ertekeles
            lk_jatekos = jatekos
    return lk_jatekos

def orszag_jatekosok(orszag) -> list[Jatekos]:
    orszagiak = []
    for jatekos in jatekosok:
        if jatekos.orszag == orszag:
            orszagiak.append(jatekos)
    return orszagiak

def fejhalal_szazalek():
    eredmeny = False
    igaz_jatekosok:list[Jatekos] = []
    for jatekos in jatekosok:
        if jatekos.fejloves > jatekos.halal:
            eredmeny = True
            igaz_jatekosok.append(jatekos)
    return eredmeny, igaz_jatekosok

def nagyobb_nyito(szazalek:float) -> list[Jatekos]:
    jok :list[Jatekos] = []
    for jatekos in jatekosok:
        if jatekos.nyito > szazalek:
            jok.append(jatekos)
    return jok

def letezo_csapat(csapat) -> bool:
    letezik = False
    for jatekos in jatekosok:
        if jatekos.csapat == csapat:
            letezik= True
    return letezik

def new_file(csapat:str) -> None:
    file = open(f"{csapat.lower()}.csv", 'w', encoding='utf-8')
    for jatekos in jatekosok:
        if jatekos.csapat == csapat:
            file.write(f"{jatekos.nev};{jatekos.orszag};{jatekos.csapat};{jatekos.ertekeles};{jatekos.nyito};{jatekos.halal};{jatekos.fejloves}\n")
    file.close()

main()