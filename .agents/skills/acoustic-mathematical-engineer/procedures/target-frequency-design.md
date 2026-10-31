# Procedure: Target-Frequency Acoustic Design

## Purpose

Develop a reproducible workflow that maps measured acoustic targets to a candidate geometry, predicts its physical response and validates the resulting device.

The design may use unconventional geometries and proposed internal-reflection mechanisms. Do not assume a specific architecture or dissipation mechanism before the project formulation establishes it.

## Stage 1 — Characterize the source

Collect available measurements from the actual machine or acoustic environment.

Record:

- machine identity and operating state;
- microphone positions and measurement conditions;
- sampling rate and acquisition duration;
- frequency resolution and spectral processing;
- dominant tonal components;
- broadband background noise;
- harmonics and modulation sidebands;
- variation across operating cycles;
- measurement uncertainty.

Distinguish a spectral peak from a demonstrated mechanical or acoustic resonance.

If only nominal frequencies are available, label the source characterization provisional.

## Stage 2 — Define the performance objective

Specify the desired outcome before generating geometries.

Possible objectives include:

- reduction of a target sound-pressure level at a defined receiver;
- absorption of incident acoustic power;
- reduction of transmitted power;
- insertion loss in a defined installation;
- suppression of a particular spectral component;
- performance over a specified frequency band;
- simultaneous reduction across multiple targets.

Record the frequency range, required improvement, measurement configuration, installation conditions and allowable uncertainty.

Do not use an unspecified term such as "maximum damping" as the sole objective.

## Stage 3 — Build a target-frequency register

For each target, record:

- nominal frequency;
- uncertainty or observed frequency range;
- source and operating condition;
- relative amplitude or importance;
- whether the component is tonal, broadband, harmonic or transient;
- required performance;
- relevant receiver and propagation path.

When several targets exist, distinguish priorities and identify whether they must be addressed simultaneously.

Do not collapse nearby frequencies into a single target unless the bandwidth and physical model justify doing so.

## Stage 4 — Connect frequency to geometry through an explicit model

For each candidate formulation:

1. Identify the geometric parameters that may affect the response.
2. Derive or specify the relationship between those parameters and the predicted acoustic behavior.
3. Identify all additional parameters required by the physical model.
4. Establish the model's validity range.
5. Check dimensions, limits and sensitivity.
6. Compare its predictions against a simple analytical case or established reference where applicable.

A frequency-to-dimension relationship is acceptable only when the assumptions that produce it are explicit.

Do not introduce an empirical tuning coefficient merely to force a desired match. If calibration is needed, define the data, estimation method and uncertainty.

## Stage 5 — Define the design parameter space

Represent the design using a vector of parameters appropriate to the actual geometry.

For every parameter, specify:

- mathematical definition;
- unit;
- admissible range;
- manufacturing tolerance;
- geometric constraints;
- influence on the predicted response;
- uncertainty, where relevant.

Check feasibility before expensive simulations.

If the formulation is still changing, keep the geometry parameterization modular rather than hard-coding an assumed architecture.

## Stage 6 — Generate and reject candidates

Use a staged process:

1. Analytical screening of simple cases.
2. Geometric validity checks.
3. Low-cost numerical exploration.
4. More detailed physical simulation for promising candidates.
5. Independent evaluation of shortlisted candidates.

Reject candidates that violate hard constraints or fail basic physical checks.

Keep exploratory models separate from the models used to support final performance claims.

## Stage 7 — Optimize against the real objective

Use an objective function that matches the requested acoustic outcome.

For multiple target frequencies, the objective may include weighted performance across the target set, penalties for poor bandwidth, sensitivity to manufacturing tolerances, mass, volume, cost or other constraints.

Define weights and penalties explicitly. Do not allow a single strong result to conceal failure at other important frequencies.

Avoid overfitting to a single idealized operating point when the source frequency, environment or construction varies.

## Stage 8 — Quantify robustness

Test the design against plausible variations in:

- target frequency;
- material properties;
- manufacturing dimensions;
- assembly and installation;
- boundary conditions;
- source position and direction;
- temperature and other environmental conditions where relevant.

Distinguish sensitivity analysis from probabilistic uncertainty analysis. Use probability distributions only when supported by adequate information.

Report whether the design remains effective within the required tolerance range.

## Stage 9 — Produce a buildable specification

For shortlisted candidates, document:

- geometry and parameter values;
- units and dimensional tolerances;
- material and interface assumptions;
- assembly requirements;
- installation conditions;
- predicted frequency response;
- expected limitations;
- required validation measurements.

The final geometry must be reproducible from the documented parameter set.

## Stage 10 — Validate against measurements

Compare predictions and measurements using the same:

- frequency definitions;
- source operating conditions;
- reference positions;
- bandwidths;
- normalization;
- acoustic metrics.

Separate numerical error, measurement uncertainty, model discrepancy and physical variation.

If results disagree, investigate the discrepancy before recalibrating the model. Do not tune the formulation solely to match a single observed result.

## Required deliverables

- Target-frequency register.
- Defined acoustic objective.
- Geometry-to-response model.
- Design constraints and parameter ranges.
- Candidate comparison.
- Sensitivity and robustness analysis.
- Manufacturing specification.
- Validation plan and measured results when available.
