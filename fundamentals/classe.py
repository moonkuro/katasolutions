def better_than_average(class_points, your_points):
    tamanhoLista = len(class_points)
    somaClasse = 0
    
    for n in class_points:
        somaClasse += n
    mediaClasse = int(somaClasse / tamanhoLista)

    if your_points > mediaClasse:
        return True
    else:
        return False