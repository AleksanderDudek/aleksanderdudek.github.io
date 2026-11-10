#!/usr/bin/env python3
"""Generuje stronę główną (katalog) i strony sprzedażowe z products.py.

    python3 _build/build.py

Katalog `_build/` nie jest publikowany (Jekyll pomija katalogi z `_`).
Strony z `page: "legacy"` są pisane ręcznie i generator ich nie dotyka.
"""
import html
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "_build"))
from products import GROUPS, PRODUCTS  # noqa: E402

SITE = "https://aleksanderdudek.github.io"
SHOP = "https://www.naffy.io/aleksander-dudek"
CONTACT = "adud3k93@gmail.com"
ASSET_V = "2"  # podbij po zmianie site.css / site.js, żeby przeglądarki pobrały nowe

FONTS = (
    "https://fonts.googleapis.com/css2?"
    "family=Newsreader:ital,opsz,wght@0,6..72,300..600;1,6..72,300..500"
    "&family=Figtree:wght@400;500;600"
    "&family=IBM+Plex+Mono:wght@400;500&display=swap"
)
# Ten sam kontener co w ręcznie pisanych landingach (oddech, flow, emocjonalna, tylko luz).
GTM_ID = "GTM-P4CSLTC9"
GTM_HEAD = f"""<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','{GTM_ID}');</script>
<!-- End Google Tag Manager -->"""
GTM_BODY = f"""<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->"""

FAVICON = (
    "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'>"
    "<rect width='32' height='32' rx='8' fill='%2316211F'/>"
    "<circle cx='16' cy='16' r='7' fill='%23E8B04B'/></svg>"
)


def esc(s):
    return html.escape(str(s), quote=True)


def img_url(p):
    return f"/assets/img/{p['image']}"


def head(title, description, canonical, image=None, extra=""):
    og_img = f'<meta property="og:image" content="{SITE}{image}">' if image else ""
    return f"""<!doctype html>
<html lang="pl">
<head>
{GTM_HEAD}
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pl_PL">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical}">
{og_img}
<meta name="theme-color" content="#E9EEEC">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="/assets/site.css?v={ASSET_V}">
<script src="/assets/site.js?v={ASSET_V}" defer></script>
{extra}
</head>"""


def masthead(on_product):
    back = ('<a class="masthead__link" href="/#oferta">Wszystkie produkty</a>'
            if on_product else
            f'<a class="masthead__link" href="{SHOP}">Sklep na Naffy</a>')
    return f"""<header class="masthead">
  <a class="brand" href="/"><span class="brand__dot" aria-hidden="true"></span>Sati Heart Space<span class="brand__by"> · Aleksander Dudek</span></a>
  {back}
</header>"""


def footer():
    return f"""<footer class="footer">
  <p class="footer__legal">Materiały mają charakter edukacyjny i nie zastępują porady lekarza, psychologa ani fizjoterapeuty. Płatności, dostęp do kursów i regulaminy obsługuje <a href="{SHOP}">Naffy</a>.</p>
  <p class="footer__meta">
    <a href="mailto:{CONTACT}">{CONTACT}</a>
    <span aria-hidden="true">·</span>
    <a href="{SHOP}/terms">Regulamin</a>
    <span aria-hidden="true">·</span>
    <a href="{SHOP}/privacy">Prywatność</a>
    <span aria-hidden="true">·</span>
    <a href="/megavideopublisher/">MegaVideoPublisher</a>
  </p>
</footer>"""


def buy_label(p):
    return "Zapisz się na listę" if p.get("waitlist") else "Kup na Naffy"


def price_html(p, size=""):
    cls = f"price {size}".strip()
    return (f'<span class="{cls}"><span class="price__value">{esc(p["price_label"])}</span>'
            f'<span class="price__note">{esc(p["price_note"])}</span></span>')


# ── Strona główna ──────────────────────────────────────────────────────

def card(p, wide=False):
    page_url = f"/{p['slug']}/"
    name = p.get("short", p["name"])
    pos = p.get("image_pos", "50% 50%")
    badge = ""
    if p.get("waitlist"):
        badge = '<span class="card__badge card__badge--muted">Zapisy wstrzymane</span>'
    elif p.get("badge"):
        badge = f'<span class="card__badge">{esc(p["badge"])}</span>'
    facts = " · ".join(esc(f) for f in p["facts"][:2])
    mods = (" card--waitlist" if p.get("waitlist") else "") + (" card--wide" if wide else "")
    return f"""<article class="card{mods}">
  <a class="card__media" href="{page_url}" tabindex="-1" aria-hidden="true">
    <img src="{img_url(p)}" alt="" loading="lazy" decoding="async" style="object-position:{pos}">
    {badge}
  </a>
  <div class="card__body">
    <p class="card__kind">{esc(p['kind'])} · {facts}</p>
    <h3 class="card__title"><a href="{page_url}" data-utm>{esc(name)}</a></h3>
    <p class="card__text">{p['card']}</p>
    <div class="card__foot">
      {price_html(p)}
      <a class="btn btn--small{' btn--quiet' if p.get('waitlist') else ''}" href="{esc(p['naffy'])}">{buy_label(p)}</a>
    </div>
  </div>
</article>"""


def build_index():
    groups = []
    for key, title, blurb in GROUPS:
        items = [p for p in PRODUCTS if p["group"] == key]
        if not items:
            continue
        groups.append(f"""<section class="group" id="{key}" aria-labelledby="g-{key}">
  <div class="group__head">
    <h2 class="group__title" id="g-{key}">{esc(title)}</h2>
    <p class="group__blurb">{esc(blurb)}</p>
  </div>
  <div class="grid">
    {''.join(card(p, wide=len(items) == 1) for p in items)}
  </div>
</section>""")

    desc = ("Kursy wideo, e-book i konsultacje Aleksandra Dudka (Sati Heart Space): oddech, "
            "akupresura i praca z nerwem błędnym na stres, sen i koncentrację.")
    page = f"""{head('Sati Heart Space – praktyki na stres, sen i koncentrację | Aleksander Dudek',
               desc, SITE + '/', '/assets/img/reset-kortyzolu.webp')}
<body class="page-home">
{GTM_BODY}
{masthead(False)}
<main>
  <section class="hero" aria-labelledby="hero-title">
    <div class="hero__copy">
      <p class="eyebrow">Oddech · akupresura · nerw błędny</p>
      <h1 class="hero__title" id="hero-title">Krótkie praktyki,<br><em>po których ciało odpuszcza.</em></h1>
      <p class="hero__lead">Kursy wideo, które włączasz i robisz razem z nimi. Kilka minut dziennie, bez suplementów i bez godzinnych medytacji.</p>
      <a class="btn" href="#oferta">Zobacz kursy</a>
    </div>
    <figure class="breath" aria-label="Kula oddechu: wdech 4 sekundy, wydech 6 sekund">
      <div class="breath__stage">
        <div class="breath__ring" aria-hidden="true"></div>
        <div class="breath__orb" aria-hidden="true"></div>
        <p class="breath__readout" aria-hidden="true"><span class="breath__phase">wdech 4 s · wydech 6 s</span><span class="breath__count"></span></p>
      </div>
      <figcaption class="breath__caption">Spróbuj teraz: oddychaj z kulą. Rośnie przy wdechu, maleje przy wydechu – tak prowadzą sesje w kursach.</figcaption>
    </figure>
  </section>

  <div class="catalog" id="oferta">
    {''.join(groups)}
  </div>

  <section class="about" aria-labelledby="about-title">
    <h2 class="about__title" id="about-title">Kto prowadzi</h2>
    <p>Aleksander Dudek, Sati Heart Space. Uczę technik oddechowych, pracy z nerwem błędnym, akupresury i uważności – tak, żeby dało się je robić samodzielnie, w kilka minut, przy biurku albo przed snem.</p>
  </section>
</main>
{footer()}
</body>
</html>
"""
    (ROOT / "index.html").write_text(page, encoding="utf-8")


# ── Strony sprzedażowe ─────────────────────────────────────────────────

def section_html(s):
    t = s["type"]
    title = f'<h2 class="sec__title">{esc(s["title"])}</h2>' if s.get("title") else ""
    if t == "text":
        body = "".join(f"<p>{para}</p>" for para in s["body"])
        return f'<section class="sec">{title}{body}</section>'
    if t == "list":
        intro = f'<p>{s["intro"]}</p>' if s.get("intro") else ""
        outro = f'<p class="sec__outro">{s["outro"]}</p>' if s.get("outro") else ""
        items = "".join(f"<li>{i}</li>" for i in s["items"])
        return f'<section class="sec">{title}{intro}<ul class="dots">{items}</ul>{outro}</section>'
    if t == "steps":
        label = s.get("label")
        lis = []
        for n, (head_, detail) in enumerate(s["items"], 1):
            num = f'{esc(label)} {n}' if label else str(n)
            det = f'<span class="step__detail">{detail}</span>' if detail else ""
            lis.append(f'<li class="step"><span class="step__num">{num}</span>'
                       f'<span class="step__text"><strong>{head_}</strong>{det}</span></li>')
        return f'<section class="sec">{title}<ol class="steps">{"".join(lis)}</ol></section>'
    if t == "pairs":
        rows = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in s["items"])
        return f'<section class="sec">{title}<dl class="pairs">{rows}</dl></section>'
    if t == "techniques":
        rows = []
        for name, rhythm, when in s["items"]:
            w = f'<p class="tech__when">{when}</p>' if when else ""
            rows.append(f'<li class="tech"><p class="tech__name">{name}</p>'
                        f'<p class="tech__rhythm">{rhythm}</p>{w}</li>')
        return f'<section class="sec">{title}<ul class="techs">{"".join(rows)}</ul></section>'
    if t == "topics":
        rows = "".join(f'<div class="topic"><h3>{a}</h3><p>{b}</p></div>' for a, b in s["items"])
        return f'<section class="sec">{title}<div class="topics">{rows}</div></section>'
    if t == "figure":
        return (f'<figure class="sec figure"><img src="/assets/img/{s["image"]}" alt="{esc(s["alt"])}" '
                f'loading="lazy" decoding="async"><figcaption>{s["caption"]}</figcaption></figure>')
    if t == "faq":
        qs = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in s["items"])
        return f'<section class="sec">{title}<div class="faq">{qs}</div></section>'
    if t == "note":
        body = "".join(f"<p>{para}</p>" for para in s["body"])
        return f'<aside class="sec note">{title}{body}</aside>'
    raise ValueError(f"nieznany typ sekcji: {t}")


def product_ld(p):
    data = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": p["name"],
        "description": html.unescape(p["card"]),
        "image": SITE + img_url(p),
        "brand": {"@type": "Brand", "name": "Sati Heart Space"},
        "offers": {
            "@type": "Offer",
            "url": p["naffy"],
            "price": f'{p["price"]:.2f}',
            "priceCurrency": "PLN",
            "availability": "https://schema.org/InStock",
        },
    }
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


def build_product(p):
    url = f"{SITE}/{p['slug']}/"
    after = p.get("after_buy", "Płatność i natychmiastowy dostęp przez Naffy.")
    facts = "".join(f"<li>{esc(f)}</li>" for f in p["facts"])
    pos = p.get("image_pos", "50% 50%")
    badge = f'<span class="tag">{esc(p["badge"])}</span>' if p.get("badge") else ""
    sections = "\n".join(section_html(s) for s in p["sections"])
    title = f'{p["name"]} – {p["kind"].lower()} | Aleksander Dudek'
    page = f"""{head(title, html.unescape(p['card']), url, img_url(p), product_ld(p))}
<body class="page-product">
{GTM_BODY}
{masthead(True)}
<main>
  <section class="phero">
    <div class="phero__copy">
      <p class="eyebrow">{esc(p['kind'])} {badge}</p>
      <h1 class="phero__title">{esc(p['name'])}</h1>
      <p class="phero__lead">{p['lead']}</p>
      <ul class="facts">{facts}</ul>
      <div class="buy" id="kup">
        {price_html(p, 'price--big')}
        <a class="btn btn--big" href="{esc(p['naffy'])}">Kup na Naffy</a>
        <p class="buy__after">{esc(after)}</p>
      </div>
    </div>
    <div class="phero__media">
      <img src="{img_url(p)}" alt="{esc(p['image_alt'])}" style="object-position:{pos}" decoding="async">
    </div>
  </section>

  <div class="prose">
{sections}
  </div>

  <section class="closer" aria-label="Zakup">
    <p class="closer__name">{esc(p.get('short', p['name']))}</p>
    {price_html(p, 'price--big')}
    <a class="btn btn--big" href="{esc(p['naffy'])}">Kup na Naffy</a>
    <p class="buy__after">{esc(after)}</p>
    <p class="closer__back"><a href="/#oferta">← Zobacz wszystkie produkty</a></p>
  </section>
</main>

<div class="buybar" aria-hidden="true">
  {price_html(p)}
  <a class="btn btn--small" href="{esc(p['naffy'])}" tabindex="-1">Kup na Naffy</a>
</div>
{footer()}
</body>
</html>
"""
    out = ROOT / p["slug"] / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(page, encoding="utf-8")


def check():
    slugs = [p["slug"] for p in PRODUCTS]
    assert len(slugs) == len(set(slugs)), "powtórzony slug"
    groups = {g[0] for g in GROUPS}
    for p in PRODUCTS:
        assert p["group"] in groups, p["slug"]
        assert p["naffy"].startswith("https://www.naffy.io/aleksander-dudek/"), p["slug"]
        assert (ROOT / "assets" / "img" / p["image"]).exists(), p["image"]
        if p["page"] == "legacy":
            assert (ROOT / p["slug"] / "index.html").exists(), f"brak strony {p['slug']}"
        for s in p.get("sections", []):
            if s["type"] == "figure":
                assert (ROOT / "assets" / "img" / s["image"]).exists(), s["image"]


if __name__ == "__main__":
    check()
    build_index()
    made = [p["slug"] for p in PRODUCTS if p["page"] == "generated"]
    for p in PRODUCTS:
        if p["page"] == "generated":
            build_product(p)
    print("index.html +", len(made), "stron:", ", ".join(made))
