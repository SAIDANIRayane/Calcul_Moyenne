# student statistics utilities

def CalculMoyenne(ListeNotes):
    somme=0
    for n in ListeNotes:
        somme=somme+n
    moyenne=somme/len(ListeNotes)
    return moyenne


def trouverMax(listeNotes):
    if listeNotes==[]:
        return None
    return max(listeNotes)


def min_value(notes):
    minimum = notes[0]
    for i in notes:
        if i<minimum:
            minimum=i
    return minimum