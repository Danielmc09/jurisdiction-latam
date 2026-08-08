# Jurisdiction Kit LATAM

Capa de jurisdicción para América Latina sobre Claude.

Pregunta en qué país operas, investiga el marco legal contra **fuentes
oficiales**, y arma el paquete de esa jurisdicción con fuente y fecha en
cada línea.

---

## Qué NO hace — léelo antes de instalar

- **No da asesoría legal.** Ningún resultado sustituye a un abogado local
- **No garantiza completitud.** Declara siempre lo que no pudo verificar
- **No afirma que algo "cumple".** Dice qué exige la norma y qué falta
- **No cita blogs.** Solo fuentes oficiales, y marca las secundarias

**Si algún resultado te dice que ya estás en regla, el plugin falló.**

Un checklist legal que se ve completo pero tiene huecos es peor que no
tener checklist: da confianza sin respaldo. El valor de esto es que
**llegues a un abogado local con el mapa hecho**, no que reemplaces la
consulta.

---

## Por qué existe

Las suites legales para Claude existentes están construidas para Estados
Unidos, Reino Unido y Europa: Delaware, C-Corp, FTC, FMLA, GDPR, CCPA.

Un fundador colombiano, peruano o ecuatoriano recibe consejo sobre en qué
estado de EE. UU. constituir. No sobre SAS, Cámara de Comercio, Ley 1581 o
facturación DIAN.

Este paquete llena ese hueco.

---

## Arquitectura

**Los skills no conocen ningún país. Los datos viven en packs.**

```
jurisdiction-kit/
├── skills/          ← neutrales, se mantienen una vez
│   ├── jurisdiction-setup/
│   ├── jurisdiction-research/
│   └── company-formation/
└── packs/           ← uno por país
    ├── _spec.md     ← el formato. Léelo antes de aportar
    └── co.md        ← Colombia
```

Un fork por país significaría mantener 151 × N skills. Con esta separación
son ~15 skills + N packs. Es la diferencia entre un proyecto y un repo
abandonado.

---

## Estado de los packs

| País | Pack | Estado | Validado por abogado |
|---|---|---|---|
| 🇨🇴 Colombia | `co.md` | Investigado | **NO** |
| 🇵🇪 Perú | — | — | — |
| 🇪🇨 Ecuador | — | — | — |
| 🇲🇽 México | — | — | — |
| 🇨🇱 Chile | — | — | — |
| 🇧🇷 Brasil | — | — | — |

**Un pack validado vale más que cinco investigados.** No se publica el
siguiente país hasta que el anterior tenga revisión profesional.

---

## Instalación

```
/plugin marketplace add <usuario>/jurisdiction-latam
/plugin install jurisdiction-kit@jurisdiction-latam
```

Complementa `anthropics/claude-for-legal`. No lo reemplaza ni lo forkea.

---

## Uso

```
/jurisdiction-kit:jurisdiction-setup
```

Pregunta país, tipo de negocio y si tratas datos de personas. Después:

```
/jurisdiction-kit:jurisdiction-research
/jurisdiction-kit:company-formation
```

---

## Aportar un país

1. Lee `jurisdiction-kit/packs/_spec.md` completo
2. Corre `jurisdiction-research` para tu país
3. **Consigue que un abogado de tu jurisdicción lo revise**
4. PR con el pack y el nombre del revisor
5. No modifiques los skills. Si tu país necesita uno nuevo, abre un issue

Sin revisor, el pack se publica marcado `NO VALIDADO`.

---

## Licencia

Apache 2.0
