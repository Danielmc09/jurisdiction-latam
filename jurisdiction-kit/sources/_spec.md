# Especificación de un catálogo de fuentes

## Qué es

**Dónde buscar en un país.** No qué dice la ley — dónde está.

Es lo primero que carga `jurisdiction-research`, y lo que separa una
investigación que consulta al regulador de una que consulta un blog.

## Por qué está separado de los packs

| | Catálogo de fuentes | Pack |
|---|---|---|
| Contiene | Dominios de entidades | Afirmaciones normativas |
| Estabilidad | **Alta.** Una entidad no cambia de dominio | Media. Las normas cambian |
| Se valida con | Nada, es verificable a simple vista | Un abogado |
| Sirve para | Buscar | Consultar |

**Solo dominios raíz y portales. Nunca rutas profundas a una norma
concreta** — esas se pudren en meses.

```
BIEN   https://www.sic.gov.co
MAL    https://www.sic.gov.co/sites/default/files/normatividad/ley_1581.pdf
```

## Ruta

```
sources/<iso>.md
```

## Contenido obligatorio

Por cada área, la entidad y su portal:

1. **Datos personales** — autoridad de protección de datos
2. **Compilador normativo oficial** — donde se consulta el texto de las leyes
3. **Diario o gaceta oficial** — donde se publica lo nuevo
4. **Autoridad tributaria**
5. **Registro mercantil**
6. **Alta corte constitucional o equivalente** — jurisprudencia
7. **Consumidor**
8. **Reguladores sectoriales** — los que apliquen al país
9. **Autoridades territoriales** — cómo se encuentran las locales

## Formato

```
| Área | Entidad | Portal | Qué se busca ahí |
|---|---|---|---|
```

## Qué NO va aquí

- **Enlaces a normas específicas.** Eso lo resuelve el skill al buscar
- Blogs, firmas de abogados, medios
- Agregadores comerciales de legislación
- Rutas profundas de cualquier tipo

## Regla de mantenimiento

Se revisa **una vez al año**. Es la capa más estable del proyecto: las
entidades cambian de dominio muy rara vez.

Si un portal cambia, **es un solo cambio** y todo lo que dependía de él
sigue funcionando. Ese es el punto de tenerlo separado.
