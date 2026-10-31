"""
Programma Calcolatore Matematica Acustica:
Calcolo delle quote geometriche costruttive dei 5 Solidi Platonici
a partire dalla frequenza di disturbo sonora.

Catena matematica deterministica:
1. Frequenza f [Hz] -> Velocita del suono c [m/s]
2. Lunghezza d'onda: lambda = c / f [m]
3. Diametro della sfera circoscritta: D_c = lambda / (2^n) [m]  (default n=0 -> D_c = lambda)
4. Formule inverse per ciascuno dei 5 Solidi Platonici:
   - Spigolo a
   - Altezza totale H
   - Sfera inscritta D_i
   - Sfera media D_m
   - Superficie totale facce S
   - Volume interno racchiuso V
   - Rapporto di dissipazione per attrito S/V
   - Angolo diedro tra le facce
"""

import argparse
import sys
from acustica import velocita_suono, lunghezza_onda
from geometria_solidi import SOLIDI_PLATONICI
from frattali_aperture import calcola_aperture_frattali


def calcola_solidi_da_frequenza(
    frequenza_hz: float,
    temperatura_c: float = None,
    ordine_armonico_n: int = 0,
    velocita_suono_ms: float = None,
    riferimento: str = "entrambi",
    ordine_frattale_k: int = None
) -> dict:
    """
    Esegue la catena di calcolo da frequenza a parametri costruttivi dei solidi.

    Parametri:
        frequenza_hz (float): Frequenza fondamentale f in Hertz.
        temperatura_c (float): Temperatura dell'aria in °C (opzionale).
        ordine_armonico_n (int): Ordine n di frazionamento armonica (default 0 -> D = lambda).
        velocita_suono_ms (float): Velocita del suono in m/s (se specificata, ha la precedenza).
        riferimento (str): "circoscritto", "inscritto" o "entrambi".

    Ritorna:
        dict: Dati della propagazione d'onda e liste delle schede tecniche dei 5 solidi.
    """
    if frequenza_hz <= 0:
        raise ValueError("La frequenza deve essere maggiore di zero.")
    if ordine_armonico_n < 0:
        raise ValueError("L'ordine armonico n deve essere un intero non negativo (>= 0).")

    # 1. Determinazione della velocita del suono c
    if velocita_suono_ms is not None:
        c = velocita_suono_ms
    elif temperatura_c is not None:
        c = velocita_suono(temperatura_c)
    else:
        c = 340.0  # Valore standard di riferimento acustico

    # 2. Lunghezza d'onda lambda = c / f
    lam = lunghezza_onda(frequenza_hz, c)

    # 3. Diametro della sfera di riferimento D_ref = lambda / (2^n)
    divisore = 2 ** ordine_armonico_n
    d_ref = lam / divisore

    # 4. Calcolo geometrico dei solidi per le modalita richieste
    solidi_circoscritti = []
    solidi_inscritti = []

    if riferimento in ("circoscritto", "entrambi"):
        for solido in SOLIDI_PLATONICI:
            dati = solido.calcola_da_dc(d_ref)
            if ordine_frattale_k is not None:
                dati["aperture_frattali"] = calcola_aperture_frattali(
                    nome_solido=solido.nome,
                    spigolo_solido_m=dati["spigolo_a_m"],
                    numero_facce=dati["facce"],
                    iterazione_k=ordine_frattale_k,
                    frequenza_hz=frequenza_hz
                )
            solidi_circoscritti.append(dati)

    if riferimento in ("inscritto", "entrambi"):
        for solido in SOLIDI_PLATONICI:
            dati = solido.calcola_da_di(d_ref)
            if ordine_frattale_k is not None:
                dati["aperture_frattali"] = calcola_aperture_frattali(
                    nome_solido=solido.nome,
                    spigolo_solido_m=dati["spigolo_a_m"],
                    numero_facce=dati["facce"],
                    iterazione_k=ordine_frattale_k,
                    frequenza_hz=frequenza_hz
                )
            solidi_inscritti.append(dati)

    return {
        "frequenza_hz": frequenza_hz,
        "temperatura_c": temperatura_c,
        "velocita_suono_ms": c,
        "lunghezza_onda_m": lam,
        "ordine_armonico_n": ordine_armonico_n,
        "divisore_2n": divisore,
        "diametro_riferimento_m": d_ref,
        "raggio_riferimento_m": d_ref / 2.0,
        "solidi_circoscritti": solidi_circoscritti,
        "solidi_inscritti": solidi_inscritti,
        "riferimento": riferimento,
        "ordine_frattale_k": ordine_frattale_k
    }


def _stampa_tabella_solidi(solidi: list, titolo_sezione: str, spiegazione: str):
    """Funzione ausiliaria di formattazione tabella per un set di solidi."""
    print("\n" + "-" * 95)
    print(f" {titolo_sezione.upper()}")
    print(f" {spiegazione}")
    print("-" * 95)
    header = (
        f"{'Solido':<12} | {'Spigolo (a)':<12} | {'Altezza (H)':<12} | "
        f"{'Sfera Insc.(Di)':<16} | {'Sfera Circ.(Dc)':<16} | {'Volume (V)':<10} | {'S/V [1/m]':<9}"
    )
    print(header)
    print("-" * 95)

    for s in solidi:
        riga = (
            f"{s['nome']:<12} | "
            f"{s['spigolo_a_m']*100:>8.2f} cm | "
            f"{s['altezza_h_m']*100:>8.2f} cm | "
            f"{s['diametro_inscritto_di_m']*100:>12.2f} cm | "
            f"{s['diametro_circoscritto_dc_m']*100:>12.2f} cm | "
            f"{s['volume_litri']:>7.2f} L | "
            f"{s['rapporto_s_v']:>9.2f}"
        )
        print(riga)


def visualizza_report(risultati: dict):
    """Stampa a schermo i risultati in modo ordinato e facilmente leggibile."""
    print("\n" + "=" * 95)
    print(" CALCOLATORE MATEMATICO ACUSTICA: PROGETTAZIONE DEI SOLIDI PLATONICI")
    print("=" * 95)
    print(f" [INPUT]  Frequenza target (f)           : {risultati['frequenza_hz']:.2f} Hz")
    temp_str = f"{risultati['temperatura_c']:.1f} °C" if risultati['temperatura_c'] is not None else "N/A (impostata c fissa)"
    print(f" [FISICA] Temperatura ambiente          : {temp_str}")
    print(f" [FISICA] Velocita del suono (c)        : {risultati['velocita_suono_ms']:.2f} m/s")
    print(f" [ONDA]   Lunghezza d'onda (lambda)     : {risultati['lunghezza_onda_m']:.4f} m  ({risultati['lunghezza_onda_m']*100:.2f} cm)")
    print(f" [SCALA]  Ordine armonico (n)           : {risultati['ordine_armonico_n']}  (Diametro = lambda / {risultati['divisore_2n']})")
    print(f" [SFERA]  Diametro di riferimento       : {risultati['diametro_riferimento_m']:.4f} m  ({risultati['diametro_riferimento_m']*100:.2f} cm)")
    print("=" * 95)

    if risultati["solidi_circoscritti"]:
        _stampa_tabella_solidi(
            risultati["solidi_circoscritti"],
            titolo_sezione="1. MODELLI CON SFERA CIRCOSCRITTA (D_c = lambda / 2^n)",
            spiegazione="La sfera tocca tutti gli SPIGOLI/VERTICI esterni (solido racchiuso nell'onda)."
        )

    if risultati["solidi_inscritti"]:
        _stampa_tabella_solidi(
            risultati["solidi_inscritti"],
            titolo_sezione="2. MODELLI CON SFERA INSCRITTA (D_i = lambda / 2^n)",
            spiegazione="La sfera tocca tutte le FACCE/PARETI interne (il solido racchiude l'intera onda tra le sue pareti)."
        )

    print("\n" + "=" * 95)
    print(" DETTAGLI COSTRUTTIVI E ANGOLI PER IL TAGLIO DEI PANNELLI / MODELLAZIONE 3D:")
    print("=" * 95)

    solidi_dettagli = risultati["solidi_circoscritti"] if risultati["solidi_circoscritti"] else risultati["solidi_inscritti"]
    for s in solidi_dettagli:
        print(f" * {s['nome'].upper()} ({s['facce']} facce - {s['forma_faccia']}):")
        print(f"     - Angolo diedro tra le facce per il taglio : {s['angolo_diedro_deg']:.2f}°")
        print(f"     - Indice di Sfericita (Wadell)            : {s['sfericita_psi']:.3f}")
        # Mostra lo spigolo sia per il modello circoscritto sia per quello inscritto
        if risultati["solidi_circoscritti"] and risultati["solidi_inscritti"]:
            s_circ = next(x for x in risultati["solidi_circoscritti"] if x["nome"] == s["nome"])
            s_insc = next(x for x in risultati["solidi_inscritti"] if x["nome"] == s["nome"])
            print(f"     - MODELLO CIRCOSCRITTO (Dc = {risultati['diametro_riferimento_m']*100:.1f} cm): Spigolo a = {s_circ['spigolo_a_m']*100:.2f} cm | H = {s_circ['altezza_h_m']*100:.2f} cm | Vol = {s_circ['volume_litri']:.2f} L | S/V = {s_circ['rapporto_s_v']:.2f} m⁻¹")
            print(f"     - MODELLO INSCRITTO    (Di = {risultati['diametro_riferimento_m']*100:.1f} cm): Spigolo a = {s_insc['spigolo_a_m']*100:.2f} cm | H = {s_insc['altezza_h_m']*100:.2f} cm | Vol = {s_insc['volume_litri']:.2f} L | S/V = {s_insc['rapporto_s_v']:.2f} m⁻¹")

    # Sezione dedicata alle aperture frattali se specificate
    k_ord = risultati.get("ordine_frattale_k")
    if k_ord is not None:
        print("\n" + "=" * 95)
        print(f" SPECIFICHE APERTURE FRATTALI DI SUPERFICIE (ORDINE FRATTALE k = {k_ord}):")
        print(f" L'aria entra attraverso fori auto-simili; il perimetro bagnato amplifica la dissipazione viscosa.")
        print("-" * 95)
        header_f = (
            f"{'Solido':<12} | {'Fori/Faccia':<11} | {'Fori Tot':<9} | {'Spigolo Foro':<14} | "
            f"{'Perimetro Totale':<17} | {'Porosita σ':<11} | {'Womersley s':<11}"
        )
        print(header_f)
        print("-" * 95)

        solidi_target = risultati["solidi_circoscritti"] if risultati["solidi_circoscritti"] else risultati["solidi_inscritti"]
        for s in solidi_target:
            ap = s.get("aperture_frattali")
            if ap:
                riga_f = (
                    f"{s['nome']:<12} | "
                    f"{ap['fori_per_faccia']:>11} | "
                    f"{ap['fori_totali_solido']:>9} | "
                    f"{ap['spigolo_foro_mm']:>11.2f} mm | "
                    f"{ap['perimetro_totale_forato_m']:>14.2f} m | "
                    f"{ap['porosita_superficiale_sigma']*100:>9.2f}% | "
                    f"{ap['parametro_womersley_s']:>11.1f}"
                )
                print(riga_f)
    print("=" * 95)


def main():
    parser = argparse.ArgumentParser(
        description="Calcolo quote costruttive dei Solidi Platonici a partire dalla frequenza sonora."
    )
    parser.add_argument(
        "-f", "--frequenza",
        type=float,
        help="Frequenza sonora in Hz (es. 120.0)"
    )
    parser.add_argument(
        "-t", "--temperatura",
        type=float,
        default=None,
        help="Temperatura ambiente in °C (calcola c termodinamica)"
    )
    parser.add_argument(
        "-c", "--velocita",
        type=float,
        default=None,
        help="Velocita di propagazione del suono in m/s (default: 340.0 m/s se non specificata temperatura)"
    )
    parser.add_argument(
        "-n", "--ordine",
        type=int,
        default=0,
        help="Ordine armonico di frazionamento n (default: 0 -> D_c = lambda; 1 -> lambda/2; 2 -> lambda/4)"
    )
    parser.add_argument(
        "-k", "--frattale",
        type=int,
        default=None,
        help="Ordine frattale delle aperture k (es. 1, 2, 3...) per forare e incanalare l'onda"
    )
    parser.add_argument(
        "-m", "--modo",
        choices=["entrambi", "circoscritto", "inscritto"],
        default="entrambi",
        help="Modalita di calcolo: 'circoscritto' (D_c=onda), 'inscritto' (D_i=onda), 'entrambi' (default)"
    )

    args = parser.parse_args()

    freq = args.frequenza
    if freq is None:
        try:
            valore_inserito = input("Inserisci la frequenza del suono da analizzare (in Hz): ").strip()
            freq = float(valore_inserito)
        except (ValueError, KeyboardInterrupt):
            print("\nValore non valido. Inserire un numero positivo per la frequenza.")
            sys.exit(1)

    if freq <= 0:
        print("Errore: la frequenza deve essere maggiore di zero.")
        sys.exit(1)

    risultati = calcola_solidi_da_frequenza(
        frequenza_hz=freq,
        temperatura_c=args.temperatura,
        ordine_armonico_n=args.ordine,
        velocita_suono_ms=args.velocita,
        riferimento=args.modo,
        ordine_frattale_k=args.frattale
    )

    visualizza_report(risultati)


if __name__ == "__main__":
    main()
