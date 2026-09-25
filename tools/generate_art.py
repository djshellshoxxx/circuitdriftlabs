"""Create the site's original vector signal drawings. No image assets or fonts required."""
from pathlib import Path
from math import sin, pi

assets = Path(__file__).resolve().parents[1] / "assets"
assets.mkdir(exist_ok=True)

def write(name, body, size):
    (assets / name).write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size[0]} {size[1]}" fill="none">\n'
        + body + '\n</svg>\n', encoding="utf-8")

write("mark.svg", '''<rect x="2" y="2" width="44" height="44" rx="5" fill="#171B22" stroke="#2A303A"/>
<path d="M8 30h8l5-15 7 21 5-12h7" stroke="#E8532A" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/>
<circle cx="9" cy="30" r="2" fill="#4FB6C4"/><circle cx="40" cy="24" r="2" fill="#4FB6C4"/>
<path d="M2 13 13 2" stroke="#E8532A" stroke-width="2"/>''', (48,48))

grid = []
for v in range(50, 701, 50):
    grid.append(f'<path d="M{v} 0v700M0 {v}h700" stroke="#2A303A" stroke-width=".7" opacity=".45"/>')
wave_a = []
wave_b = []
for x in range(30, 671, 3):
    envelope = .42 + .58 * min(1, abs(x - 350) / 270)
    y1 = 356 + (35*sin(x*.061) + 16*sin(x*.137))*envelope
    y2 = 356 + (24*sin(x*.061 + 1.25) + 8*sin(x*.216))*envelope
    wave_a.append(f"{x},{y1:.2f}")
    wave_b.append(f"{x},{y2:.2f}")
hero = '''<defs><radialGradient id="dial"><stop stop-color="#272E38"/><stop offset="1" stop-color="#141920"/></radialGradient><linearGradient id="fade"><stop stop-color="#E8532A" stop-opacity="0"/><stop offset=".22" stop-color="#E8532A"/><stop offset=".78" stop-color="#E8532A"/><stop offset="1" stop-color="#E8532A" stop-opacity="0"/></linearGradient></defs>'''
hero += ''.join(grid)
hero += '''<circle cx="350" cy="350" r="240" stroke="#2A303A" stroke-width="1"/>
<circle cx="350" cy="350" r="195" stroke="#2A303A" stroke-width="1" stroke-dasharray="2 10"/>
<circle cx="350" cy="350" r="157" stroke="#37414C" stroke-width="1"/>
<circle cx="350" cy="350" r="128" fill="url(#dial)" stroke="#333B46" stroke-width="2"/>
<circle cx="350" cy="350" r="143" stroke="#2A303A" stroke-width="5" stroke-dasharray="630 270" transform="rotate(135 350 350)"/>
<circle cx="350" cy="350" r="143" stroke="#E8532A" stroke-width="5" stroke-dasharray="335 565" transform="rotate(135 350 350)"/>
<path d="M350 350 442 270" stroke="#E8532A" stroke-width="3" stroke-linecap="round"/>
<circle cx="350" cy="350" r="6" fill="#E8532A"/>
<path d="M45 178h125l42 42h55M655 515H527l-37-38h-57" stroke="#4FB6C4" stroke-width="1.4" opacity=".65"/>
<circle cx="45" cy="178" r="3" fill="#4FB6C4"/><circle cx="655" cy="515" r="3" fill="#4FB6C4"/>
<rect x="26" y="300" width="648" height="112" fill="#10151B" opacity=".68"/>
<path d="M26 299h648M26 413h648" stroke="#39424D" stroke-width="1"/>
<polyline points="''' + ' '.join(wave_b) + '''" stroke="#4FB6C4" stroke-width="1.4" opacity=".75"/>
<polyline points="''' + ' '.join(wave_a) + '''" stroke="url(#fade)" stroke-width="2.1"/>
<text x="46" y="96" fill="#8A929E" font-size="10" font-family="monospace" letter-spacing="2">SIGNAL / CONTROL VOLTAGE</text>
<text x="48" y="580" fill="#4FB6C4" font-size="10" font-family="monospace" letter-spacing="1.2">IN  00.78</text>
<text x="552" y="580" fill="#E8532A" font-size="10" font-family="monospace" letter-spacing="1.2">OUT 01.24</text>
<path d="M63 600h574" stroke="#2A303A"/><path d="M63 596v8m574-8v8" stroke="#4FB6C4"/>'''
write("signal-field.svg", hero, (700,700))

patch = '''<rect x="0" y="0" width="560" height="440" fill="#171B22"/>'''
for v in range(20, 561, 20):
    patch += f'<path d="M{v} 0v440" stroke="#2A303A" opacity=".35"/>'
for v in range(20, 441, 20):
    patch += f'<path d="M0 {v}h560" stroke="#2A303A" opacity=".35"/>'
patch += '''<text x="34" y="39" fill="#8A929E" font-size="10" font-family="monospace" letter-spacing="2">CDL / SIGNAL ROUTING STUDY</text>
<path d="M72 139H185v76h88M273 215h57v-83h134M72 320h176v-105M329 215v104h135" stroke="#4FB6C4" stroke-width="2" stroke-linecap="round"/>
<path d="M329 215v104h135" stroke="#E8532A" stroke-width="2"/>
<path d="M248 320h-73v-83H72" stroke="#E8532A" stroke-width="1" stroke-dasharray="4 6"/>
<rect x="38" y="104" width="82" height="70" rx="4" fill="#1E242C" stroke="#48525E"/>
<rect x="231" y="180" width="98" height="70" rx="4" fill="#1E242C" stroke="#E8532A"/>
<rect x="414" y="97" width="107" height="70" rx="4" fill="#1E242C" stroke="#48525E"/>
<rect x="414" y="284" width="107" height="70" rx="4" fill="#1E242C" stroke="#48525E"/>
<text x="55" y="131" fill="#8A929E" font-size="9" font-family="monospace">01 / INPUT</text>
<text x="245" y="207" fill="#E8532A" font-size="9" font-family="monospace">02 / CORE</text>
<text x="429" y="124" fill="#8A929E" font-size="9" font-family="monospace">03 / MOTION</text>
<text x="429" y="311" fill="#8A929E" font-size="9" font-family="monospace">04 / OUTPUT</text>
<path d="M57 150h8l4-9 5 17 4-8h20M250 226h12l5-8 8 16 6-12h25M433 143h15l5-7 5 14 4-7h31M433 331h15l5-7 5 14 4-7h31" stroke="#4FB6C4" stroke-width="1.4"/>
<circle cx="185" cy="139" r="3" fill="#4FB6C4"/><circle cx="248" cy="215" r="3" fill="#E8532A"/><circle cx="329" cy="215" r="3" fill="#E8532A"/>
<text x="34" y="405" fill="#65707E" font-size="9" font-family="monospace" letter-spacing="1">INPUT      /      PROCESS      /      FEEDBACK      /      OUTPUT</text>'''
write("patch-grid.svg", patch, (560,440))

wave = []
for x in range(0,401,4):
    y = 72 + 28*sin(x*.09)*(.6+.4*sin(x*.01)**2)
    wave.append(f"{x},{y:.1f}")
write("card-wave.svg", '<path d="M0 72h400" stroke="#2A303A"/><polyline points="'+ ' '.join(wave) +'" stroke="#E8532A" stroke-width="2"/><path d="M40 112h320" stroke="#2A303A" stroke-dasharray="2 7"/>', (400,140))
write("card-grid.svg", '''<path d="M0 70h400" stroke="#2A303A"/><path d="M45 70h25l12-31 18 61 16-47 14 17h35l15-24 12 44 16-38 10 18h33l10-17 10 34 14-17h90" stroke="#E8532A" stroke-width="2" stroke-linejoin="round"/><circle cx="180" cy="46" r="3" fill="#4FB6C4"/><circle cx="258" cy="53" r="3" fill="#4FB6C4"/>''', (400,140))
bars = '<path d="M0 115h400" stroke="#2A303A"/>'
heights = [25,37,28,48,63,75,56,44,81,105,78,62,45,34,57,72,47,32,40,56,30,20]
for i,h in enumerate(heights):
    bars += f'<rect x="{i*18+3}" y="{115-h}" width="8" height="{h}" rx="1" fill="{"#E8532A" if i in (8,9,10) else "#4FB6C4"}" opacity=".83"/>'
write("card-bars.svg", bars, (400,140))
