# Instrucciones para asistentes de IA

Actualizado: 24 de noviembre de 2026. Aplica a todo el repositorio.
Las instrucciones nuevas de la propietaria prevalecen sobre este documento. No recuperar preferencias antiguas de maquetas, copias o archivos locales de contexto si contradicen estas reglas.

## Identidad y contenido

- Nombre y título del inicio: **Macarena Ayelén Rosato**. Usar el nombre completo en la cabecera, pie, accesibilidad y metadatos. Conservarlo también en inglés.
- Portafolio personal de sistemas, datos y automatización; MAR Studio es su espacio de servicios.
- No mostrar el puesto actual en Experiencia ni en el resumen del inicio. No publicar el nombre o enlace de la empresa actual en páginas, metadatos ni documentación.
- El empleo anterior se identifica únicamente como «Empresa del sector fintech» / «Fintech company», sin nombre ni enlace de la empresa.
- Experiencia fintech: soporte técnico, noviembre de 2024 a agosto de 2026, 1 año y 9 meses. SQL, MySQL, Postman, APIs, Excel (reportes, macros y automatizaciones), Jira, automatizaciones con IA, QA y coordinación de nuevos proyectos. No usar «L2» ni inventar un cargo formal de Project Manager.
- No incluir enlaces al CV. La dirección de correo no debe aparecer como texto visible; mantener «Enviar un correo» / «Send an email» con su enlace mailto. No añadir botón para copiar la dirección.
- No incorporar documentos fiscales, datos personales innecesarios, resultados, testimonios, proyectos o métricas sin respaldo.
- Redacción clara, concreta y neutral; evitar clichés, frases genéricas y tono robótico.

## Diseño y proyectos

- Conservar la foto, su encuadre y su marco cuadrado sin cambios.
- Mantener marfil, texto oscuro y terracota; serif editorial y sans serif para lectura. Tema claro predeterminado y modo oscuro opcional.
- Texto pequeño legible, esquinas suaves y movimiento reducido respetado. No reincorporar los iconos decorativos de Habilidades.
- EMME Creations y Kéfir Argentina usan sus logos propios. CAC Movies usa la portada original `assets/movies.webp`, no el icono de claqueta. Mantener imágenes grandes, sin deformación ni recortes arbitrarios.
- Todos los proyectos fueron realizados íntegramente por Macarena. No usar «Mi aporte» / «My contribution» ni sugerir trabajo compartido.
- La galería de tres columnas fue recomendada en una revisión UX/UI, pero no fue aprobada ni implementada. No tratarla como requisito confirmado. La versión actual conserva filas con imágenes grandes.
- Preservar anclas antiguas y el resumen profesional restante. Las anclas invisibles no deben ocupar celdas de la cuadrícula.

## Idioma de la documentación

- Escribir en español todos los comentarios de código, mensajes de commit, descripciones de cambios y comentarios publicados en el repositorio. Esto no cambia la versión inglesa del sitio.
- Mantener el README breve: descripción, vista previa y estructura básica. No incluir pedidos personales ni el historial de decisiones.

## Fuentes y edición

- Sitio estático HTML/CSS/JavaScript, sin framework ni servidor de aplicaciones.
- Editar contenido y plantillas en `tools/build.py`, no únicamente en HTML generado. Ejecutar `python tools/build.py` después.
- Cursos y enlaces: `tools/courses.json`. Estilos: `main.css`. Comportamiento: `script.js`.
- Aplicar cambios a español e inglés. Rutas: `index.html`, `work.html`, `education.html`, `courses.html` y equivalentes bajo `en/`. `chatbot.html` conserva el acceso compatible a contacto.
- Contenido principal legible sin JavaScript. No añadir formularios que requieran servidor.
- Preservar cambios locales y maquetas. No versionar `.codex/`, `.agents/`, ZIP, respaldos ni documentación privada.
- No fijar canónicos sin verificar el destino público. `PORTFOLIO_SITE_URL` permite configurarlos al generar.

## Verificación y entrega

- Ejecutar `node --check script.js` y `python tools/package.py portfolio.zip`. Este último comprueba archivos locales, anclas e identificadores.
- Para cambios visuales, revisar las páginas afectadas en escritorio, tableta y móvil, en ambos idiomas y temas; comprobar teclado, foco, menú y ausencia de desbordamientos.
- Los scripts de pruebas locales anteriores pueden contener expectativas obsoletas; contrastarlos con estas preferencias antes de usarlos.
- Vista previa: `python -m http.server 4173 --bind 127.0.0.1`. Comprobar que responde antes de entregar el enlace. Es local, no una URL pública.
- Repositorio: `https://github.com/marosato/macarena-it-portfolio-2026.git`. Antes de subir cambios, revisar el remoto y el diff, excluir información privada y verificar el resultado del push. No desplegar ni modificar alojamiento por iniciativa propia.
