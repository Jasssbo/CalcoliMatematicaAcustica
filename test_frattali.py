"""
Test numerico indipendente per le aperture frattali sui Solidi Platonici.
Verifica la convergenza geometrica e la legge di scala del perimetro dissipativo.
"""

from acustica import lunghezza_onda
from geometria_solidi import SOLIDI_PLATONICI
from frattali_aperture import calcola_aperture_frattali, spessore_strato_limite_viscoso


def test_scala_frattale():
    freq = 340.0
    c = 340.0
    lam = lunghezza_onda(freq, c)  # 1.0 m
    delta_v = spessore_strato_limite_viscoso(freq, c)

    print(f"=== TEST APERTURE FRATTALI (f = {freq} Hz, lambda = {lam:.2f} m) ===")
    print(f"Spessore strato limite viscoso aria delta_v = {delta_v*1000:.3f} mm\n")

    # Test per il Tetraedro a diverse iterazioni k (1, 2, 3)
    solido_tetra = SOLIDI_PLATONICI[0]  # Tetraedro
    dati_tetra = solido_tetra.calcola_da_dc(lam)
    a_tetra = dati_tetra["spigolo_a_m"]

    print(f"TETRAEDRO (Spigolo solido a = {a_tetra*100:.2f} cm):")
    perimetri = []
    raggi_idraulici = []

    for k in (1, 2, 3, 4):
        ap = calcola_aperture_frattali(
            nome_solido="Tetraedro",
            spigolo_solido_m=a_tetra,
            numero_facce=4,
            iterazione_k=k,
            frequenza_hz=freq
        )
        perimetri.append(ap["perimetro_totale_forato_m"])
        raggi_idraulici.append(ap["raggio_idraulico_mm"])
        print(
            f"  Iterazione k={k}: Fori totali={ap['fori_totali_solido']:<4} | "
            f"Spigolo foro={ap['spigolo_foro_mm']:>7.2f} mm | "
            f"Perimetro tot={ap['perimetro_totale_forato_m']:>6.2f} m | "
            f"Raggio idraulico r_h={ap['raggio_idraulico_mm']:>6.2f} mm | "
            f"Womersley s={ap['parametro_womersley_s']:>6.1f} | "
            f"Porosita sigma={ap['porosita_superficiale_sigma']*100:>5.2f}%"
        )

    # Verifiche formali:
    # 1. Il perimetro totale deve crescere ad ogni iterazione
    for i in range(len(perimetri) - 1):
        assert perimetri[i+1] > perimetri[i], f"Errore: il perimetro deve crescere con k!"

    # 2. Il raggio idraulico deve dimezzarsi ad ogni iterazione (per triangoli r_h = a / (2*sqrt(3)))
    for i in range(len(raggi_idraulici) - 1):
        ratio = raggi_idraulici[i] / raggi_idraulici[i+1]
        assert abs(ratio - 2.0) < 1e-10, f"Errore: il raggio idraulico deve dimezzare, ottenuto {ratio}"

    print("\n--> TEST MATEMATICO DELLE APERTURE FRATTALI SUPERATO CON SUCCESSO <--")


if __name__ == "__main__":
    test_scala_frattale()
