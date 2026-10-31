"""
Test Physical Invariants: Verifica di coerenza fisica e termodinamica.
"""

import sys
import os
import math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from acustica import velocita_suono, lunghezza_onda
from frattali_aperture import spessore_strato_limite_viscoso


def test_physical_bounds():
    # 1. Velocita del suono: monotonically increasing with temperature
    c_0 = velocita_suono(0.0)
    c_20 = velocita_suono(20.0)
    c_40 = velocita_suono(40.0)
    assert c_0 < c_20 < c_40
    assert 330.0 < c_0 < 333.0
    assert 342.0 < c_20 < 345.0

    # 2. Lunghezza d'onda: inversely proportional to frequency
    lam_100 = lunghezza_onda(100.0, c_20)
    lam_200 = lunghezza_onda(200.0, c_20)
    assert abs(lam_100 - 2.0 * lam_200) < 1e-12

    # 3. Strato limite viscoso: scales as 1 / sqrt(omega)
    delta_100 = spessore_strato_limite_viscoso(100.0)
    delta_400 = spessore_strato_limite_viscoso(400.0)
    assert abs(delta_100 - 2.0 * delta_400) < 1e-6
    # A frequenze udibili deve essere dell'ordine dei decimi di millimetro
    assert 0.05e-3 < delta_100 < 0.5e-3

    print("test_physical_invariants.py: TUTTI GLI INVARIANTI FISICI PASSATI.")


if __name__ == "__main__":
    test_physical_bounds()
