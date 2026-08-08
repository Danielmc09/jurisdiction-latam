---
modulo: saas-multitenant
aplica_a: arquitectura de negocio, no a un sector
jurisdiccion: CO
verificado: 2026-08-08
validado_por: NO VALIDADO
---

# SaaS multi-tenant — cadena Responsable / Encargado

> Módulo **transversal por arquitectura de negocio**, no por sector.
> Aplica a cualquier plataforma B2B2C donde el cliente del cliente aporta
> los datos: agendamiento, facturación, salud, educación, logística.
>
> Las referencias normativas de abajo son de Colombia. Un módulo por país.

> Módulo transversal. Aplica a cualquier plataforma B2B2C donde el cliente
> del cliente aporta los datos.

**La cadena**

| Actor | Rol | Sobre qué datos |
|---|---|---|
| La plataforma | **Encargado** | Datos de los clientes finales de cada tenant |
| La plataforma | **Responsable** | Datos del administrador del tenant y de sus propios leads |
| El tenant | **Responsable** | Datos de sus clientes finales |
| El cliente final | Titular | Sus propios datos |

- [oficial] 2026-08-08 · Art. 18, parágrafo: cuando concurran las calidades de Responsable y Encargado en la misma persona, **le son exigibles los deberes de cada una**. Una plataforma multi-tenant siempre es las dos

**Almacenar es tratamiento**
- [oficial] 2026-08-08 · El Tratamiento incluye recolección, almacenamiento, uso, circulación y supresión. Guardar en base de datos es tratamiento
- [secundaria] 2026-08-08 · El cifrado es cumplimiento del deber de seguridad (art. 4 lit. g), **no cambia el rol**. Con las llaves en tu poder, los datos siguen siendo datos personales en tu poder

**Cambio de rol por finalidad propia**
- [secundaria] 2026-08-08 · Los roles los definen los hechos. Usar los datos del tenant para finalidad propia —analítica agregada, entrenar modelos, marketing— convierte a la plataforma en **Responsable de ese uso**, con sus obligaciones. Debe autorizarse antes, no después

**Documentos que la cadena exige**

| Documento | Entre quién | Por qué |
|---|---|---|
| Términos y condiciones | Plataforma ↔ tenant | Contrato de adhesión |
| **Acuerdo de encargo** | Plataforma ↔ tenant | **El que prueba que actúas por instrucción** |
| Política de tratamiento | Pública | Obligatoria |
| Aviso de privacidad | Donde se recojan datos | Obligatorio |
| Autorización del titular | Tenant ↔ cliente final | La consigue el tenant, no la plataforma |
| **Manual interno** | Interno de la plataforma | Art. 18 lit. f — **no es la política** |

- [oficial] 2026-08-08 · La SIC sancionó con 20 SMLMV a un Encargado que aportó su política de tratamiento creyendo que suplía el manual interno del art. 18 lit. f · https://www.sic.gov.co/boletin-juridico-octubre-2018

**Momento de aceptación del acuerdo de encargo**
- [secundaria] 2026-08-08 · Conviene pedirlo **al cargar el primer dato de un tercero**, no en el registro. Deja evidencia de que el tenant asumió su rol en el momento exacto en que empezó a tratar datos ajenos

**Requisitos de producto que la ley impone**
- [oficial] 2026-08-08 · Estados `reclamo en trámite` e `información en discusión judicial` sobre el dato — son estados de base de datos, no papeles
- [oficial] 2026-08-08 · Acceso restringido únicamente a personas autorizadas
- [oficial] 2026-08-08 · Canal de notificación de incidentes a la autoridad
- [secundaria] 2026-08-08 · Versionado de textos aceptados con fecha y hash, para poder probar **qué** se aceptó
- [secundaria] 2026-08-08 · Exportación y supresión verificable, incluida la propagación a copias de respaldo

## Huecos declarados
- [no-verificado] 2026-08-08 · Plazos legales para responder consultas y reclamos → ABOGADO
- [no-verificado] 2026-08-08 · Plazo y umbral de gravedad para notificar incidentes a la SIC → ABOGADO
- [no-verificado] 2026-08-08 · Si destruir la llave de cifrado cuenta como supresión válida → ABOGADO
- [no-verificado] 2026-08-08 · Qué hacer con los datos si el tenant desaparece sin exportar → ABOGADO

---
