from proie import Proie


def test_proie():
    """Test de la classe Proie."""
    la_proie = Proie(8)
    assert la_proie is not None
    assert la_proie.cycle_reproduction == 8
