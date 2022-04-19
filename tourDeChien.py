class Chien(object) :
    def __init__(self, nom):
        self.nom = nom
        self.tourChien = []
        
    def ajouterTourChien(self, tour):
        self.tourChien.append(tour)
        
    def afficher_info(self):
        print ("Nom du chien:", self.nom)
        print("Tour du chien:", self.tourChien)


monChien = Chien ("Rex")
monChien.ajouterTourChien ("Faire le mort")
monChien.ajouterTourChien ("Rouler sur dos")
monChien.ajouterTourChien ("Donner sa pate")
monChien.afficher_info()
