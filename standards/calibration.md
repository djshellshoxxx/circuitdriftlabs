---
layout: page
title: "Calibration & measurement protocol"
permalink: /standards/calibration/
---

# Calibration & measurement protocol

**Proposed bench protocol**

Every trace needs a reference.

<section><h2>Before capture</h2><p>Record device identification, signal chain, gain settings, sample rate, clock source and environment. Verify reference level and loopback behavior before connecting the device under test. Use documented warm-up and settling intervals.</p></section><section><h2>During capture</h2><p>Capture silence, stepped levels, sweeps and relevant transients without changing undocumented settings. Keep raw files immutable. Repeat the sequence to distinguish drift from measurement variability.</p></section><section><h2>After capture</h2><p>Report alignment, windowing, normalization and excluded samples. Keep measurement uncertainty separate from model residuals. Store raw captures, analysis scripts and a human-readable summary together.</p></section>
