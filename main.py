# fichier en préparation
# Etape 3 : Initialisation de l architecture en couches et installation des dependances

from data.dao_salle import DataSalle
from models.salle import Salle
dao = DataSalle()


s1 = Salle("S100", "Salle reseau", "Laboratoire", 25)
dao.insert_salle(s1)
print("Insertion réussie")
