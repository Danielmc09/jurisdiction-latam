# Jurisdiction Kit LATAM

Capa de jurisdicción para América Latina sobre Claude.

Pregunta dónde operas, investiga el marco legal contra **fuentes
oficiales**, y arma los documentos y el calendario de tu jurisdicción — con
fuente y fecha en cada línea.

---

## Qué NO hace — léelo antes de instalar

- **No da asesoría legal.** Ningún resultado sustituye a un abogado local
- **No garantiza completitud.** Declara siempre lo que no pudo verificar
- **No afirma que algo "cumple".** Dice qué exige la norma y qué falta
- **No cita blogs.** Solo fuentes oficiales, y marca las secundarias

**Si algún resultado te dice que ya estás en regla, el plugin falló.**

El valor de esto es que **llegues a un abogado local con el mapa hecho**,
no que reemplaces la consulta.

---

## Por qué existe

Las suites legales para Claude están construidas para Estados Unidos,
Reino Unido y Europa: Delaware, C-Corp, FTC, GDPR, CCPA.

Un fundador colombiano, peruano o ecuatoriano recibe consejo sobre en qué
estado de EE. UU. constituir. No sobre SAS, Cámara de Comercio, Ley 1581 o
facturación DIAN.

---

## Empezar

**[QUICKSTART.md](QUICKSTART.md)** — 5 minutos.
**[SECURITY.md](SECURITY.md)** — qué hace con tu máquina y cómo se mitiga
la inyección de prompt.

## Instalación

**Requiere [Claude Code](https://claude.com/claude-code).** No aplica en
claude.ai ni en la app de escritorio. No hay servidor MCP, ni CLI en Python
o Node: cada skill es un archivo `SKILL.md` en Markdown que Claude Code
carga como instrucciones, no como código que se ejecuta.

```
/plugin marketplace add Danielmc09/jurisdiction-latam
/plugin install jurisdiction-kit@jurisdiction-latam
```

Complementa `anthropics/claude-for-legal`. No lo reemplaza ni lo forkea.

---

# Cómo se usa

## Siempre empieza igual

```
/jurisdiction-kit:jurisdiction-setup
```

Pregunta las cuatro dimensiones que definen tu marco legal:

| Dimensión | Ejemplo |
|---|---|
| **Territorio** | Colombia → Tolima → Ibagué |
| **Sector** | Fintech, salud, agro, o ninguno |
| **Arquitectura** | SaaS multi-tenant, marketplace, o ninguna |
| **Etapa** | Constituido o en proceso |

Escribe tu `perfil-legal.md`. **Se corre una sola vez.**

Después:

```
/jurisdiction-kit:jurisdiction-research
```

Investiga y llena las capas. Toma varias búsquedas.

---

## Los dos caminos

### A · Empresa que va a nacer

```
1. jurisdiction-setup       ← dónde, a qué te dedicas
2. jurisdiction-research    ← el marco legal de tu jurisdicción
3. where-to-incorporate     ← en qué ciudad conviene domiciliar
4. company-formation        ← pasos para constituir, con costos y fuentes
5. corporate-docs           ← estatutos, objeto social, actas
6. founders-and-ip          ← acuerdo entre socios y cesión de PI
7. doc-drafter              ← T&C, política de datos, aviso de privacidad
8. compliance-calendar      ← qué vence y qué umbral vas a cruzar
```

**No saltes el 6.** El acuerdo entre socios y la cesión de propiedad
intelectual son los dos errores que más empresas matan, y los que menos
gente resuelve a tiempo.

### B · Empresa que ya existe

```
1. jurisdiction-setup
2. jurisdiction-research
3. doc-review               ← audita lo que ya tienes
4. doc-drafter              ← redacta lo que faltó
5. founders-and-ip          ← inventario de PI y acuerdo entre socios
6. compliance-calendar      ← qué se te venció sin darte cuenta
```

**Empieza por `doc-review`.** Casi ninguna empresa parte de cero: parte de
una plantilla copiada de otro país que nadie volvió a mirar.

---

## Los nueve skills

| Skill | Qué hace | Cuándo |
|---|---|---|
| `jurisdiction-setup` | Pregunta las cuatro dimensiones | Una vez |
| `jurisdiction-research` | Investiga y llena las capas | Al inicio y cada 90 días |
| `where-to-incorporate` | Compara territorios: incentivos, ecosistema y costo real | Antes de elegir dónde |
| `company-formation` | Mapa para constituir, con costos y confianza por paso | Antes de constituir |
| `corporate-docs` | Estatutos, actas, libros, misión y visión | Al constituir o reformar |
| `founders-and-ip` | Acuerdo entre socios y cesión de PI | Antes del segundo socio |
| `doc-drafter` | De la norma a la cláusula | Cuando faltan documentos |
| `doc-review` | Audita documentos existentes | Cuando ya los tienes |
| `compliance-calendar` | Qué vence y qué umbral cruzaste | Mensual |

---

## Arquitectura

**Los skills no conocen ningún país. Los datos viven en capas que se suman.**

```
jurisdiction-kit/
├── skills/                    ← 9 skills, neutrales de país
├── packs/                     ← territorio
│   ├── _spec.md · _plantilla.md
│   ├── _spec-territorial.md · _plantilla-territorial.md
│   ├── co.md                  ← Colombia, nacional
│   └── co/bogota.md           ← capa municipal
├── sectors/                   ← por actividad, opcional
│   ├── _spec.md · _plantilla.md
│   └── co/tatuaje-piercing.md
└── modules/                   ← por arquitectura de negocio
    ├── _spec.md · _plantilla.md
    └── saas-multitenant.md
```

Un fork por país serían 151 × N skills. Con esta separación son 9 skills +
N capas. Es la diferencia entre un proyecto y un repo abandonado.

**`_spec.md`** dice las reglas del formato. **`_plantilla.md`** es el
archivo que copias y llenas.

---

## Las reglas que lo hacen confiable

1. Cuatro datos por línea: **nivel de fuente, fecha, afirmación, URL**
2. Jerarquía: oficial → compilador → firma de abogados (marcada) →
   **blog nunca se cita**
3. Toda cifra lleva **unidad y año**
4. **Ninguna salida concluye que algo "cumple"**
5. La sección de huecos **nunca va vacía**
6. Una norma se registra **en el nivel que le corresponde**, no donde se
   encontró
7. El pack nacional es **general**: cero sectores
8. Semáforo: <90 días normal · 90–180 advierte · **>180 el agente se
   detiene**

---

## Estado de los packs

| País | Nacional | Territorial | Sectores | Validado por abogado |
|---|---|---|---|---|
| 🇨🇴 Colombia | `co.md` | Bogotá | tatuaje-piercing | **NO** |
| 🇵🇪 Perú | — | — | — | — |
| 🇪🇨 Ecuador | — | — | — | — |
| 🇲🇽 México | — | — | — | — |
| 🇨🇱 Chile | — | — | — | — |
| 🇧🇷 Brasil | — | — | — | — |

**Un pack validado vale más que cinco investigados.** No se publica el
siguiente país hasta que el anterior tenga revisión profesional.

---

## Aportar

### Un país
1. Lee `packs/_spec.md` completo
2. Copia `packs/_plantilla.md` a `packs/<iso>.md`
3. Corre `jurisdiction-research`
4. **Consigue que un abogado de tu jurisdicción lo revise**
5. PR con el pack y el nombre del revisor

### Una ciudad, un sector, un módulo
Misma mecánica, con su plantilla y su spec.

**Sin revisor, el pack se publica marcado `NO VALIDADO`.**
No modifiques los skills: si tu país necesita uno nuevo, abre un issue.

Antes de abrir el PR:

```
python3 scripts/validate.py
```

Detalle en `CONTRIBUTING.md`.

---

## Licencia

Apache 2.0
