# fichier en préparation
# Etape 3 : Initialisation de l architecture en couches et installation des dependances

from data.dao_salle import DataSalle

dao = DataSalle()
connexion = dao.get_connection()
print(connexion)

if connexion.is_connected():
    print("Connexion réussie")
    connexion.close()