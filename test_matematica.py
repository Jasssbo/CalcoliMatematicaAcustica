"""
Test di verifica matematica per le formule dei Solidi Platonici.
Controlla la consistenza bidirezionale (formule dirette <-> inverse).
"""

import math
from acustica import velocita_suono, lunghezza_onda
from geometria_solidi import SOLIDI_PLATONICI, Tetraedro, Cubo, Ottaedro, Dodecaedro, Icosaedro


def test_coerenza_matematica():
    # Test di riferimento: f = 340.0 Hz, c = 340.0 m/s -> lambda = 1.0 m esatto
    freq = 340.0
    c = 340.0
    lam = lunghezza_onda(freq, c)
    d_onda = lam  # Ordine 0 -> 1.0 m esatto

    print(f"=== TEST CON VALORI DI RIFERIMENTO ===")
    print(f"Frequenza f = {freq} Hz")
    print(f"Velocita del suono c = {c} m/s")
    print(f"Lunghezza d'onda lambda = {lam:.4f} m (esattamente 1 metro)\n")

    tutti_superati = True

    # 1. VERIFICA MODELLO A SFERA CIRCOSCRITTA (D_c = lambda = 1.0 m)
    print("--- 1. MODELLO SFERA CIRCOSCRITTA (D_c = 1.0 m, tocca gli spigoli/vertici) ---")
    for solido in SOLIDI_PLATONICI:
        dati = solido.calcola_da_dc(d_onda)
        a = dati["spigolo_a_m"]
        r_c = dati["raggio_circoscritto_rc_m"]

        if solido.nome == "Tetraedro":
            r_c_check = a * math.sqrt(6.0) / 4.0
        elif solido.nome == "Cubo":
            r_c_check = a * math.sqrt(3.0) / 2.0
        elif solido.nome == "Ottaedro":
            r_c_check = a * math.sqrt(2.0) / 2.0
        elif solido.nome == "Dodecaedro":
            r_c_check = a * (math.sqrt(3.0) * (1.0 + math.sqrt(5.0))) / 4.0
        elif solido.nome == "Icosaedro":
            r_c_check = a * math.sqrt(10.0 + 2.0 * math.sqrt(5.0)) / 4.0

        err = abs(r_c_check - r_c)
        ok = err < 1e-12
        if not ok:
            tutti_superati = False
        print(f"[{'OK' if ok else 'FAIL'}] {solido.nome:<12}: a={a*100:.2f}cm, Di={dati['diametro_inscritto_di_m']*100:.2f}cm, V={dati['volume_litri']:.2f}L")

    # 2. VERIFICA MODELLO A SFERA INSCRITTA (D_i = lambda = 1.0 m)
    print("\n--- 2. MODELLO SFERA INSCRITTA (D_i = 1.0 m, tocca le facce/pareti interne) ---")
    for solido in SOLIDI_PLATONICI:
        dati_i = solido.calcola_da_di(d_onda)
        a_i = dati_i["spigolo_a_m"]
        r_i = dati_i["raggio_inscritto_ri_m"]

        if solido.nome == "Tetraedro":
            r_i_check = a_i * math.sqrt(6.0) / 12.0
        elif solido.nome == "Cubo":
            r_i_check = a_i / 2.0
        elif solido.nome == "Ottaedro":
            r_i_check = a_i * math.sqrt(6.0) / 6.0
        elif solido.nome == "Dodecaedro":
            coeff_ri = 0.5 * math.sqrt((25.0 + 11.0 * math.sqrt(5.0)) / 10.0)
            r_i_check = a_i * coeff_ri
        elif solido.nome == "Icosaedro":
            r_i_check = a_i * (math.sqrt(3.0) * (3.0 + math.sqrt(5.0))) / 12.0

        err_i = abs(r_i_check - r_i)
        ok_i = err_i < 1e-12
        if not ok_i:
            tutti_superati = False
        print(f"[{'OK' if ok_i else 'FAIL'}] {solido.nome:<12}: a={a_i*100:.2f}cm, Dc={dati_i['diametro_circoscritto_dc_m']*100:.2f}cm, V={dati_i['volume_litri']:.2f}L")

    if tutti_superati:
        print("\n--> TUTTE LE FORMULE MATEMATICHE (CIRCOSCRITTE E INSCRITTE) SONO ESATTE AL 100% <--")
    else:
        print("\n--> ATTENZIONE: ALCUNE FORMULE HANNO DISCREPANZE <--")


if __name__ == "__main__":
    test_coerenza_matematica()
