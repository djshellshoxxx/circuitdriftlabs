# Circuit Drift Labs

Circuit Drift Labs is a static GitHub Pages site for open-source audio tools, instruments, effects and browser utilities for producers and DJs.

Live site: https://circuitdriftlabs.djshellshoxxx.github.io/

## Browser tools

The homepage includes a persistent **Tools** dropdown and dedicated browser-tools section linking the current utility suite:

- TrackStats — local music-library analytics
- Transposition Calculator — key, pitch, BPM and sample calculations
- MIDItest — MIDI monitoring and controller diagnostics
- LoudnessBatch — batch loudness/reference analysis
- PartyPosterGen — fast rave, DJ and party-poster creation

A separate **Experiments** area links:

- Binaural Web Beats
- BabbleForge

## Complete audio project index

The homepage now includes a single project index linking every verified audio-related repository in the Circuit Drift Labs ecosystem, plus live GitHub Pages builds where they are known to exist.

Repositories currently indexed:

- trackstats
- TranspositionCalc
- Miditest
- loudnessbatch
- browsertonegen
- binauralwebeats
- babbleforge
- pluginchek
- websynth
- visualsynth
- luthier
- shelloop
- snaircreator
- robodrummer
- ReverseVerb
- interfearance-vst
- reverseback
- groovescripting
- AUDIO-COMMAND-LINE-TOOLS
- SideForge
- GapFill
- PartyPosterGen

## Site design

The site uses a dark technical workbench aesthetic with a compact Circuit Drift Labs mark. The current mark uses dark blue, black and gray rather than the earlier orange/teal icon treatment, while the rest of the existing typography and site structure are preserved.

Everything is static: no package manager, framework, build step or account system is required.

## Preview locally

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Adding releases

Edit `products.js` to add published plugin/instrument releases. Browser utilities are maintained separately in the Tools section in `index.html` so they remain clearly distinguished from instruments/effects.

## Files

- `index.html` — page structure, browser-tools section and shared navigation
- `styles.css` — original site layout/theme
- `tools.css` — tools dropdown and utility-card styling
- `site.js` — release cards plus accessible Tools dropdown behavior
- `products.js` — optional instrument/effect release cards
- `assets/*.svg` — original technical vector drawings and Circuit Drift Labs mark
- `docs/superpowers/specs/` — ecosystem design specifications
- `.nojekyll` — direct GitHub Pages serving

## Related repositories

- https://github.com/djshellshoxxx/trackstats
- https://github.com/djshellshoxxx/TranspositionCalc
- https://github.com/djshellshoxxx/Miditest
- https://github.com/djshellshoxxx/loudnessbatch
- https://github.com/djshellshoxxx/PartyPosterGen

The project remains open-source-focused. Before commercial use of branding, perform the appropriate domain/trademark checks for the relevant markets.
