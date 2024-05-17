def ossz_sebzes(fej_sebzes, test_sebzes, lotar):
    eredmenyek = []
    max_sebzes = fej_sebzes * lotar
    eredmenyek.append(max_sebzes)
    min_sebzes = test_sebzes * lotar
    eredmenyek.append(min_sebzes)
    return eredmenyek

for i in range(3):
    fegyver = input("Fegyver neve: ")
    fej_sebzes = int(input("Fegyver fejlövés sebzése: "))
    test_sebzes = int(input("Fegyver test sebzése: "))
    lotar = int(input("Fegyver tára: "))
    eredmenyek = ossz_sebzes(fej_sebzes, test_sebzes, lotar)
    print(f'A(z) {fegyver} nevű fegyver legfeljebb {eredmenyek[0]} pont sebzést, s legalább {eredmenyek[1]} pont sebzést tud okozni, ha minden lövés talál.')
