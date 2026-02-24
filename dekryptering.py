import string
# det var här jag hittade det https://www.geeksforgeeks.org/python/python-string-module/ samt om string.punctuation

alfabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "å", "ä", "ö"
]

krypterat = "Zwä, zjg bpg vj?"
ordlista = ["hej", "hur", "mår", "du", "äta", "mat", "klockan", "är"]

for nyckel in range(0, len(alfabet)):
    dekrypterat = ""
    for b in krypterat.lower():
        if b.lower() in alfabet:
            dekrypterat += alfabet[alfabet.index(b) - nyckel % 29]

        else:
            dekrypterat += b
    print(dekrypterat)

    for word in dekrypterat.split():
        clean_word = word.strip(string.punctuation)
        clean_word = clean_word.lower()
        if clean_word in ordlista:
            print(nyckel)
