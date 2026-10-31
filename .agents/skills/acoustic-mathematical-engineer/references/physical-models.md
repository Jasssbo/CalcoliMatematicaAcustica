# Reference: Physical Acoustic Models and Dissipation Mechanisms

## 1. Linear Acoustic Wave Equations
In an inviscid, homogeneous, stationary fluid under linear acoustic assumptions:
$$\nabla^2 p - \frac{1}{c^2} \frac{\partial^2 p}{\partial t^2} = 0$$
For time-harmonic fields with convention $e^{+j\omega t}$:
$$\nabla^2 p + k^2 p = 0, \quad k = \frac{\omega}{c} = \frac{2\pi}{\lambda}$$

## 2. Boundary Layer Losses (Thermo-Viscous Acoustics)
On a rigid wall, the acoustic particle velocity must satisfy the no-slip condition ($u_{\parallel} = 0$), and temperature perturbations must vanish ($T' = 0$ on isothermal boundary).
This creates two boundary layers:
1. **Viscous boundary layer thickness**:
   $$\delta_v = \sqrt{\frac{2\nu}{\omega}} = \sqrt{\frac{2\mu}{\rho_0 \omega}}$$
2. **Thermal boundary layer thickness**:
   $$\delta_t = \sqrt{\frac{2\kappa}{\rho_0 C_p \omega}} = \frac{\delta_v}{\sqrt{Pr}}$$
   where $Pr = \frac{\mu C_p}{\kappa} \approx 0.71$ is the Prandtl number of air.

## 3. Surface Acoustic Impedance and Power Balance
For an acoustic surface with normal acoustic impedance $Z_s = R_s + jX_s$:
- Normalized surface impedance: $z_s = Z_s / (\rho_0 c)$
- Plane-wave reflection coefficient at normal incidence:
  $$R = \frac{z_s - 1}{z_s + 1}$$
- Normal incidence sound absorption coefficient:
  $$\alpha = 1 - |R|^2 = \frac{4 \text{Re}(z_s)}{|z_s + 1|^2}$$
- Condition for total absorption ($\alpha = 1$):
  $$z_s = 1 + j0 \iff \text{Re}(Z_s) = \rho_0 c \quad \text{and} \quad \text{Im}(Z_s) = 0$$

## 4. Micro-Perforated and Slotted Apertures (Maa / Crandall Model)
For an aperture of characteristic width $d$ and wall thickness $t$:
- When the Stokes/Womersley parameter $s = \frac{d}{2\delta_v} \gg 10$: the flow is inertial, losses are confined to thin wall layers.
- When $s \sim 1\text{--}10$: viscous shear spans the entire aperture cross-section, generating significant acoustic resistance $R_s \sim \mathcal{O}(\rho_0 c)$.


## 5. Modelli di Confinamento d'Onda dello Stato dell'Arte vs. Presente Formulazione

### A. Acoustic Black Holes (Buchi Neri Acustici - ABH)
- **Meccanismo di Trappola**: Gradiente continuo di impedenza e profilo di spessore a legge di potenza ($h(x) = \epsilon x^m$, $m \ge 2$). La velocita di fase dell'onda decade a zero ($c_p(x) \to 0$), la lunghezza d'onda locale si annulla ($\lambda(x) \to 0$) e l'energia si comprime asintoticamente nella punta infinitesima.
- **Meccanismo Dissipativo Reale**: Strato viscoelastico o film polimerico applicato alla punta tronca. Senza dissipatore, l'onda riflette totalmente all'indietro per troncamento geometrico.
- **Differenza con il presente studio**: L'ABH opera su un gradiente unidimensionale continuo a transizione lenta (WKB approximation). La nostra formulazione opera invece su un volume poliedrico 3D discreto e non-graduato, affidando l'ingresso dell'onda a una tassellazione frattale discontinua.

### B. Space-Coiling (Avvolgimento dello Spazio / Labirinti)
- **Meccanismo di Trappola**: Canali guidati tortuosi e labirintici che allungano il cammino acustico effettivo $L_{\text{eff}} \gg L_{\text{geom}}$. L'indice di rifrazione efficace diverge ($n_{\text{eff}} \gg 1$), comprimendo la risposta di risonanza a frequenze molto basse in spessori sub-lunghezza d'onda ($d \ll \lambda$).
- **Meccanismo Dissipativo Reale**: Attrito viscoso e rilassamento termico lungo i meandri stretti dei condotti guidati ($\delta_v \approx w_{\text{canale}}$).
- **Differenza con il presente studio**: Lo space-coiling costringe il campo a propagarsi in una guida d'onda 1D/2D ripiegata. La nostra formulazione esplora una cavita tridimensionale aperta (es. tetraedro), dove il rimbalzo e spaziale e tridimensionale e le pareti riflettenti sono non-ortogonali (angoli di $70.53^\circ$).

### C. Cavita a Modi Quasi-Legati (Quasi-Bound States in the Continuum - quasi-BIC)
- **Meccanismo di Trappola**: Interferenza distruttiva completa tra canali di radiazione verso il continuo esterno (symmetry-protected BIC o Friedrich-Wintgen interference). L'energia interna non puo ri-irradiare verso l'esterno, producendo fattori di merito radiativi teoricamente infiniti ($Q_{\text{rad}} \to \infty$).
- **Meccanismo Dissipativo Reale**: Amplificazione esponenziale del tempo di permanenza interno (dwell time $\tau \propto Q$), che permette anche a minime perdite intrinseche delle pareti ($1/Q_{\text{int}}$) di assorbire completamente la potenza acustica intrappolata.
- **Differenza con il presente studio**: I quasi-BIC richiedono un accoppiamento e una cancellazione di fase estremamente sensibile e a banda strettissima all'interfaccia con il continuo. La nostra formulazione con aperture frattali di Sierpinski distribuisce le aperture su scale multiple ($a/2^k$), operando potenzialmente su una densita di accoppiamento multi-scala anziche su una singola risonanza fittamente accordata.
