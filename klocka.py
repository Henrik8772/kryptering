# Starttid (kl 08:00)

klockan = int(input("Vad är klockan?: "))
hopp = int(input("Hur många timmar går det?: "))

dygn = 0

print(f"Startar klockan {klockan}:00")

for i in range(1, 5):
    total_tid = klockan + hopp

    nya_dygn = total_tid//24
    # räknar ut hur många hela dygn som går
    # alltså exempelvis från Resa 1: 08:00 till Resa 4: 08:00 går det 1 dygn om klockan = 8 och hopp = 6
    # och från Resa 1: 12:00 till Resa 4: 12:00 går det 12 dygn om klockan = 12 och hopp = 72

    dygn += nya_dygn

    gammal_tid = klockan
    klockan = total_tid % 24

    print(f"Resa {i}: Från {gammal_tid}:00 till {klockan}:00")

print(f"Dygn: {dygn}")
