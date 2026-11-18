"""Builds the animated white Wordmark (PS-Logo-Wordmark-White-Animated.json) as a hand-authored Lottie.

Artwork:
- Letters of "PillSorted" and "PERSONAL PHARMACY": the brand's white Wordmark lockup (assets/logos/Wordmark/PS-Logo-Wordmark-White.svg),
  one shape layer per letter, so every letter can move on its own and stays vector (no text layers, which iOS and
  Android Lottie players can't animate).
- Heart and tick: the stroke centrelines from the 2023 After Effects logo animation (heart-and-tick-strokes-2023.json),
  fitted onto the brand lockup's heart, so the line draws exactly the designed path.

Motion (asymmetric): a pen dot touches down on the lower left of the heart, stretches into a short
dash that slides back, then runs out both ways and closes on the upper right of the right lobe with momentum; the
symbol breathes once on the close; the tick draws in one grey stroke; the symbol
shrinks and slides into the lockup; the letters rise in from left to right; then the tagline.

Run: python3 -I assets/logos/Animated/source/build_animated_logo.py assets/logos/Animated/PS-Logo-Wordmark-White-Animated.json
The .lottie, MP4 and WebM are made from that JSON.
"""
import json
import re
import sys
from pathlib import Path

OUT = sys.argv[1]
HERE = Path(__file__).resolve().parent
SVG = HERE.parents[1] / 'Wordmark' / 'PS-Logo-Wordmark-White.svg'
AE = HERE / 'heart-and-tick-strokes-2023.json'

FR = 60
W, H = 360, 200
K = 1.6                      # lockup scale in the comp (190 x 40 SVG units -> 304 x 64)
OFF = ((W - 190 * K) / 2, (H - 40 * K) / 2)
START_SCALE = K * 1.6        # the symbol starts 160% of its lockup size, centred, as in the 2023 design
END = 3.6                    # seconds


def f(sec):
    return round(sec * FR)


# ---------- SVG path -> Lottie shapes ----------
def svg_paths(svg):
    return re.findall(r'<path d="([^"]+)"', svg)


def parse_d(d):
    """SVG path data (M L H V C Z, absolute or relative) -> list of subpaths [(points, closed)],
    each point = [x, y, in_tangent, out_tangent] with tangents relative to the point."""
    toks = re.findall(r'[MLHVCZmlhvcz]|-?\d*\.?\d+(?:e-?\d+)?', d)
    i, cmd, subs, cur, x, y, sx, sy = 0, None, [], None, 0.0, 0.0, 0.0, 0.0

    def num():
        nonlocal i
        i += 1
        return float(toks[i - 1])

    while i < len(toks):
        if re.match(r'[A-Za-z]', toks[i]):
            cmd = toks[i]
            i += 1
        rel = cmd.islower()
        c = cmd.upper()
        if c == 'Z':
            if cur:
                if len(cur) > 1 and abs(cur[-1][0] - cur[0][0]) < 1e-6 and abs(cur[-1][1] - cur[0][1]) < 1e-6:
                    cur[0][2] = cur[-1][2]   # the closing point repeats the first: keep its in-tangent
                    cur.pop()
                subs.append((cur, True))
            cur, x, y = None, sx, sy
            continue
        if c == 'M':
            nx, ny = num(), num()
            if rel:
                nx, ny = x + nx, y + ny
            if cur:
                subs.append((cur, False))
            x, y, sx, sy = nx, ny, nx, ny
            cur = [[x, y, [0, 0], [0, 0]]]
            cmd = 'l' if rel else 'L'
        elif c in 'LHV':
            if c == 'L':
                nx, ny = num(), num()
                if rel:
                    nx, ny = x + nx, y + ny
            elif c == 'H':
                nx, ny = num(), y
                if rel:
                    nx = x + nx
            else:
                nx, ny = x, num()
                if rel:
                    ny = y + ny
            x, y = nx, ny
            cur.append([x, y, [0, 0], [0, 0]])
        elif c == 'C':
            a = [num() for _ in range(6)]
            if rel:
                a = [a[0] + x, a[1] + y, a[2] + x, a[3] + y, a[4] + x, a[5] + y]
            cur[-1][3] = [a[0] - x, a[1] - y]
            x, y = a[4], a[5]
            cur.append([x, y, [a[2] - x, a[3] - y], [0, 0]])
    if cur:
        subs.append((cur, False))
    return subs


def to_lottie_path(pts, closed):
    return {'c': closed, 'v': [[p[0], p[1]] for p in pts], 'i': [p[2] for p in pts], 'o': [p[3] for p in pts]}


def bbox_of(subs):
    xs = [p[0] for s, _ in subs for p in s]
    ys = [p[1] for s, _ in subs for p in s]
    return min(xs), min(ys), max(xs), max(ys)


# ---------- keyframes ----------
def ease(x1, y1, x2, y2):
    return (x1, y1, x2, y2)


LINEAR = ease(0.33, 0.33, 0.67, 0.67)
IN_OUT = ease(0.45, 0, 0.55, 1)
EXPO_OUT = ease(0.16, 1, 0.3, 1)
MOVE = ease(0.45, 0, 0.2, 1)          # shrink and slide together: even start, long soft landing


def anim(keys):
    """keys: [(seconds, value(s), ease to the next key)] -> Lottie animated property."""
    out = []
    for n, (t, v, e) in enumerate(keys):
        v = v if isinstance(v, list) else [v]
        k = {'t': f(t), 's': v}
        if n < len(keys) - 1 and e == 'hold':
            k['h'] = 1
        elif n < len(keys) - 1:
            dims = len(v)
            k['o'] = {'x': [e[0]] * dims, 'y': [e[1]] * dims}
            k['i'] = {'x': [e[2]] * dims, 'y': [e[3]] * dims}
        out.append(k)
    return {'a': 1, 'k': out}


def static(v):
    return {'a': 0, 'k': v}


def ks(a=(0, 0), p=(0, 0), s=(100, 100), o=100, r=0):
    def val(x):
        return x if isinstance(x, dict) else static(list(x) + [0] if isinstance(x, tuple) and len(x) == 2 else x)
    return {'a': val(a), 'p': val(p), 's': val(s if isinstance(s, dict) else tuple(s)), 'o': val(o) if isinstance(o, dict) else static(o), 'r': static(r)}


def ks3(a, p, s, o=100):
    """Transform with 3-value vectors (what After Effects exports)."""
    def v3(x):
        return x if isinstance(x, dict) else static([x[0], x[1], 0 if len(x) == 2 else x[2]])
    def s3(x):
        return x if isinstance(x, dict) else static([x[0], x[1], 100])
    return {'a': v3(a), 'p': v3(p), 's': s3(s), 'o': o if isinstance(o, dict) else static(o), 'r': static(0)}


layers = []
ind = [0]


def layer(name, ty, transform, parent=None, shapes=None):
    ind[0] += 1
    L = {'ddd': 0, 'ind': ind[0], 'ty': ty, 'nm': name, 'sr': 1, 'ks': transform, 'ao': 0,
         'ip': 0, 'op': f(END), 'st': 0, 'bm': 0}
    if parent:
        L['parent'] = parent
    if shapes is not None:
        L['shapes'] = shapes
    layers.append(L)
    return ind[0]


def group(name, items):
    items.append({'ty': 'tr', 'p': static([0, 0]), 'a': static([0, 0]), 's': static([100, 100]), 'r': static(0),
                  'o': static(100), 'sk': static(0), 'sa': static(0), 'nm': 'Transform'})
    return {'ty': 'gr', 'nm': name, 'it': items, 'np': len(items) - 1, 'cix': 2, 'bm': 0}


def fill(rgba):
    return {'ty': 'fl', 'c': static(rgba), 'o': static(100), 'r': 1, 'bm': 0, 'nm': 'Fill'}


def stroke(rgba, w):
    return {'ty': 'st', 'c': static(rgba), 'o': static(100), 'w': static(w), 'lc': 2, 'lj': 2, 'ml': 4, 'bm': 0, 'nm': 'Stroke'}


# ---------- geometry ----------
svg = open(SVG, encoding='utf-8').read()
paths = [parse_d(d) for d in svg_paths(svg)]
# Brand file order: 10 wordmark letters, the tick, the heart, then the tagline letters.
word, svg_heart, tagline = paths[:10], paths[11], paths[12:]
hx0, hy0, hx1, hy1 = bbox_of(svg_heart)

ae = json.load(open(AE))
aelayers = {l['nm']: l for l in ae['layers']}


def ae_path(name, merge_closing=False):
    """Centreline path of an After Effects stroke layer, in the 'Logo Position' null's space."""
    L = aelayers[name]
    grp = [s for s in L['shapes'] if s['ty'] == 'gr'][0]
    sh = [s for s in grp['it'] if s['ty'] == 'sh'][0]['ks']['k']
    w = [s for s in grp['it'] if s['ty'] == 'st'][0]['w']['k']
    sc = L['ks']['s']['k'][0] / 100
    px, py = L['ks']['p']['k'][:2]
    v, i, o = [list(p) for p in sh['v']], [list(p) for p in sh['i']], [list(p) for p in sh['o']]
    if merge_closing and len(v) > 1 and abs(v[-1][0] - v[0][0]) < 1e-3 and abs(v[-1][1] - v[0][1]) < 1e-3:
        i[0] = i[-1]           # the doubled closing point: point 0 takes the closing curve's tangent
        v, i, o = v[:-1], i[:-1], o[:-1]
    v = [[px + x * sc, py + y * sc] for x, y in v]
    i = [[x * sc, y * sc] for x, y in i]
    o = [[x * sc, y * sc] for x, y in o]
    return {'c': sh['c'], 'v': v, 'i': i, 'o': o}, w * sc


def cubic_points(p, n=24):
    pts = []
    m = len(p['v'])
    segs = m if p['c'] else m - 1
    for s in range(segs):
        a, b = p['v'][s], p['v'][(s + 1) % m]
        c1 = [a[0] + p['o'][s][0], a[1] + p['o'][s][1]]
        c2 = [b[0] + p['i'][(s + 1) % m][0], b[1] + p['i'][(s + 1) % m][1]]
        for k in range(n + 1):
            t = k / n
            u = 1 - t
            pts.append([u**3 * a[d] + 3 * u * u * t * c1[d] + 3 * u * t * t * c2[d] + t**3 * b[d] for d in (0, 1)])
    return pts


heart_lp, heart_w = ae_path('Heart Outlines', merge_closing=True)
tick_lp, tick_w = ae_path('Checkmark Outlines 2')
hp = cubic_points(heart_lp)
lx0 = min(x for x, _ in hp) - heart_w / 2
lx1 = max(x for x, _ in hp) + heart_w / 2
ly0 = min(y for _, y in hp) - heart_w / 2
ly1 = max(y for _, y in hp) + heart_w / 2
fit = (hx1 - hx0) / (lx1 - lx0)     # After Effects units -> brand SVG units


def to_svg(p):
    return {'c': p['c'],
            'v': [[hx0 + (x - lx0) * fit, hy0 + (y - ly0) * fit] for x, y in p['v']],
            'i': [[x * fit, y * fit] for x, y in p['i']],
            'o': [[x * fit, y * fit] for x, y in p['o']]}


heart = to_svg(heart_lp)
tick = to_svg(tick_lp)
stroke_w = heart_w * fit
cx, cy = (hx0 + hx1) / 2, (hy0 + hy1) / 2          # the symbol's centre, in SVG units
print(f'fit {fit:.5f}, stroke {stroke_w:.3f} SVG units; heart box AE {lx1-lx0:.1f}x{ly1-ly0:.1f}, '
      f'SVG {hx1-hx0:.2f}x{hy1-hy0:.2f} (aspect {((lx1-lx0)/(ly1-ly0)):.4f} vs {((hx1-hx0)/(hy1-hy0)):.4f})')

WHITE = [1, 1, 1, 1]
GREY = [0.781342029572, 0.832165658474, 0.910711288452, 1]   # the tick's grey in the 2023 animation

# ---------- timing (seconds) ----------
T_DOT, T_DASH, T_CLOSE = 0.0, 0.40, 1.15          # touch-down, dash slides back, run out and land
T_BREATH = 1.10                                     # the symbol swells 2% as the heart seals...
T_MOVE = 1.40                                       # ...and from that peak exhales into the shrink and slide
T_MOVE_END = 2.25
T_TICK = 0.90                                       # one grey stroke (the 2023 white stroke under it is dropped)
T_WORD, WORD_STAGGER, WORD_DUR = 1.95, 0.035, 0.55   # letters start as the symbol settles: no overlap
T_TAG, TAG_STAGGER, TAG_DUR = 2.52, 0.016, 0.50

# Symbol: one null carries the breath, the shrink and the slide (all in comp pixels / percent).
start_pos = [W / 2, H / 2, 0]
end_pos = [OFF[0] + cx * K, OFF[1] + cy * K, 0]
s0, s1 = START_SCALE * 100, K * 100
symbol = layer('Symbol', 3, ks3(
    a=[cx, cy],
    p=anim([(0, start_pos, LINEAR), (T_MOVE, start_pos, MOVE), (T_MOVE_END, end_pos, LINEAR)]),
    s=anim([(0, [s0, s0, 100], LINEAR),
            (T_BREATH, [s0, s0, 100], ease(0.37, 0, 0.63, 1)),             # a slow, soft swell
            (T_MOVE, [s0 * 1.02, s0 * 1.02, 100], MOVE),                   # no stop: the peak flows into the shrink
            (T_MOVE_END, [s1, s1, 100], LINEAR)])))
layers[-1]['ty'] = 3

# Wordmark null: places the brand lockup's letters in the comp.
lockup = layer('Lockup', 3, ks3(a=[0, 0], p=[OFF[0], OFF[1]], s=[K * 100, K * 100]))


def letter_layers(name, subs_list, t0, stagger, dur, rise, slide):
    order = sorted(range(len(subs_list)), key=lambda n: bbox_of(subs_list[n])[0])
    for rank, n in enumerate(order):
        subs = subs_list[n]
        x0, y0, x1, y1 = bbox_of(subs)
        t = t0 + rank * stagger
        base = [(x0 + x1) / 2, y1]                      # each letter rises from its own baseline
        shapes = [group(f'{name} {rank + 1}', [{'ty': 'sh', 'ks': static(to_lottie_path(p, c)), 'nm': 'Path'}
                                                for p, c in subs] + [fill(WHITE)])]
        layer(f'{name} {rank + 1}', 4, ks3(
            a=base,
            p=anim([(t, [base[0] - slide, base[1] + rise, 0], EXPO_OUT), (t + dur, [base[0], base[1], 0], LINEAR)]),
            s=[100, 100],
            o=anim([(t, 0, ease(0.33, 0, 0.2, 1)), (t + dur * 0.6, 100, LINEAR)])), parent=lockup, shapes=shapes)


# Top of the stack first: tagline, wordmark, tick (grey over white), heart.
letter_layers('Tagline', tagline, T_TAG, TAG_STAGGER, TAG_DUR, rise=2.5, slide=0)
letter_layers('Letter', word, T_WORD, WORD_STAGGER, WORD_DUR, rise=6, slide=3)

for name, colour, delay in (('Tick', GREY, 0),):
    t = T_TICK + delay
    trim = {'ty': 'tm', 's': static(0), 'e': anim([(t, 0, ease(0.3, 0, 0.1, 1)), (t + 0.42, 100, LINEAR)]),
            'o': static(0), 'm': 1, 'nm': 'Trim'}
    layer(name, 4, ks3(a=[0, 0], p=[0, 0], s=[100, 100]), parent=symbol,
          shapes=[group(name, [{'ty': 'sh', 'ks': static(tick), 'nm': 'Path'}, trim, stroke(colour, stroke_w)])])

# Heart: the designed draw values (start 50 -> 47.3 -> 0, end 50 -> 43.5 -> 100 along the path).
DOT = 0.35   # % of the path: a round dot at touch-down
# The run lands softly with the two round ends stopping short of each other; meanwhile the closed heart fades in
# underneath, so the last gap melts shut instead of the two ends pinching together where they meet on the curve.
GAP = 2.3    # % of the path on each side: the stroke is 4.0% of the path, so the round ends never touch
RUN = ease(0.45, 0, 0.3, 1)
T_SEAL, SEAL_DUR = T_CLOSE - 0.10, 0.16
trim = {'ty': 'tm',
        's': anim([(T_DOT, 50 - DOT, IN_OUT), (T_DASH, 47.3004748830046, RUN), (T_CLOSE, GAP, LINEAR)]),
        'e': anim([(T_DOT, 50 + DOT, IN_OUT), (T_DASH, 43.5028558353856, RUN), (T_CLOSE, 100 - GAP, LINEAR)]),
        'o': static(0), 'm': 1, 'nm': 'Trim'}
layer('Heart seal', 4, ks3(a=[0, 0], p=[0, 0], s=[100, 100],
                           o=anim([(T_SEAL, 0, ease(0.4, 0, 0.6, 1)), (T_SEAL + SEAL_DUR, 100, LINEAR)])), parent=symbol,
      shapes=[group('Heart seal', [{'ty': 'sh', 'ks': static(heart), 'nm': 'Path'}, stroke(WHITE, stroke_w)])])
layer('Heart', 4, ks3(a=[0, 0], p=[0, 0], s=[100, 100],
                      o=anim([(T_DOT, 0, LINEAR), (T_DOT + 0.08, 100, LINEAR)])), parent=symbol,
      shapes=[group('Heart', [{'ty': 'sh', 'ks': static(heart), 'nm': 'Path'}, trim, stroke(WHITE, stroke_w)])])

# Nulls are listed after the layers that use them; Lottie finds parents by index either way.
layers.sort(key=lambda L: (L['ty'] == 3))
doc = {'v': '5.12.2', 'fr': FR, 'ip': 0, 'op': f(END), 'w': W, 'h': H, 'nm': 'PillSorted launch', 'ddd': 0,
       'assets': [], 'layers': layers, 'markers': []}
json.dump(doc, open(OUT, 'w'), separators=(',', ':'))
print(f'wrote {OUT}: {len(layers)} layers, {END}s at {FR} fps')
