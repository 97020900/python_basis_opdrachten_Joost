# Opdracht 1 functies
# Naam student: Joost Dommerholt
# Groep:


# Functie om kilometers om te zetten naar miles
def kilometers_naar_miles(kilometers):
    return kilometers / 1.609344  # Omrekeningsfactor van km naar miles

# Functie om miles om te zetten naar kilometers
def miles_naar_kilometers(miles):
    return miles * 1.609344  # Omrekeningsfactor van miles naar km

# Voorbeeld gebruik
kilometers = 124
miles = 895

# Roep de functies aan
miles_omgezet = kilometers_naar_miles(kilometers)
kilometers_omgezet = miles_naar_kilometers(miles)

# Print de resultaten
print(f"{kilometers} kilometers = {miles_omgezet} miles")
print(f"{miles} miles = {kilometers_omgezet} kilometers")
