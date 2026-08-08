# Especificación de una capa territorial

Un pack nacional no alcanza. Casi todo país tiene competencias repartidas
en al menos dos niveles más.

## Los tres niveles

```
packs/<iso>.md                    ← nacional. General, sin sector
packs/<iso>/<departamento>.md     ← intermedio. Solo si el país lo usa
packs/<iso>/<municipio>.md        ← local
```

Nombre en minúscula, sin tildes ni espacios: `bogota`, `medellin`,
`ibague`, `ciudad-de-mexico`, `sao-paulo`.

## Regla de herencia

**Los tres se cargan y se suman. Ninguno reemplaza al anterior.**

Si una norma local contradice la nacional, **no se resuelve en el pack**:
se marca como conflicto y se manda a la sección de huecos. Resolver
jerarquía normativa es trabajo de abogado.

## Qué va en una capa territorial

**Solo lo que cambia.** Si es igual que la nacional, no se repite.

Típicamente:
- Registro mercantil: qué cámara, tarifas, tiempos
- Impuestos locales: ICA en Colombia, predial, industria y comercio
- Autoridad sanitaria y sus normas propias
- Uso del suelo, concepto sanitario, apertura de establecimiento
- Publicidad exterior
- Normas de establecimiento por sector, cuando la competencia es local

## Frontmatter

```yaml
---
jurisdiccion: CO
nivel: nacional | departamental | municipal
departamento: <si aplica>
municipio: <si aplica>
verificado: <fecha>
validado_por: <abogado> | NO VALIDADO
estado: VIGENTE | POR_VERIFICAR | VENCIDO
---
```

## Regla de honestidad territorial

**Un hallazgo de una ciudad no se generaliza al país.** Si verificaste algo
en Bogotá, el pack dice Bogotá — no "Colombia".

Es el error más fácil de cometer y el más caro: alguien en Ibagué siguiendo
una norma distrital de Bogotá.
