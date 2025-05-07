from monde import Monde
from requin import Requin
from proie import Proie


def test_monde():
    """Test de la classe Monde."""
    # Création d'une instance de la classe Monde
    monde = Monde(5, 5)

    # Vérification de la taille de la grille
    assert monde.lignes == 5, "Le nombre de lignes doit être 5"
    assert monde.colonnes == 5, "Le nombre de colonnes doit être 5"

    # Vérification que la grille est vide au départ

    for i in range(monde.lignes):
        for j in range(monde.colonnes):
            assert (
                monde.grille.grille[i][j] is None
            ), f"La cellule ({i}, {j}) ne doit pas contenir d'objet"

    # Création de poissons et requins

    proies = [Proie() for _ in range(3)]
    requins = [Requin() for _ in range(2)]

    # Placement des proies et requins dans la grille

    monde.placer_poissons(proies, requins)

    # Vérification que les proies et requins sont placés dans la grille

    for proie in proies:
        found = False
        for i in range(monde.lignes):
            for j in range(monde.colonnes):
                if monde.grille.grille[i][j] == proie:
                    found = True
                    break
            if found:
                break
        assert found, f"La proie {proie} n'a pas été placée dans la grille"

    for requin in requins:
        found = False
        for i in range(monde.lignes):
            for j in range(monde.colonnes):
                if monde.grille.grille[i][j] == requin:
                    found = True
                    break
            if found:
                break
        assert found, f"Le requin {requin} n'a pas été placé dans la grille"

    # Vérification que les cellules sont vides après le placement
    for i in range(monde.lignes):
        for j in range(monde.colonnes):
            if monde.grille.grille[i][j] is not None:
                assert isinstance(
                    monde.grille.grille[i][j], (Proie, Requin)
                ), f"La cellule ({i}, {j}) doit contenir un poisson ou un requin"

    # Vérification que le nombre de poissons et requins est correct
    assert len(proies) == 3, "Le nombre de proies doit être 3"
    assert len(requins) == 2, "Le nombre de requins doit être 2"
