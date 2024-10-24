# Opdracht 1 functies
# Naam student: Joost Dommerholt
# Groep:


def write_to_file(filename, text):
    with open(filename, 'a') as file:  # Open het bestand in 'append' modus ('a')
        file.write(text + '\n')  # Voeg de tekst toe en sluit af met een nieuwe regel

my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test2.txt"
write_to_file(my_file, my_tekst)



