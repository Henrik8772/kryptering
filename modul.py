timmar_dagen = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00",
                "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00",
                "21:00", "22:00", "23:00"]

början = ["12:00"]

timmar = 48

klockan = ""

for time in början:
    old_time = timmar_dagen.index(time)
    new_time = old_time + timmar

    if new_time >= len(timmar_dagen):
        new_time = new_time % len(timmar_dagen)

    klockan += timmar_dagen[new_time]

print(klockan)

# vet äntligen vad % modulen gör modulus den returnar resten av new_time / len(timmar_dagen)
# alltså den kollar om len(timmar_dagen) får plats i new_time annars returnar den ursprungs värdet:)
