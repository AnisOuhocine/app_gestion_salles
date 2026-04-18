# fichier en préparation
# Etape 3 : Initialisation de l architecture en couches et installation des dependances

from data.dao_salle import DataSalle

dao = DataSalle()
dao.delete_salle("S100")
print("Suppression réussie")
