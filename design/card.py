#!/usr/bin/env python3
"""Carte simple pour un post, dans le style STYLE-GRAPHIQUE.md.

Usage : python3 design/card.py accounts/XCryptoKeys/threads/pactus-001 [index ...]
Lit posts.json, prend le champ "card" de chaque post et écrit la source
<campagne>/src/post_N.html. Avec --png, produit aussi l'image
<campagne>/post_N.png (via design/render.js).
La signature et les préfixes viennent de accounts/<compte>/card.json :
{"handle": "@moncompte", "prefixes": {"<nom technique>": "<préfixe>"}}.
Un post qui a déjà un schéma sur mesure (src/post_N.html sans la marque
"auto-card") n'est pas écrasé, mais son PNG est régénéré.

Accroches (hooks) : python3 design/card.py <campagne> --hooks [index ...] [--png]
Lit <campagne>/hooks/hooks.json et écrit <campagne>/hooks/src/hook_N.html
(et hooks/hook_N.png avec --png), puis réécrit <campagne>/hooks/HOOKS.md, la liste
des textes à copier avec leur image. Le champ "layout" de la carte choisit la
mise en page de secours : hero, list, question, chain ou versus (voir accroche_body).
La règle est un schéma sur mesure par accroche (hooks/src/hook_N.html écrit à la main,
sans la marque "auto-card") : il n'est jamais écrasé, seul son PNG est régénéré.
"""
import json, sys, os, html, re, subprocess

E = html.escape


def wrap(text, width):
    words, lines, cur = text.split(), [], ''
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur); cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur: lines.append(cur)
    return lines

def card_svg(prefix, n, card, handle):
    e = html.escape
    title = wrap(card['title'], 22)
    sub = wrap(card.get('sub', ''), 44)
    big = card.get('big', '')
    y = 215
    parts = []
    if big:
        size = 120 if len(big) <= 6 else 92 if len(big) <= 9 else 70
        parts.append(f'<text class="t" x="60" y="{y+70}" font-size="{size}" font-weight="800" fill="url(#edgeT)" filter="url(#glow)">{e(big)}</text>')
        y += 70 + 75
    for l in title:
        parts.append(f'<text class="t" x="60" y="{y}" font-size="50" font-weight="800" fill="#eaf6ff">{e(l)}</text>'); y += 60
    y += 10
    for l in sub:
        parts.append(f'<text x="60" y="{y}" font-size="24" fill="#8fa8dd">{e(l)}</text>'); y += 34
    body = '\n'.join(parts)
    return f'''<!doctype html><html><head><meta charset="utf-8"><!-- auto-card -->
<link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@600;800&display=block" rel="stylesheet">
<style>body{{margin:0;background:#040823}}.t{{font-family:'Exo 2',Inter,sans-serif}}.m{{font-family:'JetBrains Mono',monospace}}</style></head><body>
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675" font-family="Inter,sans-serif">
<defs>
 <radialGradient id="bg" cx="70%" cy="50%" r="85%"><stop offset="0" stop-color="#10235b"/><stop offset=".55" stop-color="#081039"/><stop offset="1" stop-color="#040823"/></radialGradient>
 <linearGradient id="edgeT" x1="0" x2="1"><stop offset="0" stop-color="#5cfcfa"/><stop offset="1" stop-color="#ad59e9"/></linearGradient>
 <linearGradient id="cubeA" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5cfcfa" stop-opacity=".35"/><stop offset="1" stop-color="#2169af" stop-opacity=".15"/></linearGradient>
 <linearGradient id="cubeB" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ad59e9" stop-opacity=".35"/><stop offset="1" stop-color="#4a7ce1" stop-opacity=".15"/></linearGradient>
 <filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
 <filter id="soft" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="60"/></filter>
 <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#2169af" stroke-opacity=".12"/></pattern>
 <g id="cube"><path d="M0,30 L52,0 L104,30 L104,92 L52,122 L0,92Z" stroke-width="2"/><path d="M0,30 L52,60 L104,30 M52,60 V122" fill="none" stroke-width="1.5" stroke-opacity=".7"/></g>
</defs>
<rect width="1200" height="675" fill="url(#bg)"/><rect width="1200" height="675" fill="url(#grid)"/>
<circle cx="930" cy="360" r="190" fill="#2169af" opacity=".35" filter="url(#soft)"/>
<circle cx="1080" cy="160" r="140" fill="#8565e4" opacity=".3" filter="url(#soft)"/>
<g fill="none" stroke="#46b6e9" stroke-opacity=".35" stroke-width="1.5"><path d="M1200 600H1100L1070 572H960"/><path d="M1200 130H1150L1120 100H1010"/><path d="M700 675V640L730 610H820"/></g>
<g fill="#5cfcfa" opacity=".6"><circle cx="960" cy="572" r="3"/><circle cx="1010" cy="100" r="3"/><circle cx="820" cy="610" r="3"/></g>
<g filter="url(#glow)">
 <path d="M790,395 L870,350 M950,305 L1020,265" stroke="#5cfcfa" stroke-width="3" stroke-dasharray="2 8" stroke-linecap="round"/>
 <use href="#cube" x="700" y="360" fill="url(#cubeA)" stroke="#5cfcfa"/>
 <use href="#cube" x="860" y="270" fill="url(#cubeB)" stroke="#ad59e9"/>
 <use href="#cube" x="1020" y="180" fill="url(#cubeA)" stroke="#46b6e9"/>
</g>
<g class="m" font-size="12" fill="#5cfcfa" opacity=".55" text-anchor="middle"><text x="726" y="420">0x{n:02x}</text><text x="886" y="330">1011</text><text x="1046" y="240">0x{n*7%256:02x}</text></g>
<text class="m" x="60" y="92" fill="#5cfcfa" font-size="22" font-weight="700" letter-spacing="2" filter="url(#glow)">{e(prefix.upper())} #{n}</text>
{body}
<text class="m" x="1140" y="640" fill="#488fdb" font-size="16" text-anchor="end">{e(handle)}</text>
</svg></body></html>'''

HEAD = """<!doctype html><html><head><meta charset="utf-8"><!-- auto-card -->
<link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@600;800&family=JetBrains+Mono:wght@500;700&display=block" rel="stylesheet">
<style>body{margin:0;background:#040823}.t{font-family:'Exo 2',Inter,sans-serif}.m{font-family:'JetBrains Mono',monospace}</style></head><body>
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675" font-family="Inter,sans-serif">
<defs>
 <radialGradient id="bg" cx="%(cx)s%%" cy="50%%" r="85%%"><stop offset="0" stop-color="#10235b"/><stop offset=".55" stop-color="#081039"/><stop offset="1" stop-color="#040823"/></radialGradient>
 <linearGradient id="edgeT" x1="0" x2="1"><stop offset="0" stop-color="#5cfcfa"/><stop offset="1" stop-color="#ad59e9"/></linearGradient>
 <linearGradient id="glass" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#172667" stop-opacity=".85"/><stop offset="1" stop-color="#0b2053" stop-opacity=".7"/></linearGradient>
 <linearGradient id="cubeA" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5cfcfa" stop-opacity=".35"/><stop offset="1" stop-color="#2169af" stop-opacity=".15"/></linearGradient>
 <linearGradient id="cubeB" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ad59e9" stop-opacity=".35"/><stop offset="1" stop-color="#4a7ce1" stop-opacity=".15"/></linearGradient>
 <filter id="glow" x="-30%%" y="-30%%" width="160%%" height="160%%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
 <filter id="soft" x="-100%%" y="-100%%" width="300%%" height="300%%"><feGaussianBlur stdDeviation="60"/></filter>
 <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#2169af" stroke-opacity=".12"/></pattern>
 <g id="cube"><path d="M0,30 L52,0 L104,30 L104,92 L52,122 L0,92Z" stroke-width="2"/><path d="M0,30 L52,60 L104,30 M52,60 V122" fill="none" stroke-width="1.5" stroke-opacity=".7"/></g>
 <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#5cfcfa"/></marker>
</defs>
<rect width="1200" height="675" fill="url(#bg)"/><rect width="1200" height="675" fill="url(#grid)"/>
"""

def glass(x, y, w, h, hi=False):
    stroke = 'url(#edgeT)" stroke-width="2.5" filter="url(#glow)' if hi else '#2169af" stroke-width="1.5'
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="url(#glass)" stroke="{stroke}"/>'

def lines(text, x, y, width, size, fill, cls='t', weight=800, step=None):
    out = []
    for l in wrap(text, width):
        out.append(f'<text class="{cls}" x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}">{E(l)}</text>')
        y += step or int(size * 1.2)
    return out, y

def accroche_body(c):
    """Corps de l'image d'une accroche, selon c['layout'] :
    hero     : title, big (chiffre ou formule) et sub dans une carte, items (3 thèmes reliés par des flèches), foot
    list     : title, items (4 thèmes du thread, en cartes), sub
    question : q (la question), sub ; grand point d'interrogation
    chain    : title, items (4 étapes reliées comme des blocs), sub
    versus   : left/right = {"label", "items"} (idée reçue / réalité), sub
    """
    lay, P = c.get('layout', 'hero'), []
    if lay == 'hero':
        t, y = lines(c['title'], 60, 150, 40, 50, '#eaf6ff'); P += t
        big = c['big']
        size = 110 if len(big) <= 6 else 84 if len(big) <= 9 else 62
        P.append(glass(60, 200, 470, 340, hi=True))
        P.append(f'<text class="t" x="295" y="{350 + size//3}" font-size="{size}" font-weight="800" fill="url(#edgeT)" text-anchor="middle" filter="url(#glow)">{E(big)}</text>')
        for k, l in enumerate(wrap(c.get('sub', ''), 30)[:3]):
            P.append(f'<text x="295" y="{450 + k*32}" font-size="24" fill="#8fa8dd" text-anchor="middle">{E(l)}</text>')
        for k, it in enumerate(c['items'][:3]):
            yy = 210 + k * 118
            P.append(glass(650, yy, 490, 90))
            P.append(f'<text class="m" x="680" y="{yy+55}" font-size="20" font-weight="700" fill="#5cfcfa">{k+1:02d}</text>')
            P.append(f'<text class="t" x="728" y="{yy+56}" font-size="28" font-weight="800" fill="#eaf6ff">{E(it)}</text>')
            dash = ' stroke-dasharray="6 7"' if k == 1 else ''
            col = '#ad59e9' if k == 1 else '#5cfcfa'
            P.append(f'<path d="M530,370 C590,370 580,{yy+45} 640,{yy+45}" fill="none" stroke="{col}" stroke-width="2.5"{dash} filter="url(#glow)"/>')
            P.append(f'<path d="M628,{yy+38} L642,{yy+45} L628,{yy+52}z" fill="{col}"/>')
        P.append(f'<text x="60" y="595" font-size="24" fill="#8fa8dd">{E(c.get("foot", ""))}</text>')
    elif lay == 'list':
        t, y = lines(c['title'], 60, 175, 40, 50, '#eaf6ff'); P += t
        w, h, gap = 520, 82, 22
        for i, it in enumerate(c['items']):
            x, yy = 60 + (i % 2) * (w + 40), 230 + (i // 2) * (h + gap)
            P.append(glass(x, yy, w, h, hi=(i == 0)))
            P.append(f'<text class="m" x="{x+26}" y="{yy+52}" font-size="22" font-weight="700" fill="#5cfcfa">{i+1:02d}</text>')
            P.append(f'<text class="t" x="{x+80}" y="{yy+52}" font-size="28" font-weight="800" fill="#eaf6ff">{E(it)}</text>')
        P.append(f'<text x="60" y="{230 + 2*(h+gap) + 40}" font-size="24" fill="#8fa8dd">{E(c.get("sub", ""))}</text>')
        P.append('<circle cx="1080" cy="600" r="160" fill="#8565e4" opacity=".25" filter="url(#soft)"/>')
    elif lay == 'question':
        P.append('<circle cx="960" cy="330" r="200" fill="#8565e4" opacity=".3" filter="url(#soft)"/>')
        P.append('<text class="t" x="960" y="480" font-size="400" font-weight="800" fill="url(#edgeT)" opacity=".9" text-anchor="middle" filter="url(#glow)">?</text>')
        t, y = lines(c['q'], 60, 230, 22, 58, '#eaf6ff', step=70); P += t
        t, y = lines(c.get('sub', ''), 60, y + 20, 40, 26, '#8fa8dd', cls='', weight=400, step=36); P += t
    elif lay == 'chain':
        t, y = lines(c['title'], 60, 175, 40, 50, '#eaf6ff'); P += t
        items = c['items']; n = len(items)
        w = 230; gap = (1080 - w * n) // max(n - 1, 1)
        for i, it in enumerate(items):
            x = 60 + i * (w + gap)
            P.append(f'<use href="#cube" x="{x + w//2 - 52}" y="250" fill="url(#{"cubeB" if i % 2 else "cubeA"})" stroke="{"#ad59e9" if i % 2 else "#5cfcfa"}" filter="url(#glow)"/>')
            P.append(glass(x, 410, w, 110, hi=(i == n - 1)))
            P.append(f'<text class="m" x="{x + w//2}" y="448" font-size="18" font-weight="700" fill="#5cfcfa" text-anchor="middle">STEP {i+1}</text>')
            for k, l in enumerate(wrap(it, 14)[:2]):
                P.append(f'<text class="t" x="{x + w//2}" y="{484 + k*30}" font-size="26" font-weight="800" fill="#eaf6ff" text-anchor="middle">{E(l)}</text>')
            if i < n - 1:
                P.append(f'<path d="M{x + w//2 + 64},311 L{x + w + gap + w//2 - 68},311" stroke="#5cfcfa" stroke-width="2.5" stroke-dasharray="2 8" stroke-linecap="round" marker-end="url(#arr)"/>')
        P.append(f'<text x="60" y="590" font-size="24" fill="#8fa8dd">{E(c.get("sub", ""))}</text>')
    elif lay == 'versus':
        for side, x, hi in (('left', 60, False), ('right', 630, True)):
            d = c[side]
            P.append(glass(x, 140, 510, 400, hi=hi))
            col = '#5cfcfa' if hi else '#ad59e9'
            P.append(f'<text class="m" x="{x+32}" y="195" font-size="22" font-weight="700" letter-spacing="2" fill="{col}">{E(d["label"].upper())}</text>')
            for k, it in enumerate(d['items']):
                yy = 270 + k * 95
                mark = ('<path d="M0,9 L7,17 L20,0" fill="none" stroke="#5cfcfa" stroke-width="3"/>' if hi
                        else '<path d="M0,0 L18,18 M18,0 L0,18" stroke="#ad59e9" stroke-width="3"/>')
                P.append(f'<g transform="translate({x+32},{yy-22})">{mark}</g>')
                t, _ = lines(it, x + 70, yy, 24, 30, '#eaf6ff' if hi else '#8fa8dd', step=34); P += t[:2]
        P.append('<circle cx="600" cy="340" r="34" fill="#040823" stroke="url(#edgeT)" stroke-width="2.5"/>')
        P.append('<text class="t" x="600" y="352" font-size="30" font-weight="800" fill="#eaf6ff" text-anchor="middle">VS</text>')
        P.append(f'<text x="60" y="595" font-size="24" fill="#8fa8dd">{E(c.get("sub", ""))}</text>')
    else:
        sys.exit(f"layout inconnu : {lay}")
    return '\n'.join(P)

def accroche_svg(prefix, c, handle):
    lay = c.get('layout', 'hero')
    return (HEAD % {'cx': 70 if lay in ('hero', 'question') else 50}
        + '<g fill="none" stroke="#46b6e9" stroke-opacity=".3" stroke-width="1.5"><path d="M1200 600H1100L1070 572H960"/><path d="M1200 50H1150L1120 20H1010"/></g>\n'
        + f'<text class="m" x="60" y="92" fill="#5cfcfa" font-size="22" font-weight="700" letter-spacing="2" filter="url(#glow)">{E(prefix.upper())} · DAILY THREAD</text>\n'
        + accroche_body(c)
        + f'\n<text class="m" x="1140" y="640" fill="#488fdb" font-size="16" text-anchor="end">{E(handle)}</text>\n</svg></body></html>')

def xlen(text):
    # comptage X approché : les caractères hors latin/grec/cyrillique comptent 2
    return sum(1 if ord(c) <= 0x10FF else 2 for c in text)

def accroches(camp, conf, prefix, want, png):
    hooks = json.load(open(os.path.join(camp, 'hooks', 'hooks.json'), encoding='utf-8'))
    tag = json.load(open(os.path.join(camp, 'status.json'), encoding='utf-8'))['hashtag']
    d = os.path.join(camp, 'hooks', 'src')
    os.makedirs(d, exist_ok=True)
    out, md = [], [f"# Accroches {os.path.basename(camp)}", "",
        "Réponses à coller à la main sous un post populaire du même sujet, avec l'image qui va avec. "
        "Fichier généré par `design/card.py --hooks` depuis `hooks.json` : modifier le JSON, pas ce fichier. "
        "Règles dans `STYLE.md` (section Accroches).", ""]
    for h in hooks:
        n, text = h['index'], f"{h['text']} {tag}"
        if xlen(text) >= 280: sys.exit(f"accroche {n} : {xlen(text)} caractères, 280 maximum")
        md += [f"## {n}", "", f"![accroche {n}](hook_{n}.png)", "", "```text", text, "```", "",
               f"{xlen(text)} caractères" + (f" · utilisée : {h['used']}" if h.get('used') else ''), ""]
        if want and n not in want: continue
        path = os.path.join(d, f"hook_{n}.html")
        # un schéma sur mesure (sans la marque "auto-card") n'est jamais écrasé
        if not (os.path.exists(path) and 'auto-card' not in open(path, encoding='utf-8').read()):
            open(path, 'w', encoding='utf-8').write(accroche_svg(prefix, h['card'], conf['handle']))
        out.append(path)
    open(os.path.join(camp, 'hooks', 'HOOKS.md'), 'w', encoding='utf-8').write('\n'.join(md))
    if png:
        here = os.path.dirname(os.path.abspath(__file__))
        for path in out: subprocess.run(['node', os.path.join(here, 'render.js'), path], check=True)
    print('\n'.join(out))

def main():
    camp = sys.argv[1].rstrip('/')
    args = [a for a in sys.argv[2:] if a not in ('--png', '--hooks')]
    name = re.sub(r'-\d{3}$', '', os.path.basename(camp))
    # accounts/<compte>/threads/<campagne> -> accounts/<compte>/card.json
    account = os.path.dirname(os.path.dirname(os.path.abspath(camp)))
    conf = json.load(open(os.path.join(account, 'card.json'), encoding='utf-8'))
    want = set(int(a) for a in args)
    if '--hooks' in sys.argv:
        return accroches(camp, conf, conf['prefixes'][name], want, '--png' in sys.argv)
    posts = json.load(open(os.path.join(camp, 'posts.json'), encoding='utf-8'))
    os.makedirs(os.path.join(camp, 'src'), exist_ok=True)
    out = []
    for p in posts:
        if want and p['index'] not in want: continue
        if 'card' not in p: continue
        path = os.path.join(camp, 'src', f"post_{p['index']}.html")
        if not (os.path.exists(path) and 'auto-card' not in open(path, encoding='utf-8').read()):
            open(path, 'w', encoding='utf-8').write(card_svg(conf['prefixes'][name], p['index'], p['card'], conf['handle']))
        out.append(path)
    if '--png' in sys.argv:
        here = os.path.dirname(os.path.abspath(__file__))
        for path in out: subprocess.run(['node', os.path.join(here, 'render.js'), path], check=True)
    print('\n'.join(out))

if __name__ == '__main__':
    main()
