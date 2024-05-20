class Jatekos:
    def __init__(self, row) -> None:
        splitted = row.split(';')
        self.nev = splitted[0]
        self.orszag = splitted[1]
        self.csapat = splitted[2]
        self.ertekeles = float(splitted[3])
        self.nyito = float(splitted[4])
        self.halal = float(splitted[5])
        self.fejloves = float(splitted[6])
    