# Changelog

Formato basado en [Keep a Changelog](https://keepachangelog.com/es/).

## [Sin publicar]

### Agregado
- `sources/<iso>.md` — catálogo de **dónde buscar** en cada país: entidades
  y portales raíz. Es la capa más estable y la que `jurisdiction-research`
  carga antes de la primera búsqueda
- `jurisdiction-kit/CLAUDE.md` con los guardrails compartidos del plugin
- `scripts/validate.py` — valida frontmatter, secciones obligatorias,
  marcadores de las capas y presencia de URL
- `QUICKSTART.md`, `SECURITY.md`, `CHANGELOG.md`
- Plantillas de issue y de PR en `.github/`
- `where-to-incorporate` — comparar territorios por incentivos, ecosistema
  y costo real
- `founders-and-ip` — acuerdo entre socios y cesión de propiedad intelectual
- `doc-review` — auditar documentos que la empresa ya tiene
- `compliance-calendar` — obligaciones recurrentes, umbrales y eventos
- `corporate-docs` — estatutos, actas, y misión/visión separadas de lo legal
- `doc-drafter` — de la norma a la cláusula
- Las cuatro plantillas de capa y el spec de `modules/`
- `packs/co.md` secciones de incentivos, territorialidad del ICA,
  constitución de S.A.S. y obligaciones recurrentes

### Cambiado
- **El ancla de una afirmación oficial es la cita normativa, no la URL.**
  Las rutas profundas de portales gubernamentales se pudren; una URL muerta
  en el repo parece autoritativa y da 404. `Ley 1581/2012 art. 18` no caduca
- `packs/co.md` pasa a ser **ejemplo de referencia**. El pack de cada
  usuario se genera local con `jurisdiction-research`
- Modelo de cuatro dimensiones: territorio, sector, arquitectura y etapa
- El pack nacional vuelve a ser **general**: la normativa sectorial sale a
  `sectors/` y la de arquitectura a `modules/`
- `jurisdiction-setup` pregunta departamento y municipio, no solo país
- `company-formation` ahora exige la capa territorial
- README con guía de uso y los dos caminos

### Corregido
- `where-to-incorporate` afirmaba que domiciliar en otra ciudad obliga a
  abrir sucursal. Falso para negocios sin establecimiento abierto al público
- Las plantillas de capa no existían y `jurisdiction-setup` mandaba a
  copiarlas
- Texto completo de Apache 2.0 para que GitHub detecte la licencia

## [0.1.0] — 2026-08-08
- Primera publicación: 3 skills, spec de packs y pack de Colombia
