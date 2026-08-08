#!/usr/bin/env python3
"""Valida los invariantes estructurales de jurisdiction-kit.

Uso:  python3 scripts/validate.py
Sale con codigo 1 si hay fallos.
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
KIT = ROOT / "jurisdiction-kit"
ALLOWED_KEYS = {"name","description","license","allowed-tools","metadata","compatibility"}
NIVELES = {"oficial","secundaria","no-verificado","recurrente","umbral","evento","n/a"}

errors, warnings = [], []

def err(f, m): errors.append(f"FALLA  {f}: {m}")
def warn(f, m): warnings.append(f"AVISO  {f}: {m}")

# ---------- skills ----------
skills = sorted((KIT/"skills").rglob("SKILL.md"))
if not skills: err("skills/", "no se encontro ningun SKILL.md")

for p in skills:
    rel = p.relative_to(ROOT); t = p.read_text(encoding="utf-8")
    if not t.startswith("---"):
        err(rel, "el frontmatter no empieza en el byte 0"); continue
    try: fm = t.split("---")[1]
    except IndexError:
        err(rel, "frontmatter mal delimitado"); continue

    keys = re.findall(r"^([a-z-]+):", fm, re.M)
    bad = [k for k in keys if k not in ALLOWED_KEYS]
    if bad: err(rel, f"claves no permitidas en frontmatter: {bad}")

    mname = re.search(r"^name:\s*(.+)$", fm, re.M)
    if not mname: err(rel, "falta 'name'")
    else:
        name = mname.group(1).strip()
        if name != p.parent.name: err(rel, f"name '{name}' != carpeta '{p.parent.name}'")
        if not re.fullmatch(r"[a-z0-9-]+", name): err(rel, f"name '{name}' debe ser minusculas, numeros y guiones")

    mdesc = re.search(r"^description:\s*(.+)$", fm, re.M)
    if not mdesc: err(rel, "falta 'description'")
    else:
        d = mdesc.group(1).strip().strip('"')
        if not d.startswith("[JURISDICTION]"): err(rel, "description sin prefijo [JURISDICTION]")
        if len(d) > 1024: err(rel, f"description de {len(d)} chars (max 1024)")
        if len(d) < 60: warn(rel, "description muy corta: el modelo la usa para decidir si activa el skill")

    n = len(t.splitlines())
    if n >= 500: err(rel, f"{n} lineas (max 500)")
    elif n > 400: warn(rel, f"{n} lineas, cerca del tope de 500")

    for sec in ("## Requiere", "## Qué NO hacer"):
        if sec not in t: err(rel, f"falta la seccion obligatoria '{sec}'")

# ---------- capas ----------
def check_layer(p, need_estado=True):
    rel = p.relative_to(ROOT); t = p.read_text(encoding="utf-8")
    if p.name.startswith("_"): return
    if not t.startswith("---"): err(rel, "sin frontmatter"); return
    fm = t.split("---")[1]
    if need_estado and "validado_por:" not in fm: err(rel, "falta 'validado_por' en el frontmatter")
    if "verificado:" not in fm: err(rel, "falta 'verificado' en el frontmatter")
    if re.search(r"^## .*[Hh]uecos", t, re.M) is None: warn(rel, "sin seccion de huecos declarados")
    for m in re.finditer(r"^- \[([a-z-]+)\]", t, re.M):
        if m.group(1) not in NIVELES: err(rel, f"marcador desconocido: [{m.group(1)}]")
    CITA = re.compile(r"(Ley|Decreto|Resoluci[oó]n|Acuerdo|Ordenanza|C[oó]digo|Sentencia|Circular|art\.|Art\.|CST|ET)\s", re.I)
    for m in re.finditer(r"\[oficial\][^\n]*", t):
        if not CITA.search(m.group(0)) and "http" not in m.group(0):
            warn(rel, f"[oficial] sin cita normativa: {m.group(0)[:60]}...")
    for m in re.finditer(r"\[secundaria\][^\n]*", t):
        if "http" not in m.group(0):
            warn(rel, f"[secundaria] sin fuente identificable: {m.group(0)[:60]}...")

for d, needs in (("packs", True), ("sectors", True), ("modules", True)):
    for p in sorted((KIT/d).rglob("*.md")):
        check_layer(p, needs)

# ---------- gobernanza ----------
for f in ("README.md","CONTRIBUTING.md","LICENSE",".claude-plugin/marketplace.json"):
    if not (ROOT/f).exists(): err(f, "falta")
if not (KIT/"CLAUDE.md").exists(): err("jurisdiction-kit/CLAUDE.md", "faltan los guardrails compartidos")
if not (KIT/"sources"/"_spec.md").exists(): err("sources/_spec.md", "falta el spec del catalogo de fuentes")
for d in ("packs","sectors","modules"):
    if not (KIT/d/"_spec.md").exists() and not list((KIT/d).glob("_spec*.md")):
        err(f"{d}/_spec.md", "falta el spec de la capa")
    if not list((KIT/d).glob("_plantilla*.md")):
        err(f"{d}/_plantilla.md", "falta la plantilla de la capa")

# ---------- salida ----------
for w in warnings: print(w)
for e in errors: print(e)
print(f"\n{len(skills)} skills · {len(errors)} fallos · {len(warnings)} avisos")
sys.exit(1 if errors else 0)
