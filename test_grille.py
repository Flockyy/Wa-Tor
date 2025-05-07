from grille import Grille


def test_grille():
    """Test de la classe Grille."""
    # Création d'une instance de la classe Grille
    grille = Grille(5, 5)

    # Vérification de la taille de la grille
    assert grille.lignes == 5, "Le nombre de lignes doit être 5"
    assert grille.colonnes == 5, "Le nombre de colonnes doit être 5"

    # Vérification que la grille est vide au départ
    for i in range(grille.lignes):
        for j in range(grille.colonnes):
            assert (
                grille.grille[i][j] is None
            ), f"La cellule ({i}, {j}) ne doit pas contenir d'objet"

    print("Tous les tests de la classe Grille ont réussi.")
