## Qué cambia

## Tipo
- [ ] Capa nueva (pack, territorial, sector, módulo)
- [ ] Corrección de una capa existente
- [ ] Skill
- [ ] Documentación

---

## Si aportas o modificas una capa

- [ ] Leí el spec de esa capa
- [ ] Cada afirmación lleva **nivel de fuente, fecha, afirmación y URL**
- [ ] Ninguna fuente es un blog
- [ ] Toda cifra lleva **unidad y año**, y marca `[CADUCA]` si aplica
- [ ] Cada norma está **en el nivel que le corresponde**, no en el que la encontré
- [ ] La sección de **huecos declarados no está vacía**
- [ ] Ninguna línea afirma que algo "cumple" o "es legal"
- [ ] El frontmatter tiene `verificado` y `validado_por`

**Revisor profesional**
- [ ] Abogado o contador de la jurisdicción — nombre y matrícula:
- [ ] Ninguno — se publica `NO VALIDADO`

---

## Si tocas un skill

- [ ] `## Requiere` y `## Qué NO hacer` presentes
- [ ] `description` empieza con `[JURISDICTION]`
- [ ] Bajo 500 líneas
- [ ] **No menciona ninguna norma concreta** — eso vive en las capas
- [ ] No contradice `jurisdiction-kit/CLAUDE.md`

---

## Validación

- [ ] Corrí `python3 scripts/validate.py` y no hay fallos
