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


class_points = [30,40,60,70,90]
your_points = 50
better_than_average(class_points, your_points)
