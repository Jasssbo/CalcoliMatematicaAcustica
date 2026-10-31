"""
Modulo Geometria Solidi: Proprietà analitiche dei 5 Solidi Platonici.

Formule matematiche chiuse e inverse:
Dato il raggio della sfera circoscritta R_c (o diametro D_c = 2 * R_c),
calcola esattamente:
- Spigolo del solido (a)
- Raggio e diametro della sfera inscritta (R_i, D_i)
- Raggio della sfera media tangente agli spigoli (R_m)
- Altezza d'ingombro (H)
- Superficie totale delle facce (S)
- Volume interno racchiuso (V)
- Rapporto Superficie/Volume (S/V)
- Angolo diedro tra due facce adiacenti (theta)
- Indice di Sfericità (Wadell)
"""

import math
from typing import Dict, Any


class SolidoPlatonico:
    """Classe base per un solido platonico regolare."""

    def __init__(self, nome: str, facce: int, vertici: int, spigoli: int, forma_faccia: str):
        self.nome = nome
        self.facce = facce
        self.vertici = vertici
        self.spigoli = spigoli
        self.forma_faccia = forma_faccia

    @staticmethod
    def sfericita(volume: float, superficie: float) -> float:
        """
        Indice di sfericita di Wadell (1935):
            Psi = (pi^(1/3) * (6 * V)^(2/3)) / S
        Per una sfera ideale Psi = 1.0.
        """
        return (math.pi ** (1.0 / 3.0)) * ((6.0 * volume) ** (2.0 / 3.0)) / superficie


class Tetraedro(SolidoPlatonico):
    """
    Tetraedro regolare:
    - 4 facce triangolari equilatere
    - 4 vertici
    - 6 spigoli
    - Angolo diedro: arccos(1/3) ≈ 70.5288°
    """

    def __init__(self):
        super().__init__("Tetraedro", facce=4, vertici=4, spigoli=6, forma_faccia="Triangolo equilatero")
        self.angolo_diedro_deg = math.degrees(math.acos(1.0 / 3.0))

    def calcola_da_dc(self, d_c: float) -> Dict[str, Any]:
        """
        Calcola tutte le quote a partire dal diametro della sfera circoscritta D_c (tocca i 4 vertici).
        Formula inversa per lo spigolo:
            R_c = a * sqrt(6) / 4  ==>  a = (4 * R_c) / sqrt(6) = D_c * sqrt(6) / 3
        """
        r_c = d_c / 2.0
        spigolo = (4.0 * r_c) / math.sqrt(6.0)
        return self._costruisci_proprieta(spigolo, modo="circoscritto", d_ref=d_c)

    def calcola_da_di(self, d_i: float) -> Dict[str, Any]:
        """
        Calcola tutte le quote a partire dal diametro della sfera inscritta D_i (tangente alle 4 facce).
        Formula inversa per lo spigolo:
            R_i = a * sqrt(6) / 12  ==>  a = 12 * R_i / sqrt(6) = 2 * sqrt(6) * R_i = sqrt(6) * D_i
        """
        r_i = d_i / 2.0
        spigolo = math.sqrt(6.0) * d_i
        return self._costruisci_proprieta(spigolo, modo="inscritto", d_ref=d_i)

    def _costruisci_proprieta(self, spigolo: float, modo: str, d_ref: float) -> Dict[str, Any]:
        r_c = spigolo * math.sqrt(6.0) / 4.0
        d_c = 2.0 * r_c
        r_i = spigolo * math.sqrt(6.0) / 12.0
        d_i = 2.0 * r_i
        r_m = spigolo * math.sqrt(2.0) / 4.0
        altezza_h = spigolo * math.sqrt(6.0) / 3.0  # Vertice - faccia opposta
        superficie = math.sqrt(3.0) * (spigolo ** 2)
        volume = (math.sqrt(2.0) / 12.0) * (spigolo ** 3)

        return {
            "nome": self.nome,
            "facce": self.facce,
            "forma_faccia": self.forma_faccia,
            "modo_riferimento": modo,
            "diametro_riferimento_m": d_ref,
            "spigolo_a_m": spigolo,
            "altezza_h_m": altezza_h,
            "diametro_circoscritto_dc_m": d_c,
            "raggio_circoscritto_rc_m": r_c,
            "diametro_inscritto_di_m": d_i,
            "raggio_inscritto_ri_m": r_i,
            "raggio_medio_rm_m": r_m,
            "superficie_m2": superficie,
            "volume_m3": volume,
            "volume_litri": volume * 1000.0,
            "rapporto_s_v": superficie / volume,
            "angolo_diedro_deg": self.angolo_diedro_deg,
            "sfericita_psi": self.sfericita(volume, superficie),
        }


class Cubo(SolidoPlatonico):
    """
    Cubo / Esaedro regolare:
    - 6 facce quadrate
    - 8 vertici
    - 12 spigoli
    - Angolo diedro: 90.0°
    """

    def __init__(self):
        super().__init__("Cubo", facce=6, vertici=8, spigoli=12, forma_faccia="Quadrato")
        self.angolo_diedro_deg = 90.0

    def calcola_da_dc(self, d_c: float) -> Dict[str, Any]:
        """
        Calcola tutte le quote a partire dal diametro della sfera circoscritta D_c (tocca gli 8 vertici).
        Formula inversa per lo spigolo:
            R_c = a * sqrt(3) / 2  ==>  a = (2 * R_c) / sqrt(3) = D_c / sqrt(3)
        """
        r_c = d_c / 2.0
        spigolo = (2.0 * r_c) / math.sqrt(3.0)
        return self._costruisci_proprieta(spigolo, modo="circoscritto", d_ref=d_c)

    def calcola_da_di(self, d_i: float) -> Dict[str, Any]:
        """
        Calcola tutte le quote a partire dal diametro della sfera inscritta D_i (tangente alle 6 facce).
        Formula inversa per lo spigolo:
            R_i = a / 2  ==>  a = 2 * R_i = D_i
        """
        spigolo = d_i
        return self._costruisci_proprieta(spigolo, modo="inscritto", d_ref=d_i)

    def _costruisci_proprieta(self, spigolo: float, modo: str, d_ref: float) -> Dict[str, Any]:
        r_c = spigolo * math.sqrt(3.0) / 2.0
        d_c = 2.0 * r_c
        r_i = spigolo / 2.0
        d_i = 2.0 * r_i
        r_m = spigolo * math.sqrt(2.0) / 2.0
        altezza_h = spigolo  # Distanza tra facce opposte
        superficie = 6.0 * (spigolo ** 2)
        volume = spigolo ** 3

        return {
            "nome": self.nome,
            "facce": self.facce,
            "forma_faccia": self.forma_faccia,
            "modo_riferimento": modo,
            "diametro_riferimento_m": d_ref,
            "spigolo_a_m": spigolo,
            "altezza_h_m": altezza_h,
            "diametro_circoscritto_dc_m": d_c,
            "raggio_circoscritto_rc_m": r_c,
            "diametro_inscritto_di_m": d_i,
            "raggio_inscritto_ri_m": r_i,
            "raggio_medio_rm_m": r_m,
            "superficie_m2": superficie,
            "volume_m3": volume,
            "volume_litri": volume * 1000.0,
            "rapporto_s_v": superficie / volume,
            "angolo_diedro_deg": self.angolo_diedro_deg,
            "sfericita_psi": self.sfericita(volume, superficie),
        }


class Ottaedro(SolidoPlatonico):
    """
    Ottaedro regolare:
    - 8 facce triangolari equilatere
    - 6 vertici
    - 12 spigoli
    - Angolo diedro: arccos(-1/3) ≈ 109.4712°
    """

    def __init__(self):
        super().__init__("Ottaedro", facce=8, vertici=6, spigoli=12, forma_faccia="Triangolo equilatero")
        self.angolo_diedro_deg = math.degrees(math.acos(-1.0 / 3.0))

    def calcola_da_dc(self, d_c: float) -> Dict[str, Any]:
        """
        Calcola tutte le quote a partire dal diametro della sfera circoscritta D_c (tocca i 6 vertici).
        Formula inversa per lo spigolo:
            R_c = a * sqrt(2) / 2  ==>  a = R_c * sqrt(2) = D_c * sqrt(2) / 2
        """
        r_c = d_c / 2.0
        spigolo = r_c * math.sqrt(2.0)
        return self._costruisci_proprieta(spigolo, modo="circoscritto", d_ref=d_c)

    def calcola_da_di(self, d_i: float) -> Dict[str, Any]:
        """
        Calcola tutte le quote a partire dal diametro della sfera inscritta D_i (tangente alle 8 facce).
        Formula inversa per lo spigolo:
            R_i = a * sqrt(6) / 6  ==>  a = 6 * R_i / sqrt(6) = sqrt(6) * R_i = (sqrt(6) / 2) * D_i
        """
        r_i = d_i / 2.0
        spigolo = (math.sqrt(6.0) / 2.0) * d_i
        return self._costruisci_proprieta(spigolo, modo="inscritto", d_ref=d_i)

    def _costruisci_proprieta(self, spigolo: float, modo: str, d_ref: float) -> Dict[str, Any]:
        r_c = spigolo * math.sqrt(2.0) / 2.0
        d_c = 2.0 * r_c
        r_i = spigolo * math.sqrt(6.0) / 6.0
        d_i = 2.0 * r_i
        r_m = spigolo / 2.0
        altezza_h = 2.0 * r_c  # Vertice-vertice opposto = D_c
        superficie = 2.0 * math.sqrt(3.0) * (spigolo ** 2)
        volume = (math.sqrt(2.0) / 3.0) * (spigolo ** 3)

        return {
            "nome": self.nome,
            "facce": self.facce,
            "forma_faccia": self.forma_faccia,
            "modo_riferimento": modo,
            "diametro_riferimento_m": d_ref,
            "spigolo_a_m": spigolo,
            "altezza_h_m": altezza_h,
            "diametro_circoscritto_dc_m": d_c,
            "raggio_circoscritto_rc_m": r_c,
            "diametro_inscritto_di_m": d_i,
            "raggio_inscritto_ri_m": r_i,
            "raggio_medio_rm_m": r_m,
            "superficie_m2": superficie,
            "volume_m3": volume,
            "volume_litri": volume * 1000.0,
            "rapporto_s_v": superficie / volume,
            "angolo_diedro_deg": self.angolo_diedro_deg,
            "sfericita_psi": self.sfericita(volume, superficie),
        }


class Dodecaedro(SolidoPlatonico):
    """
    Dodecaedro regolare:
    - 12 facce pentagonali regolari
    - 20 vertici
    - 30 spigoli
    - Angolo diedro: arccos(-1/sqrt(5)) ≈ 116.5651°
    """

    def __init__(self):
        super().__init__("Dodecaedro", facce=12, vertici=20, spigoli=30, forma_faccia="Pentagono regolare")
        self.angolo_diedro_deg = math.degrees(math.acos(-1.0 / math.sqrt(5.0)))

    def calcola_da_dc(self, d_c: float) -> Dict[str, Any]:
        """
        Calcola tutte le quote a partire dal diametro della sfera circoscritta D_c (tocca i 20 vertici).
        Formula inversa per lo spigolo:
            R_c = a * (sqrt(3) + sqrt(15)) / 4  ==>  a = 4 * R_c / (sqrt(3) * (1 + sqrt(5)))
        """
        r_c = d_c / 2.0
        spigolo = (4.0 * r_c) / (math.sqrt(3.0) * (1.0 + math.sqrt(5.0)))
        return self._costruisci_proprieta(spigolo, modo="circoscritto", d_ref=d_c)

    def calcola_da_di(self, d_i: float) -> Dict[str, Any]:
        """
        Calcola tutte le quote a partire dal diametro della sfera inscritta D_i (tangente alle 12 facce).
        Formula inversa per lo spigolo:
            R_i = a * 0.5 * sqrt((25 + 11*sqrt(5)) / 10)  ==>  a = D_i / sqrt((25 + 11*sqrt(5)) / 10)
        """
        r_i = d_i / 2.0
        coeff_ri = 0.5 * math.sqrt((25.0 + 11.0 * math.sqrt(5.0)) / 10.0)
        spigolo = r_i / coeff_ri
        return self._costruisci_proprieta(spigolo, modo="inscritto", d_ref=d_i)

    def _costruisci_proprieta(self, spigolo: float, modo: str, d_ref: float) -> Dict[str, Any]:
        r_c = spigolo * (math.sqrt(3.0) * (1.0 + math.sqrt(5.0))) / 4.0
        d_c = 2.0 * r_c
        coeff_ri = 0.5 * math.sqrt((25.0 + 11.0 * math.sqrt(5.0)) / 10.0)
        r_i = spigolo * coeff_ri
        d_i = 2.0 * r_i
        r_m = spigolo * (3.0 + math.sqrt(5.0)) / 4.0
        altezza_h = 2.0 * r_i  # Faccia-faccia opposta = D_i
        superficie = 3.0 * math.sqrt(25.0 + 10.0 * math.sqrt(5.0)) * (spigolo ** 2)
        volume = ((15.0 + 7.0 * math.sqrt(5.0)) / 4.0) * (spigolo ** 3)

        return {
            "nome": self.nome,
            "facce": self.facce,
            "forma_faccia": self.forma_faccia,
            "modo_riferimento": modo,
            "diametro_riferimento_m": d_ref,
            "spigolo_a_m": spigolo,
            "altezza_h_m": altezza_h,
            "diametro_circoscritto_dc_m": d_c,
            "raggio_circoscritto_rc_m": r_c,
            "diametro_inscritto_di_m": d_i,
            "raggio_inscritto_ri_m": r_i,
            "raggio_medio_rm_m": r_m,
            "superficie_m2": superficie,
            "volume_m3": volume,
            "volume_litri": volume * 1000.0,
            "rapporto_s_v": superficie / volume,
            "angolo_diedro_deg": self.angolo_diedro_deg,
            "sfericita_psi": self.sfericita(volume, superficie),
        }


class Icosaedro(SolidoPlatonico):
    """
    Icosaedro regolare:
    - 20 facce triangolari equilatere
    - 12 vertici
    - 30 spigoli
    - Angolo diedro: arccos(-sqrt(5)/3) ≈ 138.1897°
    """

    def __init__(self):
        super().__init__("Icosaedro", facce=20, vertici=12, spigoli=30, forma_faccia="Triangolo equilatero")
        self.angolo_diedro_deg = math.degrees(math.acos(-math.sqrt(5.0) / 3.0))

    def calcola_da_dc(self, d_c: float) -> Dict[str, Any]:
        """
        Calcola tutte le quote a partire dal diametro della sfera circoscritta D_c (tocca i 12 vertici).
        Formula inversa per lo spigolo:
            R_c = a * sqrt(10 + 2*sqrt(5)) / 4  ==>  a = 4 * R_c / sqrt(10 + 2*sqrt(5))
        """
        r_c = d_c / 2.0
        spigolo = (4.0 * r_c) / math.sqrt(10.0 + 2.0 * math.sqrt(5.0))
        return self._costruisci_proprieta(spigolo, modo="circoscritto", d_ref=d_c)

    def calcola_da_di(self, d_i: float) -> Dict[str, Any]:
        """
        Calcola tutte le quote a partire dal diametro della sfera inscritta D_i (tangente alle 20 facce).
        Formula inversa per lo spigolo:
            R_i = a * sqrt(3) * (3 + sqrt(5)) / 12  ==>  a = 12 * R_i / (sqrt(3) * (3 + sqrt(5)))
        """
        r_i = d_i / 2.0
        spigolo = (12.0 * r_i) / (math.sqrt(3.0) * (3.0 + math.sqrt(5.0)))
        return self._costruisci_proprieta(spigolo, modo="inscritto", d_ref=d_i)

    def _costruisci_proprieta(self, spigolo: float, modo: str, d_ref: float) -> Dict[str, Any]:
        r_c = spigolo * math.sqrt(10.0 + 2.0 * math.sqrt(5.0)) / 4.0
        d_c = 2.0 * r_c
        r_i = spigolo * (math.sqrt(3.0) * (3.0 + math.sqrt(5.0))) / 12.0
        d_i = 2.0 * r_i
        r_m = spigolo * (1.0 + math.sqrt(5.0)) / 4.0
        altezza_h = 2.0 * r_c  # Vertice-vertice opposto = D_c
        superficie = 5.0 * math.sqrt(3.0) * (spigolo ** 2)
        volume = (5.0 * (3.0 + math.sqrt(5.0)) / 12.0) * (spigolo ** 3)

        return {
            "nome": self.nome,
            "facce": self.facce,
            "forma_faccia": self.forma_faccia,
            "modo_riferimento": modo,
            "diametro_riferimento_m": d_ref,
            "spigolo_a_m": spigolo,
            "altezza_h_m": altezza_h,
            "diametro_circoscritto_dc_m": d_c,
            "raggio_circoscritto_rc_m": r_c,
            "diametro_inscritto_di_m": d_i,
            "raggio_inscritto_ri_m": r_i,
            "raggio_medio_rm_m": r_m,
            "superficie_m2": superficie,
            "volume_m3": volume,
            "volume_litri": volume * 1000.0,
            "rapporto_s_v": superficie / volume,
            "angolo_diedro_deg": self.angolo_diedro_deg,
            "sfericita_psi": self.sfericita(volume, superficie),
        }


SOLIDI_PLATONICI = [
    Tetraedro(),
    Cubo(),
    Ottaedro(),
    Dodecaedro(),
    Icosaedro(),
]
