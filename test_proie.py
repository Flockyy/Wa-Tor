from proie import Proie

def test_proie():
    """Test de la classe Proie."""
    la_proie = Proie(8)
    assert la_proie is not None
    assert la_proie.cycle_reproduction == 8
    assert la_proie.caractere_symbole() == "P"
    assert str(la_proie) == "Proie ayant un cycle de reproduction de 8 tours"
    
def test_proie_reproduction():
    """Test de la reproduction de la classe Proie."""
    la_proie = Proie(1)
    assert la_proie.reproduction() == False
    for _ in range(1, 6):
        la_proie.vieillisement()
        assert la_proie.reproduction() == False
    la_proie.vieillisement()
    assert la_proie.reproduction() == True
    assert la_proie.gestion_reproduction() is not None
    assert isinstance(la_proie.gestion_reproduction(), Proie)
    assert str(la_proie.gestion_reproduction()) == "Proie ayant un cycle de reproduction de 1 tours"