---
name: jurisdiction-setup
description: "[JURISDICTION] Configura el perfil legal preguntando pais, departamento, municipio, sector y arquitectura de negocio, y crea los archivos base que cargaran los demas skills. Usar una sola vez al instalar el kit, o al empezar a operar en un territorio o sector nuevo."
---

# Jurisdiction Setup

Se corre una vez. Define **qué se carga** en todas las sesiones.

## Las cuatro dimensiones

El marco legal de un negocio no lo define solo el país:

| Dimensión | Ejemplo | Se carga desde |
|---|---|---|
| **Territorio** | Colombia → Cundinamarca → Bogotá | `packs/co.md` + `packs/co/bogota.md` |
| **Sector** | Fintech, salud, agro, alimentos | `sectors/co/<sector>.md` |
| **Arquitectura** | SaaS multi-tenant, marketplace, e-commerce | `modules/<modulo>.md` |
| **Etapa** | Constituido o en proceso | Decide si corre `company-formation` |

**Las cuatro se suman. Ninguna reemplaza a otra.**

## Procedimiento

### 1. Territorio — pregunta los tres niveles

**Nunca infieras el país por el idioma.** El español se habla en veinte
países con marcos distintos.

1. ¿En qué **país** opera o va a operar?
2. ¿En qué **departamento, estado o provincia**?
3. ¿En qué **ciudad o municipio**?

**El nivel local no es un detalle.** Registro mercantil, impuestos locales,
autoridad sanitaria, uso del suelo y apertura de establecimiento suelen ser
competencia municipal. Un negocio en Ibagué no se rige por normas
distritales de Bogotá.

Si opera en varios territorios: se crea una capa por cada uno. **Nunca se
fusionan.**

### 2. Sector

> ¿A qué se dedica el negocio? Descríbelo en una frase.

De ahí infieres el sector y **lo confirmas**. No lo asumas.

Si el sector no existe en `sectors/<iso>/`, dilo: hay que investigarlo, y
puede ser un aporte al proyecto.

Si el negocio es genuinamente transversal —una herramienta de
productividad, por ejemplo— **no hay pack sectorial y está bien.**

### 3. Arquitectura de negocio

> ¿El negocio trata datos de personas que no son sus clientes directos?

Si la respuesta es sí, hay una cadena y aplica un módulo:

- **SaaS multi-tenant / B2B2C** → `modules/saas-multitenant.md`
- Marketplace, e-commerce, procesamiento por cuenta de terceros → `[por escribir]`

Es la pregunta que más se omite y la que más cambia las obligaciones.

### 4. Etapa

> ¿El negocio ya está constituido, o está en proceso?

Si está en proceso, propón `company-formation` después.

### 5. Escribe el perfil

```yaml
# perfil-legal.md
pais: CO
departamento: Cundinamarca
municipio: Bogotá D.C.
sector: <o "transversal">
arquitectura: <o "ninguna">
etapa: constituido | en proceso

carga:
  - packs/co.md
  - packs/co/bogota.md
  - sectors/co/<sector>.md
  - modules/<modulo>.md
```

Crea los archivos que falten desde sus plantillas, con todos los campos
marcados `[SIN VERIFICAR]`. **No los llenes tú.** Eso es
`jurisdiction-research`.

### 6. Propón la investigación

No la corras sin confirmación: con cuatro capas puede tomar bastantes
búsquedas.

## Qué NO hacer

- No asumas el país por idioma, zona horaria ni nombre del usuario
- **No te quedes en el nivel país.** Preguntar el municipio es obligatorio
- No infieras el sector sin confirmarlo
- No cargues packs sectoriales que el negocio no declaró
- No llenes ningún archivo con conocimiento previo
