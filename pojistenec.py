class Pojistenec:

    def __init__(self, jmeno, prijmeni, telefon, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.telefon = telefon
        self.vek = vek

    def __str__(self):
        return "{0} \t{1} \t{2} \t{3}".format(self.jmeno, self.prijmeni, self.telefon, self.vek)

