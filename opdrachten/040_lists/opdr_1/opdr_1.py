# Opdracht 1 lists
# Naam student: Joost Dommerholt
# Groep:

# Maak een list
lijst = []

# Maak 4 dictionaries met gegevens van personen
persoon_1 = { "id": 0, "voornaam": "Joost", "achternaam": "de Vries" }
persoon_2 = { "id": 1, "voornaam": "Bas", "achternaam": "Jansen" }
persoon_3 = { "id": 2, "voornaam": "Stefan", "achternaam": "Peters" }
persoon_4 = { "id": 3, "voornaam": "Arjan", "achternaam": "Smit" }

# Voeg de dictionaries toe aan de list met behulp van een list-methode
lijst.append(persoon_1)
lijst.append(persoon_2)
lijst.append(persoon_3)
lijst.append(persoon_4)

# Print de volledige naam van de 2e persoon (index 1)
print(lijst[1]["voornaam"], lijst[1]["achternaam"])

