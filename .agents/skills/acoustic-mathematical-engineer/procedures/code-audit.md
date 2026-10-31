# Procedure: Scientific Python Code Audit

## Purpose

Determine whether the Python implementation faithfully represents its intended mathematical model and whether the computed results are independently defensible.

This procedure applies to preliminary and evolving formulations. Do not require a complete theory before inspecting the code, but do not interpret missing theory as established fact.

## Step 1 — Establish the audit boundary

Record:

- files and functions in scope;
- expected inputs and outputs;
- intended mathematical meaning;
- current behavior;
- available tests and reference results;
- dependencies and numerical methods;
- explicitly excluded parts.

If the code's intended meaning is unclear, reconstruct the most plausible interpretation and label it provisional. Ask for clarification only when the ambiguity materially changes the audit.

## Step 2 — Build an equation-to-code map

For every central calculation, document:

| Field | Required information |
| --- | --- |
| Mathematical definition | Equation or algorithm being implemented |
| Source location | File, function and relevant expression |
| Inputs | Meaning, units, domain and constraints |
| Outputs | Meaning, units and expected properties |
| Assumptions | Conditions under which the calculation is valid |
| Verification | Independent test or reference |
| Status | Verified, provisional, defective or unresolved |

If the equation is not documented, reconstruct it from the implementation and mark the reconstruction as inferred.

## Step 3 — Audit mathematical correctness

Check:

- algebraic transformations and indexing;
- sign conventions and phase conventions;
- vector and matrix dimensions;
- coordinate transformations;
- derivatives, integrals and discretization;
- normalization factors;
- boundary and initial conditions;
- parameter constraints;
- limiting behavior;
- consistency between equations and comments.

For complex-valued acoustic quantities, check the time-harmonic convention and the corresponding signs in propagation, impedance and boundary relations.

Do not apply a familiar formula until its assumptions match the implementation.

## Step 4 — Audit numerical reliability

Inspect:

- division by zero and near-zero denominators;
- singular and ill-conditioned systems;
- floating-point cancellation;
- sensitivity to precision;
- mesh or sampling resolution;
- discretization errors;
- convergence criteria;
- inappropriate clipping or absolute values;
- accidental unit conversions;
- non-finite outputs;
- dependence on initialization or parameter ordering.

Distinguish implementation defects from numerical limitations inherent to the chosen method.

## Step 5 — Audit geometric validity

Check:

- coordinate and orientation consistency;
- duplicate or coincident points;
- self-intersections where relevant;
- zero-length segments and zero-area elements;
- discontinuities and invalid connectivity;
- inconsistent normals;
- negative or impossible dimensions;
- tolerance-dependent topology;
- collisions and impossible manufacturing features.

Use geometry-specific checks appropriate to the representation. Do not impose mesh requirements on a model that does not use a mesh.

## Step 6 — Construct independent tests

Prioritize tests in this order:

1. Analytically solvable cases.
2. Limiting cases with known behavior.
3. Symmetry and invariance tests.
4. Dimensional and property-based tests.
5. Independent numerical implementations.
6. Regression tests for existing behavior.
7. Randomized or adversarial tests within physically admissible domains.

Do not duplicate the original implementation line by line in the reference test. Independent verification must reduce the likelihood of reproducing the same mistake.

## Step 7 — Preserve scientific intent

Before editing:

- identify the smallest relevant code region;
- state the defect or uncertainty;
- explain the expected correction;
- define a test that distinguishes the original behavior from the corrected behavior.

Do not silently substitute a conventional acoustic model for the project's proposed formulation.

If the implementation is mathematically consistent but its physical interpretation is unsupported, report that distinction instead of rewriting the equations.

## Step 8 — Execute and report

Run available tests when execution is possible.

Report exact test commands, test outcomes and any untested behavior. Do not invent outputs or claim successful execution without evidence.

For each defect, provide:

- severity: critical, major, moderate or minor;
- confidence: confirmed or suspected;
- location;
- mathematical or physical consequence;
- minimal correction;
- verification method;
- regression risk.

A clean audit means that no defect was found within the defined scope. It does not mean that the entire model is proven correct.

## Required deliverables

- Audit scope.
- Equation-to-code map.
- Ranked defect list.
- Independent test plan.
- Minimal patch proposal.
- Actual test results.
- Remaining assumptions and limitations.
