---
name: jurisdiction-setup
description: "[JURISDICTION] Configura la jurisdiccion de trabajo preguntando pais, tipo de negocio y etapa, y crea el archivo base en knowledge-legal. Usar una sola vez al instalar el kit, o al empezar a operar en un pais nuevo."
---

# Jurisdiction Setup

Se corre una vez. Define contra qué marco legal trabajan todos los demás.

## Procedimiento

### 1. Pregunta, no asumas

**Nunca infieras el país por el idioma.** El español se habla en veinte
países con marcos legales distintos.

Preguntas, en este orden:

1. ¿En qué país está constituido o va a constituirse el negocio?
2. ¿Opera en más de un país? Si sí, se crea un archivo por cada uno.
   **Nunca se fusionan regímenes**
3. ¿Qué tipo de negocio? Producto digital, servicios, comercio,
   marketplace. Cambia qué normas aplican
4. ¿Trata datos de personas? ¿De salud, biométricos, de menores?
5. ¿Ya está constituido, o está en proceso?

### 2. Crea el archivo

Copia `knowledge-legal/_plantilla.md` a `knowledge-legal/<iso>.md`.
Código ISO de dos letras en minúscula: `co`, `mx`, `ar`, `cl`, `pe`, `es`.

Deja los campos vacíos y marcados `[SIN VERIFICAR]`. **No los llenes tú.**
Eso es `jurisdiction-research`.

### 3. Declara la jurisdicción en el proyecto

```
jurisdiccion: <ISO>
```

### 4. Propón la investigación

No la corras sin confirmación: puede tomar bastantes búsquedas.

## Qué NO hacer

- No asumas el país por el idioma, la zona horaria ni el nombre del usuario
- No llenes el archivo con conocimiento previo. Todo se verifica
- No apliques normativa de un país a otro "porque son parecidos"
