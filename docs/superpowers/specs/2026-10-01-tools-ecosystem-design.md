# Circuit Drift Labs Web Tools Ecosystem Design

Date: 2026-10-01
Primary site: https://circuitdriftlabs.djshellshoxxx.github.io

## Purpose
Unify Circuit Drift Labs browser-based utilities under one visual identity and navigation system while preserving each repository as an independently deployable GitHub Pages tool.

## Shared visual identity
- near-black and dark navy base
- charcoal/slate surfaces and borders
- gray secondary typography
- restrained cool-blue accents
- simple flat 2D Circuit Drift Labs mark
- small logo placement in headers and/or footers rather than large hero branding
- shared `Circuit Drift Labs` link back to the primary site

## Main production tools
Display these prominently as the core utility suite:
1. TrackStats — local music-library analytics
2. Transposition Calculator — key, pitch, BPM, sample and loop calculations
3. MIDItest — MIDI monitoring and controller diagnostics
4. LoudnessBatch — batch loudness measurement/normalization workflow when available

Each tool should link to the others in a compact `More Circuit Drift Labs tools` area.

## Experiments
Display separately below the production tools because these projects serve a different purpose:
1. Binaural Web Beats
2. BabbleForge

The experiments section should be visually separated and always appear after the main tool list.

## Main site changes required during implementation
- replace/use the approved simplified dark Circuit Drift Labs logo/mark consistently
- add a dedicated tools/current utilities area if one is not already present
- add TrackStats, Transposition Calculator, MIDItest, and LoudnessBatch once deployed
- add an `Experiments` subsection beneath them with Binaural Web Beats and BabbleForge
- maintain existing instruments/effects presentation separately from utility tools
- link every utility page back to the main Circuit Drift Labs site

## Cross-tool contextual links
Links should be useful rather than repetitive:
- TrackStats key/BPM views → Transposition Calculator
- TrackStats quality/loudness views → LoudnessBatch when deployed
- MIDI-oriented help/navigation → MIDItest
- each tool footer → main Circuit Drift Labs site and other tools

## Deployment model
Each project remains independently deployable via GitHub Pages. Links should use final live Pages URLs once verified rather than guessed repository URLs.

## Success criteria
Users should be able to recognize every tool as part of Circuit Drift Labs, move among production utilities in one or two clicks, and still see experimental projects without confusing them with the primary DAW workflow tools.
