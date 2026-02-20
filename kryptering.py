
# en sträng med alla bokstäver i det svenska alfabetet
alfabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "å", "ä", "ö"
]


# meddelandet som ska krypteras
meddelande = "Hej, hur mår du?"
# nyckeln är antalet positioner varje bokstav ska flyttas
nyckel = 250
# variabel för att lagra det krypterade meddelandet
resultat = ""

# UPPDRAG: Skriv en loop som skriver ut "ifk"
# Tips: Använd .index() och []

for letter in meddelande:
    if letter.lower() in alfabet:
        # Detta är en kontrol if sats som behövs för att kontrolerar om de är lowercase bokstäver i meddelandet

        old_position = alfabet.index(letter.lower())
        new_position = (old_position + nyckel) % len(alfabet)

        # Det hjälpte mycket att du bad mig träna på modulen
        # men jag tog dock hjälp av geeksforgeeks för att vet vad modulus egentligen gör

        new_letter = alfabet[new_position]
        # En ny variabel för att underlätta med resten av if satserna

        if letter.isupper():
            # Samma typ av if sats som den första men för just uppercase

            resultat += new_letter.upper()
            # Om det finns bokstäver i meddelandet som är uppercase så printas
            # de nya bokstäverna som har det i just uppercase

        else:
            resultat += new_letter
            # detta är bara om ingen bokstav är uppercase så printas den som lowercase
    else:
        resultat += letter
        # Denna hjälper med sånt som , och ? genom att när du printar ut resultatet så blir de inte ändrade

print(resultat)
