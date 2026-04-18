# fichier en préparation
# Etape 3 : Initialisation de l architecture en couches et installation des dependances

from data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

# Test connexion
connexion = dao.get_connection()
if connexion.is_connected():
    print("Connexion réussie")
connexion.close()

# Nettoyage avant test
dao.delete_salle("S101")

# Test ajout
s1 = Salle("S101", "Salle programmation", "Laboratoire", 20)
dao.insert_salle(s1)
print("Salle ajoutée")

salle = dao.get_salle("S101")
if salle is not None:
    print("Salle trouvée :")
    salle.afficher_infos()

