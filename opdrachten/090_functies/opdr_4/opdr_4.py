# Opdracht 1 functies
# Naam student: Joost Dommerholt
# Groep:


def volledige_naam(lijst_met_namen):
    for naam in lijst_met_namen:
        # Controleer of er een tussenvoegsel is, zo niet, voeg het niet toe
        if naam['tussenvoegsel']:
            volledige_naam = f"{naam['voornaam']} {naam['tussenvoegsel']} {naam['achternaam']}"
        else:
            volledige_naam = f"{naam['voornaam']} {naam['achternaam']}"

        print(volledige_naam)


# Voorbeeldlijst met namen
namen = [
    {"voornaam": "Henk", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Jopie", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Peter", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carien", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

# Functie aanroepen
volledige_naam(namen)
