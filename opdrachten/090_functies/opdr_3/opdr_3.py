# Opdracht 1 functies
# Naam student: Joost Dommerholt
# Groep:


import math  # Nodig voor de waarde van pi

# Functie om het volume van een kubus te berekenen
def kubus_vol(zijde):
    return zijde ** 3  # Volume is zijde^3

# Functie om het volume van een bol te berekenen
def bol_vol(straal):
    return (4 / 3) * math.pi * (straal ** 3)  # Volume van een bol: (4/3) * pi * straal^3

# Voorbeeld gebruik voor de kubus
kubus_volume = kubus_vol(5)
print(f"De inhoud van deze kubus is: {kubus_volume}")

# Voorbeeld gebruik voor de bol
bol_volume = bol_vol(4)
print(f"De inhoud van deze bol is: {bol_volume}")
