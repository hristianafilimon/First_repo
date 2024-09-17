from gradinita.gradinitaABC import GradinitaABC

class Gradinita_Privata(GradinitaABC):
    def __init__(self):
        self.elevi = {}
        self.__valoare_taxa = None

    def activitate_practica(self):
        print('Copiii invata sa modeleze cu plastilina')

    def ora_de_somn(self):
        print('Ora de somn este 15.00')

    def adauga_elev(self, nume_elev, varsta_elev, an_inscriere, taxa_platita):
        #{<nume_elev>:{"varsta": <varsta_elev>, "an_inscriere":<an_inscriere>, "taxa_platita": <taxa_platita"}
        self.elevi[nume_elev] = {
            "varsta": varsta_elev,
            "an_inscriere": an_inscriere,
            "taxa_platita": taxa_platita
        }

    #implementam metoda "afisare elevi" si o apelam in Main

    @property
    def valoare_taxa(self):
        return self.__valoare_taxa

    @valoare_taxa.getter
    def valoare_taxa(self):
        return f'{self.__valoare_taxa} lei'

    @valoare_taxa.setter
    def valoare_taxa(self, taxa_noua):
        if taxa_noua < 5000:
            print('Taxa e de 5000 lei. Trebuie achitata toata suma o data.')
        elif taxa_noua > 5000:
            self.__valoare_taxa = 5000
            print(f'Taxa este de 5000 Ron, a fost platita cu succes si restul sumei de {taxa_noua - 5000} Lei va fi returnata')
        else:
            self.__valoare_taxa = 5000
            print('Taxa a fost platita cu succes')






