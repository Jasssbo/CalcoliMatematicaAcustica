# Verification Standards

## Purpose

Define the minimum evidence required before mathematical, computational and acoustic claims are treated as reliable.

## Level M — Mathematical consistency

Minimum requirements:

- explicit definitions and assumptions;
- consistent units;
- valid algebraic transformations;
- identified domains and constraints;
- correct limiting behavior where applicable.

Passing this level establishes consistency within the reviewed scope, not physical validity.

## Level G — Geometric validity

Minimum requirements:

- valid parameter ranges;
- appropriate topology and connectivity checks;
- detection of relevant degeneracies;
- consistent coordinate conventions;
- feasible dimensions within stated manufacturing constraints.

Passing this level does not establish acoustic performance.

## Level N — Numerical verification

Minimum requirements:

- independent reference cases where available;
- documented tolerances;
- stability checks appropriate to the algorithm;
- convergence or discretization checks where relevant;
- regression tests;
- reproducible inputs and outputs.

A result is numerically verified only to the extent supported by these tests.

## Level P — Physical admissibility

Minimum requirements:

- identified governing model;
- appropriate boundary and interface conditions;
- physically justified material parameters;
- consistent energy accounting;
- explicit treatment of losses and approximations.

A mathematically converged solution may still fail this level.

## Level A — Acoustic performance validation

Minimum requirements:

- a defined acoustic metric;
- a baseline and measurement configuration;
- suitable instrumentation and calibration;
- documented operating conditions;
- repeatability and uncertainty assessment;
- comparison with model predictions.

Performance claims apply only to the conditions and metrics actually tested.

## Level H — Mechanism validation

Minimum requirements:

- an explicit mechanistic hypothesis;
- a predicted observable signature;
- at least one discriminating test;
- consideration of plausible alternative explanations;
- evidence consistent with the predicted mechanism.

A device can demonstrate useful performance without validating its originally proposed mechanism. Record these outcomes separately.

## Release rule

Never label a design "validated" without stating which levels it has passed.

Use a scoped statement such as:

"Geometric validity and numerical verification passed for the documented parameter range. Physical dissipation and measured acoustic performance remain unverified."

Avoid unqualified labels such as "scientifically proven" or "fully validated."

## Change control

Any modification to a governing equation, boundary condition, geometric parameterization, loss model or numerical method triggers a review of the affected verification levels.

Retain previous test results and identify which conclusions remain valid after the change.
