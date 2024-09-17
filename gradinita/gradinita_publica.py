from gradinita.gradinitaABC import GradinitaABC

class Gradinita_Publica(GradinitaABC):
    def __init__(self):
        self.elevi = {}
    def activitate_practica(self):
        print('Copii invata sa deseneze')
    def ora_de_somn(self):
        print('Copiii trebuie sa doarma la ora 5')

    def adauga_elev(self, nume_elev, varsta_elev, an_inscriere):
        #{<nume_elev>:{"varsta": <varsta_elev>, "an_inscriere":<an_inscriere>}
        self.elevi[nume_elev] = {
            "varsta": varsta_elev,
            "an_inscriere": an_inscriere
        }

    # implementam metoda "afisare elevi" si o apelam in Main

