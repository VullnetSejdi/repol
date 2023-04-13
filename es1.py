with open("./voti.txt") as file:
    for line in file:
        voto = line.rstrip()
        print(f"voto: {voto}")