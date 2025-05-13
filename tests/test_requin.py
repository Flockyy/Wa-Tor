from requin import Requin

def test_requin():
    """Test de la classe Requin."""
    le_requin = Requin(10, 6)
    assert le_requin is not None
    assert le_requin.points_energie == 6
    assert le_requin.cycle_reproduction == 10
    #assert le_requin.__points_par_repas == 3