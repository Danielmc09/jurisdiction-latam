# Especificación de un pack sectorial

## Por qué existen aparte

El pack nacional es **general**. No conoce sectores.

Un negocio no carga todos los sectores: carga el suyo. Meter normativa
sectorial en el pack nacional lo vuelve inservible para todos los demás.

## Ruta

```
sectors/<iso>/<sector>.md
```

La normativa sectorial **casi siempre es específica de un país**, así que
va bajo el código de jurisdicción.

Nombres de sector, en minúscula con guiones:
`fintech` · `salud` · `agro` · `educacion` · `alimentos` · `transporte` ·
`inmobiliario` · `tatuaje-piercing` · `cosmetica` · `seguros`

## Regla de carga

Se carga **solo si el negocio declaró ese sector** en `jurisdiction-setup`.
Nunca por defecto.

## Contenido

- Norma que regula la actividad
- Autoridad que la vigila — **suele ser distinta del regulador general**
- Habilitación, licencia o inscripción previa
- Obligaciones documentales propias
- Prohibiciones específicas
- Régimen de menores si aplica
- Sanciones y quién las impone
- **Nivel territorial de la competencia**: nacional, departamental o municipal

## Regla territorial

Muchas normas sectoriales son de competencia local. **El pack sectorial
declara en qué territorio se verificó.**

```yaml
nivel: nacional | departamental | distrital | municipal
territorio_verificado: <dónde>
```

Si se verificó en una ciudad, no se afirma para el país.

## Huecos

Igual que en el pack nacional: la sección de huecos nunca va vacía.
