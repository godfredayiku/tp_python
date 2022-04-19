import math

class Cercle(object):
    def __init__(self, rayon):
        self.rayon = rayon
        self.nom = "Cercle"

    def surface(self):
        s = math.pi * (self.rayon**2)
        return(s)

    def __str__(self):
        return("\n Le {} ayant une rayon de {} a une surface de {}."
               .format(self.nom, self.rayon, self.surface()))

class Cylindre(Cercle):
    def __init__(self, hauteur, rayon):
        self.hauteur = hauteur
        Cercle.__init__(self, rayon)
        self.nom = "Cylindre"

    def volume(self):
        v = self.surface() * self.hauteur
        return(v)

class Cone(Cylindre):
    def __init__(self, hauteur, rayon):
        Cylindre.__init__(self, hauteur, rayon)
        self.nom = "Cone"
        
    def volume_cone(self):
        v = self.volume()/3
        return(v)

cercle = Cercle(5)
surface = cercle.surface()
print(surface)

cylindre = Cylindre(5, 10)
surface = cylindre.surface()
print(surface)
volume = cylindre.volume()
print(volume)

cone = Cone(2, 5)
surface = cone.surface()
print(surface)
volume = cone.volume_cone()
print(volume)

print(cercle)
print(cylindre)
