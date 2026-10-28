---
layout: page
title: "CDL-RFC-042"
permalink: /standards/cdl-rfc-042/
---

# CDL-RFC-042

**Draft RFC / 0.1 / not ratified**

Nonlinear state-space and wave digital solver requirements.

<section><h2>1. Scope</h2><p>Draft 0.1, October 2026. This proposal covers bounded iterative solves in real-time nonlinear audio models. It is not a ratified industry standard and does not establish historical CDL certification.</p></section><section><h2>2. Required implementation record</h2><p>Every candidate implementation must specify its equations, discretization, state variables, initialization, residual norm, absolute and relative tolerances, iteration cap and fallback. Tolerances must have units or a stated normalization. No universal numeric threshold is asserted for all circuits.</p></section><section><h2>3. Failure and timing</h2><p>The audio path must have bounded work. Report non-convergence and non-finite events through an audio-safe mechanism; do not perform file I/O or blocking synchronization in the callback. The fallback must be tested for discontinuities and output level excursions.</p></section><section><h2>4. Drift and repeatability</h2><p>The Sheffield Thermal Drift Index is a fictional term from CDL’s lore, not an established metric. Actual drift evaluation should report defined temperature coefficients, drift time constants, seed policy and measured model error. Stochastic instance variation must be optional and reproducible.</p></section><section><h2>5. Acceptance record</h2><p>Attach source revision, platform details, test vectors, residual distributions and maximum observed execution time. Approval remains pending until a reviewer can reproduce the results.</p></section>
