"""
Modulo Frattali Aperture: Modellazione geometrica e acustica delle aperture
derivate da suddivisioni frattali sulle facce dei Solidi Platonici.

Formalizza la rimozione di sotto-facce auto-simili per ordini frattali k >= 1:
- Facce triangolari (Tetraedro, Ottaedro, Icosaedro): Sierpinski Gasket diadico (scala 1/2^k)
- Facce quadrate (Cubo): Sierpinski Carpet triadico (scala 1/3^k)
- Facce pentagonali (Dodecaedro): Pentaflake regolare aureo (scala 1/phi^(2k))

Fornisce quote costruttive, perimetri dissipativi, porosita ed equivalenze termo-viscose.
"""

import math
from typing import Dict, Any

# Costante aurea
PHI = (1.0 + math.sqrt(5.0)) / 2.0


def spessore_strato_limite_viscoso(frequenza_hz: float, c: float = 340.0) -> float:
    """
    Calcola lo spessore dello strato limite viscoso dell'aria:
        delta_v = sqrt(2 * mu / (rho_0 * omega))
    in aria standard a 20°C (mu = 1.81e-5 Pa*s, rho_0 = 1.204 kg/m^3).
    """
    if frequenza_hz <= 0:
        raise ValueError("La frequenza deve essere maggiore di zero.")
    omega = 2.0 * math.pi * frequenza_hz
    mu = 1.81e-5
    rho_0 = 1.204
    return math.sqrt((2.0 * mu) / (rho_0 * omega))


def calcola_aperture_frattali(
    nome_solido: str,
    spigolo_solido_m: float,
    numero_facce: int,
    iterazione_k: int,
    frequenza_hz: float = 340.0
) -> Dict[str, Any]:
    """
    Calcola le proprieta geometriche e termo-viscose delle aperture frattali
    generate sulla superficie del solido all'iterazione k.

    Parametri:
        nome_solido: Nome del solido platonico.
        spigolo_solido_m: Lunghezza dello spigolo nominale del solido a (m).
        numero_facce: Numero totale di facce del solido (4, 6, 8, 12, 20).
        iterazione_k: Ordine frattale di apertura k (intero >= 1).
        frequenza_hz: Frequenza target dell'onda (Hz).

    Ritorna:
        Dizionario con metriche geometriche, perimetri, aree, porosita e parametri viscosi.
    """
    if iterazione_k < 1:
        raise ValueError("L'ordine frattale di apertura k deve essere >= 1.")
    if spigolo_solido_m <= 0:
        raise ValueError("Lo spigolo del solido deve essere maggiore di zero.")

    delta_v = spessore_strato_limite_viscoso(frequenza_hz)

    # 1. Facce triangolari equilatere (Tetraedro, Ottaedro, Icosaedro)
    if nome_solido in ("Tetraedro", "Ottaedro", "Icosaedro"):
        tipo_apertura = "Triangolo equilatero (Sierpinski)"
        # All'ordine k, lo spigolo del foro si dimezza k volte
        spigolo_foro = spigolo_solido_m / (2.0 ** iterazione_k)
        # Numero di fori generati per faccia
        fori_per_faccia = 3 ** (iterazione_k - 1)
        perimetro_singolo = 3.0 * spigolo_foro
        area_singola = (math.sqrt(3.0) / 4.0) * (spigolo_foro ** 2)
        area_faccia_nominale = (math.sqrt(3.0) / 4.0) * (spigolo_solido_m ** 2)

    # 2. Facce quadrate (Cubo)
    elif nome_solido == "Cubo":
        tipo_apertura = "Quadrato (Sierpinski Carpet)"
        # Nella tassellazione classica di Sierpinski carpet, la suddivisione e triadica
        spigolo_foro = spigolo_solido_m / (3.0 ** iterazione_k)
        fori_per_faccia = 8 ** (iterazione_k - 1)
        perimetro_singolo = 4.0 * spigolo_foro
        area_singola = spigolo_foro ** 2
        area_faccia_nominale = spigolo_solido_m ** 2

    # 3. Facce pentagonali regolari (Dodecaedro)
    elif nome_solido == "Dodecaedro":
        tipo_apertura = "Pentagono regolare (Pentaflake aureo)"
        # Scala aurea concentrica: fattore phi^(2k)
        spigolo_foro = spigolo_solido_m / (PHI ** (2.0 * iterazione_k))
        # Concentrico centrale: 1 foro pentagonale principale all'ordine 1, 5 all'ordine 2, etc.
        fori_per_faccia = 5 ** (iterazione_k - 1)
        perimetro_singolo = 5.0 * spigolo_foro
        coeff_area_pent = 0.25 * math.sqrt(5.0 * (5.0 + 2.0 * math.sqrt(5.0)))
        area_singola = coeff_area_pent * (spigolo_foro ** 2)
        area_faccia_nominale = coeff_area_pent * (spigolo_solido_m ** 2)

    else:
        raise ValueError(f"Solido non supportato: {nome_solido}")

    # Totali su tutto il solido
    fori_totali_solido = fori_per_faccia * numero_facce
    area_totale_forata = area_singola * fori_totali_solido
    perimetro_totale_forato = perimetro_singolo * fori_totali_solido
    superficie_totale_nominale = area_faccia_nominale * numero_facce

    # Porosita / Rapporto di perforazione sigma = A_fori / A_nominale
    porosita_sigma = area_totale_forata / superficie_totale_nominale

    # Raggio idraulico equivalente r_h = 2 * A / P
    raggio_idraulico_m = (2.0 * area_singola) / perimetro_singolo

    # Numero adimensionale di Womersley/Stokes s = r_h / delta_v
    # Se s < 10, la viscosita domina fortemente su tutta la sezione del foro
    parametro_womersley = raggio_idraulico_m / delta_v

    # Rapporto perimetro/area del singolo foro (indice di efficienza dissipativa perimetrale)
    rapporto_p_a = perimetro_singolo / area_singola

    return {
        "solido": nome_solido,
        "iterazione_k": iterazione_k,
        "tipo_apertura": tipo_apertura,
        "spigolo_foro_m": spigolo_foro,
        "spigolo_foro_mm": spigolo_foro * 1000.0,
        "fori_per_faccia": fori_per_faccia,
        "fori_totali_solido": fori_totali_solido,
        "area_singolo_foro_mm2": area_singola * 1e6,
        "perimetro_singolo_foro_mm": perimetro_singolo * 1000.0,
        "area_totale_forata_cm2": area_totale_forata * 10000.0,
        "perimetro_totale_forato_m": perimetro_totale_forato,
        "porosita_superficiale_sigma": porosita_sigma,
        "raggio_idraulico_mm": raggio_idraulico_m * 1000.0,
        "spessore_strato_viscoso_delta_v_mm": delta_v * 1000.0,
        "parametro_womersley_s": parametro_womersley,
        "rapporto_perimetro_area_m_inv": rapporto_p_a,
    }
