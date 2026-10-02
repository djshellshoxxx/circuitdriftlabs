# Circuit Drift Labs Contextual Tool Links Addendum

Date: 2026-10-01

This addendum supplements the Circuit Drift Labs web-tools ecosystem design.

## Canonical production-tool order

1. TrackStats
2. Transposition Calculator
3. MIDItest
4. LoudnessBatch

## Experiments

Always below and visually separate from the production-tool list:

1. Binaural Web Beats
2. BabbleForge

## Main-site presentation

The Circuit Drift Labs home page is the canonical directory for the suite. Add a dedicated browser-tools/utilities area that links to all four production tools and then a separate Experiments area.

The approved simple 2D Circuit Drift Labs mark should be used unobtrusively across the main site and tool pages. The mark should use the dark-blue/black/gray visual direction rather than the older orange/teal treatment when the shared branding is refreshed.

## Contextual cross-linking rule

Individual tools should recommend another project only when it is a reasonable next workflow step. Generic footer navigation is separate from these recommendations.

Required examples:

- TrackStats BPM/key results -> Transposition Calculator.
- TrackStats quality/loudness views -> LoudnessBatch.
- LoudnessBatch completed analysis -> TrackStats, with copy such as `Want to know more about your tracks? Check out TrackStats for library-wide statistics.`
- LoudnessBatch track details with BPM/key metadata -> Transposition Calculator.
- MIDItest completed diagnostic -> optional next-workflow links below the report, never inside diagnostic findings.
- Transposition Calculator completed sample/key/BPM calculation -> TrackStats when the user may want library-wide context, and LoudnessBatch when comparing finished mixes/references.

## Cross-link UX requirements

- Do not display contextual recommendations before the related task has produced useful output.
- Keep recommendations small and subordinate to the primary result.
- Explain why the linked tool is useful.
- Never pass private local file paths, filenames, hashes, raw MIDI data, analysis results, or audio files through URLs.
- Safe explicit musical values such as BPM/key may be passed to Transposition Calculator when supported.
- Use final verified GitHub Pages URLs.

## Success criteria

A user can move through related Circuit Drift Labs workflows naturally without the sites feeling like a link farm, while the main home page remains the complete directory for production tools and experiments.
