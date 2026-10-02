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
4. LoudnessBatch — batch loudness, dynamics, quality, reference and revision analysis

Each tool should link to the others in a compact `More Circuit Drift Labs tools` area.

## Experiments
Display separately below the production tools because these projects serve a different purpose:
1. Binaural Web Beats
2. BabbleForge

The experiments section should be visually separated and always appear after the main tool list.

## Main-site tools dropdown
The main Circuit Drift Labs site must have a visible `Tools` dropdown in the primary navigation.

The dropdown must contain all current Circuit Drift Labs web projects in two visually distinct groups.

### Production tools
- TrackStats
- Transposition Calculator
- MIDItest
- LoudnessBatch

### Experiments
- Binaural Web Beats
- BabbleForge

Requirements:
- dropdown must work with mouse, keyboard and touch
- `Tools` trigger must expose proper accessible expanded/collapsed state
- menu must not depend on hover alone
- current-page indication where relevant
- production tools appear first
- experiments appear below a divider/label
- links use verified live GitHub Pages URLs once deployments exist
- if a tool is not yet deployed, do not publish a broken live link; show it only once its Pages URL is verified
- the dropdown should remain compact and unobtrusive rather than becoming a large mega-menu

## Main site changes required during implementation
- replace/use the approved simplified dark Circuit Drift Labs logo/mark consistently
- add the `Tools` dropdown to the main navigation
- add a dedicated tools/current utilities area in the page body if one is not already present
- add TrackStats, Transposition Calculator, MIDItest, and LoudnessBatch once deployed
- add an `Experiments` subsection beneath them with Binaural Web Beats and BabbleForge
- maintain existing instruments/effects presentation separately from utility tools
- link every utility page back to the main Circuit Drift Labs site

## Cross-tool contextual links
Links should be useful rather than repetitive and should appear at natural completion points.

Required contextual paths:
- TrackStats key/BPM results → Transposition Calculator
- TrackStats quality/loudness results → LoudnessBatch
- LoudnessBatch completed track/batch analysis → TrackStats with copy such as `Want to know more about your tracks? Check out TrackStats for library-wide format, bitrate, sample-rate, key, BPM, metadata and collection statistics.`
- LoudnessBatch key/BPM-related findings where useful → Transposition Calculator
- MIDI-oriented help/navigation → MIDItest
- each tool footer → main Circuit Drift Labs site and other tools

Contextual suggestions must not interrupt the primary workflow or look like advertising. They should be small related-tool cards or end-of-workflow prompts.

No audio, MIDI data, filenames, metadata, analysis values, or other local user data should be transferred between tools unless a future explicit user-controlled export/import format is added. Simple cross-links may pass only non-sensitive calculator-style values through URL parameters when the user deliberately follows the link.

## Shared tool-page navigation
Each production tool should include:
- small Circuit Drift Labs brand link
- `More Circuit Drift Labs tools` area
- production tools listed before experiments
- experiments visually separated at the bottom
- no dead links to undeployed tools

## Deployment model
Each project remains independently deployable via GitHub Pages. Links should use final live Pages URLs once verified rather than guessed repository URLs.

## Success criteria
Users should be able to recognize every tool as part of Circuit Drift Labs, reach any deployed project directly from the main-site `Tools` dropdown, move among production utilities in one or two clicks, and still see experimental projects without confusing them with the primary DAW workflow tools.
