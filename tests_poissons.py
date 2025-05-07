from poisson import Poisson
from proie import Proie
from requin import Requin

def test_poisson():
    """Test de la classe Poisson."""
    le_poisson = Poisson(10)
    assert le_poisson is not None
    assert le_poisson.cycle_reproduction == 10