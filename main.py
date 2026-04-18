from services.service_salle import ServiceSalle
from models.salle import Salle

service = ServiceSalle()

#Nettoyge avant teste pour ne pas avoir des erreurs
service.supprimer_salle("S200")

# Test ajout
s1 = Salle("S200", "Salle test", "Classe", 10)
success, message = service.ajouter_salle(s1)

print(message)

# Test affichage
liste = service.recuperer_salles()
for s in liste:
    s.afficher_infos()
    print("------")

# Test modification
s2 = Salle("S200", "Salle test modifiee", "Classe", 20)
success, message = service.modifier_salle(s2)
print(message)

# Test recherche
salle = service.rechercher_salle("S200")
if salle:
    salle.afficher_infos()

# Test suppression
service.supprimer_salle("S200")
print("Salle supprimée")
