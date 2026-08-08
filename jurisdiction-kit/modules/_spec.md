# Especificación de un módulo

## Qué es un módulo

Obligaciones que se disparan por **cómo está estructurado el negocio**, no
por dónde está ni a qué se dedica.

Un SaaS multi-tenant de salud y uno de logística comparten obligaciones que
un SaaS de un solo cliente no tiene. Eso es un módulo.

## Módulo vs sector — la distinción

| | Sector | Módulo |
|---|---|---|
| Responde a | ¿A qué se dedica? | ¿Cómo está estructurado? |
| Ejemplo | Fintech, salud, agro | Multi-tenant, marketplace, pagos |
| Se cruzan | Una fintech multi-tenant carga los dos | |

**Prueba:** si la obligación desaparece al cambiar de rubro, es sector. Si
sobrevive al cambio de rubro pero desaparece al cambiar la estructura, es
módulo.

## Ruta

```
modules/<slug>.md
```

Módulos previstos: `saas-multitenant` · `marketplace` · `ecommerce` ·
`procesamiento-pagos` · `ia-modelos`

## Regla de jurisdicción

**Las referencias normativas son de un país.** Un módulo por país, o
secciones por jurisdicción dentro del archivo.

La *estructura* del módulo es universal; las normas que la regulan no.

## Contenido obligatorio

1. Cuándo aplica — descrito por estructura, no por rubro
2. Cadena de roles
3. Obligaciones que dispara la arquitectura
4. Documentos que exige
5. **Requisitos que la ley impone al producto** — lo que se cumple
   construyendo una función, no firmando un papel
6. Cómo se cambia de rol sin darse cuenta
7. Obligaciones recurrentes y disparadores
8. Huecos declarados

## Regla de carga

Se carga **solo si el negocio declaró esa arquitectura** en
`jurisdiction-setup`. Nunca por defecto.
