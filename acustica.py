"""
Modulo Acustica: Formule di fisica acustica e teoria del risuonatore di Helmholtz.

Fornisce definizioni analitiche rigorose per la propagazione ondulatoria,
il calcolo della velocità del suono in funzione della temperatura e il
dimensionamento inverso delle cavità risonanti.
"""

import math


def velocita_suono(temperatura_c: float = 20.0) -> float:
    """
    Calcola la velocità del suono nell'aria secca in funzione della temperatura.
    Formula basata sull'equazione dei gas ideali:
        c(T) = sqrt(gamma * R_aria * T_kelvin)
    Approssimazione standard:
        c(T) = 331.3 * sqrt(1 + T_celsius / 273.15)

    Parametri:
        temperatura_c (float): Temperatura ambiente in gradi Celsius (default: 20.0 °C).

    Ritorna:
        float: Velocità del suono c in metri al secondo (m/s).
    """
    t_kelvin = 273.15 + temperatura_c
    if t_kelvin <= 0:
        raise ValueError("La temperatura deve essere superiore allo zero assoluto.")
    # gamma = 1.40 (rapporto calori specifici), R = 287.05 J/(kg*K)
    gamma = 1.40
    r_aria = 287.05
    return math.sqrt(gamma * r_aria * t_kelvin)


def lunghezza_onda(frequenza: float, c: float) -> float:
    """
    Calcola la lunghezza d'onda acustica:
        lambda = c / f

    Parametri:
        frequenza (float): Frequenza fondamentale f in Hertz (Hz).
        c (float): Velocità del suono in metri al secondo (m/s).

    Ritorna:
        float: Lunghezza d'onda lambda in metri (m).
    """
    if frequenza <= 0:
        raise ValueError("La frequenza deve essere strettamente positiva.")
    return c / frequenza


def frequenza_helmholtz(
    volume_cavita: float,
    raggio_apertura: float,
    spessore_parete: float,
    c: float,
    flangia_interna: bool = True,
    flangia_esterna: bool = False
) -> float:
    """
    Calcola la frequenza di risonanza fondamentale di una cavità di Helmholtz:
        f_0 = (c / (2 * pi)) * sqrt(S_a / (V * L_eff))

    dove:
        S_a = pi * r_a^2
        L_eff = t + delta_L  (lunghezza effettiva corretta)
        delta_L = correzione di fine corsa acustica (Rayleigh / Ingard).
                  delta_L ≈ (0.85 + 0.61) * r_a = 1.46 * r_a (parete interna flangiata, esterna libera)
                  oppure ≈ 1.60 * r_a (entrambe le estremità flangiate).

    Parametri:
        volume_cavita (float): Volume interno V della cavità in metri cubi (m^3).
        raggio_apertura (float): Raggio dell'orifizio circolare r_a in metri (m).
        spessore_parete (float): Lunghezza geometrica del collo / spessore t in metri (m).
        c (float): Velocità del suono in m/s.
        flangia_interna (bool): Se l'apertura interna ha flangia (default True).
        flangia_esterna (bool): Se l'apertura esterna ha flangia (default False).

    Ritorna:
        float: Frequenza di risonanza f_0 in Hertz (Hz).
    """
    if volume_cavita <= 0 or raggio_apertura <= 0 or spessore_parete <= 0:
        raise ValueError("Volume, raggio dell'apertura e spessore devono essere maggiori di zero.")

    area_apertura = math.pi * (raggio_apertura ** 2)

    # Coefficiente di correzione di fine corsa (end-correction factor)
    coeff_in = 0.85 if flangia_interna else 0.61
    coeff_out = 0.85 if flangia_esterna else 0.61
    delta_l = (coeff_in + coeff_out) * raggio_apertura

    l_eff = spessore_parete + delta_l

    f_0 = (c / (2.0 * math.pi)) * math.sqrt(area_apertura / (volume_cavita * l_eff))
    return f_0


def dimensione_apertura_helmholtz(
    frequenza_target: float,
    volume_cavita: float,
    spessore_parete: float,
    c: float,
    coeff_correzione: float = 1.46
) -> dict:
    """
    Risoluzione analitica inversa dell'equazione di Helmholtz.
    Data la frequenza target f_0, il volume della cavità V e lo spessore parete t,
    determina esattamente il raggio r_a dell'apertura circolare richiesta:

        f_0 = (c / 2pi) * sqrt( pi * r_a^2 / (V * (t + coeff * r_a)) )

    Posto k_0 = 2 * pi * f_0 / c:
        k_0^2 * V * (t + coeff * r_a) = pi * r_a^2
        pi * r_a^2 - (coeff * k_0^2 * V) * r_a - (k_0^2 * V * t) = 0

    Risolta tramite formula quadratica:
        A * r_a^2 + B * r_a + C = 0
        r_a = (-B + sqrt(B^2 - 4*A*C)) / (2*A)

    Parametri:
        frequenza_target (float): Frequenza desiderata f_0 (Hz).
        volume_cavita (float): Volume interno V (m^3).
        spessore_parete (float): Spessore della parete t (m).
        c (float): Velocità del suono (m/s).
        coeff_correzione (float): delta_L / r_a (tipicamente 1.46 - 1.60).

    Ritorna:
        dict: {
            'raggio_apertura_m': float,
            'diametro_apertura_mm': float,
            'area_apertura_cm2': float,
            'lunghezza_effettiva_mm': float
        }
    """
    k_0 = (2.0 * math.pi * frequenza_target) / c
    k0_sq_v = (k_0 ** 2) * volume_cavita

    a_quad = math.pi
    b_quad = -coeff_correzione * k0_sq_v
    c_quad = -k0_sq_v * spessore_parete

    discriminante = (b_quad ** 2) - (4.0 * a_quad * c_quad)
    if discriminante < 0:
        raise ValueError("Impossibile trovare una soluzione reale per l'apertura con questi parametri.")

    r_a = (-b_quad + math.sqrt(discriminante)) / (2.0 * a_quad)
    l_eff = spessore_parete + (coeff_correzione * r_a)
    area = math.pi * (r_a ** 2)

    return {
        "raggio_apertura_m": r_a,
        "diametro_apertura_mm": (2.0 * r_a) * 1000.0,
        "area_apertura_cm2": area * 10000.0,
        "lunghezza_effettiva_mm": l_eff * 1000.0,
    }
