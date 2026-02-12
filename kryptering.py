
# en sträng med alla bokstäver i det svenska alfabetet
alfabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "å", "ä", "ö"
]


# meddelandet som ska krypteras
meddelande = "läxa"
# nyckeln är antalet positioner varje bokstav ska flyttas
nyckel = 3
# variabel för att lagra det krypterade meddelandet
resultat = ""

# UPPDRAG: Skriv en loop som skriver ut "ifk"
# Tips: Använd .index() och []

for letter in meddelande:
    old_position = alfabet.index(letter)
    new_position = old_position + nyckel

    if new_position >= len(alfabet):
        new_position = new_position - len(alfabet)

    resultat += alfabet[new_position]

print(resultat)
