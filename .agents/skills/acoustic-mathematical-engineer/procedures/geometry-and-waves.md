# Procedure: Geometry, Wave Propagation and Internal Reflection

## Purpose

Analyze how a proposed geometry may influence acoustic propagation, reflection, phase accumulation, interference, resonance and energy confinement without assuming that any of these effects automatically produces absorption.

## 1. Define the geometric representation

Identify the actual representation used by the project:

- analytical surfaces;
- parametric curves or surfaces;
- boundary-defined cavities;
- connected channels;
- repeated cells;
- meshes;
- implicit surfaces;
- another representation.

Document coordinates, parameters, domains, boundary definitions, dimensions and construction constraints.

Do not select a representation based on familiarity alone.

## 2. Define the wave problem

Before interpreting propagation, establish the relevant physical model.

Where applicable, specify:

- fluid or solid domain;
- medium properties;
- density and sound speed;
- frequency or frequency range;
- governing equation;
- source representation;
- boundary and interface conditions;
- radiation or termination conditions;
- losses included or neglected;
- dimensionality and symmetry assumptions.

For a simple homogeneous, stationary fluid under appropriate linear assumptions, a harmonic pressure field may be represented by a Helmholtz-type equation. This is a candidate model, not a mandatory assumption for every project.

If the formulation uses a different governing equation, identify it explicitly and justify its applicability.

## 3. Distinguish path models from wave models

A geometric path calculation can estimate distances, travel times and phase accumulation under specified assumptions.

For a homogeneous medium with sound speed c, a path of length L has a propagation phase magnitude related to:

kL, where k = 2πf/c.

This relation alone does not solve the wave field. It does not automatically account for diffraction, mode conversion, coupling, finite aperture, interference from all paths or boundary losses.

Do not treat a ray or path-length model as a complete wave simulation unless the required approximations have been justified.

## 4. Analyze internal reflections

For each relevant reflection or interface, establish:

- the incident field and direction;
- local geometry and boundary condition;
- reflection coefficient or boundary model;
- phase change;
- energy reflected, transmitted and dissipated;
- coupling to other propagation paths or modes.

Do not assign a reflection coefficient from geometry alone when the boundary response also depends on material properties, frequency, incidence and the surrounding medium.

For repeated reflections, examine how the amplitude evolves. Perfectly lossless repeated reflections do not create net dissipation merely because they repeat.

## 5. Analyze interference and phase

Where the model supports it, calculate the complex field before interpreting sound-pressure cancellation.

Distinguish:

- local pressure minima;
- spatial standing-wave patterns;
- interference between coherent paths;
- interference between independent or partially coherent sources;
- cancellation at one location;
- reduction in reflected or transmitted power;
- net dissipation.

A local minimum is not sufficient evidence of a reduction in total acoustic energy.

Verify phase conventions and ensure that phase comparisons refer to compatible frequencies, reference positions and time conventions.

## 6. Analyze beats

When two or more frequency components are present, determine whether the observed envelope is consistent with their frequency difference and relative amplitudes.

Distinguish amplitude modulation from energy dissipation.

If a proposed mechanism claims that rapid beats produce heat, require a physical coupling mechanism, a quantitative energy balance and a measurement strategy capable of distinguishing the effect from ordinary losses and unrelated heating.

Do not introduce beat frequencies into a single-frequency model without defining the additional frequency components.

## 7. Analyze resonance and confinement

If resonance is proposed, identify the mathematical or measured signature:

- an eigenfrequency or eigenmode;
- a peak or dip in a frequency response;
- a pole or resonance of an appropriate system model;
- a measured energy-storage or decay characteristic;
- another clearly defined criterion.

Specify whether the relevant resonance belongs to the source, room, surrounding structure or proposed device.

Where appropriate, estimate or calculate mode shapes, quality factor, resonance bandwidth and decay behavior. State the assumptions behind each quantity.

A resonance may increase local energy storage without ensuring high absorption. Establish how energy enters the device and where it is ultimately dissipated or returned to the environment.

## 8. Establish the energy pathway

For each proposed mechanism, document the chain:

incident acoustic power → coupling into the structure → internal field or motion → energy storage and transfer → physical losses or outgoing power.

Identify any step that has not yet been modeled.

If the model is passive, verify an appropriate energy balance. For a simple, single-mode, normal-incidence case with consistent power normalization, the relationship between absorption, reflection and transmission can be expressed as:

A = 1 − R − T

Here, R and T are reflected and transmitted power fractions, not generally the squared magnitudes of arbitrary pressure ratios. The simple relation requires an appropriate accounting of all relevant propagating channels and no unaccounted energy inputs or outputs.

For multimodal or more complex systems, use a suitable generalized power balance.

## 9. Select the next model by evidence

Use the least complex model capable of answering the current question.

- Analytical model: for derivations, limits and idealized cases.
- Geometric or path model: for exploratory geometry and path comparisons.
- Reduced-order model: for parameter studies when its assumptions are justified.
- Numerical wave solver: when field interactions and boundary conditions require it.
- Experimental model: for validating actual behavior and losses.

Escalate model complexity only when a simpler model cannot answer the relevant question.

## Required deliverables

- Geometric definitions.
- Physical assumptions and governing equations.
- Propagation and boundary model.
- Reflection and phase analysis.
- Energy pathway and loss mechanisms.
- Model limitations.
- A testable prediction distinguishing the proposed mechanism from alternative explanations.
