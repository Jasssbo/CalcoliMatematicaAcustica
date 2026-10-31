"""
Test Geometry: Verifica formale della geometria analitica dei solidi platonici.
"""

import sys
import os
import math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from geometria_solidi import SOLIDI_PLATONICI


def test_geometric_invariants():
    d_ref = 1.0  # 1 metro

    for solido in SOLIDI_PLATONICI:
        # 1. Modello circoscritto
        dc_data = solido.calcola_da_dc(d_ref)
        assert abs(dc_data["diametro_circoscritto_dc_m"] - 1.0) < 1e-14
        assert dc_data["volume_m3"] > 0
        assert dc_data["superficie_m2"] > 0
        assert 0 < dc_data["sfericita_psi"] <= 1.0

        # 2. Modello inscritto
        di_data = solido.calcola_da_di(d_ref)
        assert abs(di_data["diametro_inscritto_di_m"] - 1.0) < 1e-14
        # Teorema S/V = 6 / D_i per D_i = 1 m -> S/V deve essere esattamente 6.0
        assert abs(di_data["rapporto_s_v"] - 6.0) < 1e-12, f"Errore su {solido.nome}"

    print("test_geometry.py: TUTTI I TEST GEOMETRICI PASSATI.")


if __name__ == "__main__":
    test_geometric_invariants()
