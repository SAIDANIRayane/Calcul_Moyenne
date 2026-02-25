# student statistics utilities

def calcul_moyenne(liste_notes):
    """
    Calcule et retourne la moyenne d'une liste de notes.
    Retourne None si la liste est vide.
    """
    if not liste_notes:
        return None
    
    somme = 0
    for note in liste_notes:
        somme = somme + note
    
    moyenne = somme / len(liste_notes)
    return moyenne


def trouver_max(liste_notes):
    """
    Retourne la valeur maximale d'une liste.
    Retourne None si la liste est vide.
    """
    if not liste_notes:
        return None
    return max(liste_notes)


def min_value(liste_notes):
    """
    Retourne la valeur minimale d'une liste.
    Retourne None si la liste est vide.
    """
    if not liste_notes:
        return None

    minimum = liste_notes[0]
    for note in liste_notes:
        if note < minimum:
            minimum = note

    return minimum
