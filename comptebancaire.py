class CompteBancaire(object):
    def __init__(self, nomTitulaire, solde = 0):
        self.nomTitulaire = nomTitulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde = self.solde + montant

    def retrait(self, montant):
        self.solde = self.solde - montant

    def afficher_infos(self):
        print("Nom Titulaire:", self.nomTitulaire)
        print("Solde =", self.solde)

compte1 = CompteBancaire("Ali", 10000)

#Ali depose 2500, retire 3000, retire 7000
compte1.deposer(2500)
compte1.retrait(3000)
compte1.retrait(7000)

#Ali depose 1500
compte1.deposer(1500)

compte1.afficher_infos()
