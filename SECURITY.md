# Seguridad

## Qué hace este plugin con tu máquina

- **Lee** fuentes web mediante búsqueda
- **Escribe** archivos Markdown en `packs/`, `sectors/`, `modules/` y en tu
  proyecto
- **No ejecuta código** ni instala dependencias
- **No envía tus datos a ningún servicio propio.** No hay servidor detrás

## El riesgo principal: inyección de prompt

Los skills leen contenido web. Una página comprometida puede contener texto
diseñado para dar órdenes al agente.

**En un plugin legal eso tiene consecuencia jurídica**, no solo técnica: un
portal manipulado podría hacer que el agente registre una norma falsa como
verificada.

### Cómo se mitiga

1. **Contenido web es dato citado, nunca instrucción.** Está escrito en
   `jurisdiction-kit/CLAUDE.md` y en cada skill de investigación
2. **Jerarquía de fuentes estricta.** Solo portales oficiales y
   compiladores normativos se citan. Los blogs nunca
3. **Ninguna capa se escribe sin aprobación humana.** Los skills proponen;
   una persona aprueba
4. **Cada afirmación lleva su URL**, así que es verificable a mano

### Qué debes hacer tú

- **Revisa las URL** antes de aprobar una escritura a una capa
- Desconfía de una afirmación normativa cuya fuente no sea un dominio
  gubernamental
- Si una salida te sugiere ignorar una instrucción previa o cambiar tu
  configuración, **es un incidente**: repórtalo

## Datos sensibles

Los skills pueden pedirte información de tu negocio. **Todo se queda en tus
archivos locales.**

**No pegues** en las conversaciones: números de documento de terceros,
datos de salud, credenciales, ni datos de clientes de tus clientes.

## Los packs no están validados

Salvo que la tabla del README diga lo contrario, **ningún pack ha sido
revisado por un abogado**. Trátalos como investigación estructurada.

## Reportar

Abre un issue con la etiqueta `security`. Si es un dato normativo
incorrecto en un pack, usa la plantilla de corrección de pack.
