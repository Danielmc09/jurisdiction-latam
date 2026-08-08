# Estrategia multipaís

---

# 1. La matemática que descarta el fork por país

`claude-for-legal` tiene **151 skills**, con marcos estadounidenses
cableados en 160 archivos.

| Estrategia | Artefactos a mantener | Actualización anual |
|---|---|---|
| **Fork por país** | 151 × 20 = **3.020 skills** | 3.020 revisiones |
| **Skills + paquetes** | ~15 skills + 20 paquetes = **35** | 20 revisiones |

Un fork por país **muere en el tercero.** No por falta de ganas: porque
cada cifra tributaria caduca cada año, y revisar 3.020 archivos al año no
lo hace una persona.

**Y el fork tiene un problema peor:** cada vez que Anthropic actualice el
repo original, tienes que rebasar 20 forks divergentes.

---

# 2. La separación que lo hace posible

El error de diseño del repo oficial es mezclar dos cosas que cambian a
velocidades distintas:

| Capa | Ejemplo | ¿Cambia por país? | ¿Cambia por año? |
|---|---|---|---|
| **Método** | Cómo se revisa un acuerdo de encargo | **No** | No |
| **Datos** | Cuál es la norma, qué umbral, qué regulador | **Sí** | Sí |

**El método es 90% invariante.** Revisar un DPA es el mismo procedimiento
en Bogotá que en Lima: identificar roles, verificar finalidades, revisar
medidas de seguridad, marcar lo que falta. Lo que cambia es contra qué
norma se contrasta.

Nuestro `knowledge-legal/<iso>.md` ya es esa separación. **El diseño que
hicimos por accidente es el que escala.**

---

# 3. La arquitectura

```
jurisdiction-kit/                    ← se mantiene una vez
├── skills/                          ← 12–15 skills neutrales
│   ├── jurisdiction-setup/
│   ├── jurisdiction-research/
│   ├── company-formation/
│   ├── dpa-review/
│   ├── privacy-assessment/
│   └── ...
└── packs/                           ← uno por país
    ├── _spec.md                     ← el formato
    ├── co.md   ← Colombia
    ├── ec.md   ← Ecuador
    ├── pe.md   ← Perú
    └── br.md   ← Brasil
```

Un skill nunca nombra un país. Lee el pack de la jurisdicción declarada.

**Consecuencia:** un desarrollador peruano agrega `pe.md` y no toca ni un
skill. Eso es lo que hace que crezca sin ti.

---

# 4. El cuello de botella real: no es generar, es validar

Un agente investiga el marco colombiano en una tarde. **Eso no vale nada
por sí solo.**

Lo que hace confiable un pack es que **un abogado de ese país lo firme.**

| Etapa | Quién | Tiempo |
|---|---|---|
| Investigación con fuentes oficiales | El agente | 1 día |
| Revisión y corrección | Abogado local | 1–2 semanas |
| Marcado de lo no verificable | Ambos | — |
| Publicación con firma | — | — |

**Un país validado vale más que veinte investigados.** Y es tu única
ventaja defendible: cualquiera puede correr búsquedas; conseguir que un
abogado colombiano avale el pack, no.

Cada pack lleva en su encabezado quién lo revisó y cuándo. Sin revisor, se
publica marcado **`[NO VALIDADO]`**.

---

# 5. El orden, y por qué no es el que dijiste

Propusiste Colombia → Ecuador → Perú → Brasil. Cambiaría el último.

| # | País | Por qué en ese lugar |
|---|---|---|
| 1 | **Colombia** | Es tu país. Tienes el caso real y vas a hablar con un abogado de todos modos |
| 2 | **Perú** | Ley de protección de datos con estructura comparable. Mercado tech más grande que Ecuador |
| 3 | **Ecuador** | Marco más reciente, menos jurisprudencia acumulada — más fácil de mapear |
| 4 | **México** | El mercado más grande de habla hispana. Debería ir antes que Brasil |
| 5 | **Chile** | Marco reformado recientemente |
| N | **Brasil** | **Al final.** Portugués, LGPD con estructura propia, y necesitas fuentes y abogado en otro idioma |

Brasil no es difícil por la ley. Es difícil porque **rompe el supuesto de
idioma** de todo lo demás: fuentes en portugués, revisor en portugués,
terminología distinta. Eso es un proyecto aparte, no el cuarto de la fila.

---

# 6. Regla de entrada: no publiques el país N+1 hasta que el N esté validado

La tentación va a ser generar cinco packs en una semana porque el agente
puede. **Resístela.**

Cinco packs sin validar es peor que uno validado: la gente confía en el
paquete completo y falla en el que estaba mal.

**Criterio para pasar al siguiente país:**
- [ ] El pack anterior fue revisado por un abogado de ese país
- [ ] Tiene su sección de "no verificable" completa
- [ ] Alguien lo usó para algo real y no falló

---

# 7. Distribución

No forkeas `claude-for-legal`. Publicas un marketplace propio que se
instala **junto** a él.

```
Usuario instala:
  claude-for-legal          ← método legal general, de Anthropic
  jurisdiction-kit-latam    ← el tuyo: la capa de jurisdicción
```

Ventajas:
- No rebasas nada cuando Anthropic actualice
- Tus skills declaran su departamento con prefijo `[JURISDICTION]` para no
  colisionar con los de ellos
- Si Anthropic agrega soporte LATAM oficialmente, tu paquete sigue
  sirviendo o se contribuye de vuelta

---

# 8. Lo primero que haría, en orden

1. **Escribir `packs/_spec.md`** — el formato exacto de un pack. Sin esto,
   el pack 2 no se parece al 1 y se acabó la escalabilidad
2. **Completar `co.md`** con lo que ya investigamos: Ley 1581, Ley 527,
   Decreto 2364, facturación DIAN, artículos 17 y 18
3. **Llevárselo al abogado con el que ya vas a hablar** por tu contrato.
   Es la misma consulta
4. **Publicar Colombia solo.** Un país validado
5. Perú cuando alguien lo pida, no antes

---

# 9. La pregunta que decide si esto existe

**¿Quién valida el pack de Ecuador?**

Tú puedes escribir Colombia porque vives ahí y vas a pagar un abogado
igual. Para Ecuador necesitas un abogado ecuatoriano. Y para veinte
países, veinte abogados.

Tres salidas posibles:
- **Comunitaria** — cada país lo aporta alguien de ahí. Lento pero
  sostenible
- **Comercial** — pagas la validación. Rápido, pero es un costo real por
  país
- **Marcada** — publicas sin validar y lo dices en grande. Honesto, pero
  reduce mucho el valor

**Resuelve esa pregunta antes de escribir el segundo pack.** Es lo que
define si esto es un proyecto o un repositorio abandonado en seis meses.
