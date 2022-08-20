paises = ['Alemanha','Argentina', 'Bélgica', 'Brasil', 'Costa Rica', 'Colômbia', 'França', 'Holanda']
i = 0

while i < len(paises):
    for vice in paises:
        if paises[i] != vice:
            print("Campeao: " + paises[i] + " | Vice: " + vice)
    i = i + 1   