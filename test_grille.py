from ocean import Ocean


def test_grille():
    """Test de la classe Grille."""
    # Création d'une instance de la classe Grille
    ocean = Ocean(5, 5)

    # Vérification de la taille de la grille
    assert ocean.lignes == 5, "Le nombre de lignes doit être 5"
    assert ocean.colonnes == 5, "Le nombre de colonnes doit être 5"

    # Vérification que la grille est vide au départ
    for i in range(ocean.lignes):
        for j in range(ocean.colonnes):
            assert (
                ocean.grille[i][j] is None
            ), f"La cellule ({i}, {j}) ne doit pas contenir d'objet"

    print("Tous les tests de la classe Grille ont réussi.")
