"""
Test Regression: Verifica regressione per calcoli noti a 340 Hz e 120 Hz.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from calcolatore import calcola_solidi_da_frequenza


def test_regression_outputs():
    # Regression test at 340 Hz, c = 340 m/s, n = 0, k = 2
    res_340 = calcola_solidi_da_frequenza(
        frequenza_hz=340.0,
        velocita_suono_ms=340.0,
        ordine_armonico_n=0,
        riferimento="entrambi",
        ordine_frattale_k=2
    )

    assert abs(res_340["lunghezza_onda_m"] - 1.0) < 1e-14
    assert len(res_340["solidi_circoscritti"]) == 5
    assert len(res_340["solidi_inscritti"]) == 5

    # Check tetrahedron values
    tetra_c = res_340["solidi_circoscritti"][0]
    assert tetra_c["nome"] == "Tetraedro"
    assert abs(tetra_c["spigolo_a_m"] - 0.81649658) < 1e-6
    assert abs(tetra_c["volume_litri"] - 64.150029) < 1e-4

    # Check fractal apertures at k=2
    ap_tetra = tetra_c["aperture_frattali"]
    assert ap_tetra["fori_totali_solido"] == 12
    assert abs(ap_tetra["porosita_superficiale_sigma"] - 0.1875) < 1e-6

    print("test_regression.py: TEST DI REGRESSIONE PASSATI CON SUCCESSO.")


if __name__ == "__main__":
    test_regression_outputs()
