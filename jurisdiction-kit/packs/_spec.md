# Especificación de un pack de jurisdicción

> **Léelo completo antes de escribir un pack.** Si el pack 2 no se parece
> al pack 1, se acabó la escalabilidad del proyecto.

---

## Nombre del archivo

`<iso>.md` — código ISO 3166-1 alfa-2 en minúscula.
`co` `pe` `ec` `mx` `cl` `br` `ar` `uy` `cr` `pa`

## Frontmatter obligatorio

```yaml
---
jurisdiccion: CO
pais: Colombia
idioma_fuentes: es
verificado: 2026-08-08
verificado_por: <nombre> | jurisdiction-research
validado_por: <abogado y matrícula> | NO VALIDADO
estado: VIGENTE | POR_VERIFICAR | VENCIDO
revisar_cada: 90
version: 0.1.0
---
```

**`validado_por` es el campo que decide el valor del pack.** Sin abogado de
esa jurisdicción, el valor es `NO VALIDADO` y todas las salidas lo advierten.

---

## Formato de línea — invariante

Toda afirmación lleva **cuatro cosas**. Sin las cuatro, no entra.

```
- [nivel] <fecha> · <afirmación> · <ancla>
```

### El ancla depende del nivel

| Nivel | Ancla obligatoria | URL |
|---|---|---|
| `[oficial]` | **Cita normativa** — `Ley 1581/2012 art. 18 lit. f` | Opcional |
| `[secundaria]` | **Fuente identificable** — autor o firma | **Sí** |
| `[no-verificado]` | A quién preguntar | — |

**Por qué la cita y no la URL:** los portales gubernamentales reorganizan
rutas constantemente. `Ley 1581/2012 art. 18` no caduca; una ruta profunda
sí. Una URL muerta en el repo es peor que ninguna: parece autoritativa y da
404.

**Dónde buscar** cada cita vive en `sources/<iso>.md`, que es la capa
estable. El skill resuelve la cita a una URL vigente cuando hace falta.

### La línea tiene que sostenerse sola

Los skills extraen **líneas sueltas**, no archivos: `compliance-calendar`
saca una obligación, `doc-drafter` saca una para citarla en una cláusula.

Si el ancla está solo en el encabezado del bloque, la línea viaja sin
fuente y la cláusula generada dice "lo exige la ley" sin poder decir dónde.

### Marcadores de obligación — para el calendario

Además del nivel de fuente, toda obligación que se repita o se dispare
lleva su marcador. **Sin marcador, `compliance-calendar` no la ve.**

| Marcador | Cuándo | Formato |
|---|---|---|
| `[recurrente]` | Se repite en ciclo fijo | `cada <ciclo> · vence <fecha o regla>` |
| `[umbral]` | Se activa al cruzar una cifra | `al superar <cifra + unidad + año>` |
| `[evento]` | Se activa por un hecho | `cuando <hecho> · plazo <tiempo>` |

Toda obligación marcada lleva además **ante quién** se cumple y **qué pasa
si no**. Una obligación sin consecuencia declarada no se puede priorizar.

### Niveles de fuente

| Nivel | Significado | ¿Se cita? |
|---|---|---|
| `[oficial]` | Portal del organismo regulador o compilador normativo oficial | Sí |
| `[secundaria]` | Firma de abogados reconocida | Sí, marcada |
| `[no-verificado]` | No se encontró fuente de nivel 1 o 2 | **Sí, marcada. Va también a la lista de huecos** |

`[blog]` no existe como nivel. Un blog es pista para buscar la fuente
primaria, nunca se cita.

### Cifras — regla especial

Toda cifra lleva **unidad y año**, y marca de caducidad:

```
- [oficial] 2026-08-08 · Umbral de facturación: 3.500 UVT anuales
  · valor UVT 2026: $52.374 COP · <URL DIAN>
  · [CADUCA] revisar cada año fiscal
```

Una cifra sin año es una cifra inútil.

---

## Las cuatro capas

Este spec describe **el pack nacional**. Hay tres capas más, cada una con
su propio spec:

| Capa | Ruta | Spec |
|---|---|---|
| Nacional | `packs/<iso>.md` | este archivo |
| Territorial | `packs/<iso>/<municipio>.md` | `_spec-territorial.md` |
| Sectorial | `sectors/<iso>/<sector>.md` | `../sectors/_spec.md` |
| Módulo | `modules/<modulo>.md` | por arquitectura de negocio |

**El pack nacional es general.** No contiene sectores ni normas locales.

---

## Secciones obligatorias — las nueve

Un pack sin las nueve está incompleto. Si una no aplica en ese país, se
declara: `No aplica en <país>. Fuente: <URL>`.

### 1. Protección de datos personales
Norma principal · reglamentación · autoridad · a quién aplica · definición
de datos sensibles · registro obligatorio de bases y su umbral · régimen de
menores · transferencia internacional · deberes del responsable · deberes
del encargado · sanciones

### 2. Firma electrónica y documentos digitales
Norma · requisitos de validez · diferencia entre firma electrónica y
digital · quién carga con la prueba · casos excluidos

### 3. Facturación y obligaciones fiscales
Autoridad · quiénes están obligados · umbrales con unidad y año · régimen
simplificado si existe · sanciones

### 4. Protección al consumidor
Norma · si aplica a servicios digitales · derecho de retracto · garantías

### 5. Constitución de empresa
Tipos societarios · capital mínimo · dónde se registra · costo · tiempo ·
renovación

### 6. Normas del sector
**No se listan sectores aquí.** Esta sección solo apunta a
`sectors/<iso>/`. Un pack nacional con normativa de un rubro concreto es
inservible para los demás.

### 7. Relación laboral y contratación
Exclusividad · no competencia y su validez post-contractual · propiedad
intelectual del trabajador · contratistas independientes

### 8. Cifras que caducan
Tabla consolidada de toda cifra del pack con su año y dónde verificarla.
**Es la sección que se revisa cada año fiscal.**

### 8-bis. Obligaciones recurrentes y disparadores
Tabla consolidada de todo lo marcado `[recurrente]`, `[umbral]` y
`[evento]` en el pack. Es la sección que consume `compliance-calendar`.

**Los umbrales son los que más daño hacen**: no tienen fecha, se cruzan sin
avisar, y cuando alguien lo nota ya se incumplió.

### 9. Huecos declarados
```
## No pude verificar
- <tema> · <por qué> · PREGUNTAR A: <abogado | contador | entidad>

## Varía por ciudad o municipio
- <tema>

## Requiere abogado local sí o sí
- <tema>
```

**Si esta sección está vacía, sospecha de la investigación.** Ningún país
se mapea sin huecos.

---

## Reglas duras para todo pack

1. **Ninguna línea concluye que algo "cumple" o "es legal"**
2. **Ninguna línea da una recomendación.** Se exponen opciones y diferencias
3. **Ninguna línea cita un blog**
4. **Ninguna cifra sin año**
5. **Ninguna norma de otro país**, ni "por analogía"
6. La sección 9 nunca se omite

---

## Cómo aportar un pack nuevo

1. Copia `_spec.md` y esta estructura
2. Corre `jurisdiction-research` para tu país
3. **Consigue que un abogado de tu jurisdicción lo revise.** Sin eso, se
   publica marcado `NO VALIDADO`
4. Abre un PR con el pack y el nombre del revisor
5. No modifiques ningún skill. Si tu país necesita un skill nuevo, ábrelo
   como issue aparte

**Un pack validado vale más que cinco investigados.**
