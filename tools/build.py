"""Genera las páginas del portafolio bilingüe con Python 3."""
from pathlib import Path
from html import escape
import json
import os

ROOT = Path(__file__).resolve().parents[1]
SITE_URL = os.environ.get('PORTFOLIO_SITE_URL', '').rstrip('/')
LINKEDIN = 'https://www.linkedin.com/in/macarena-ayelen-rosato/'
STUDIO = 'https://marosato.github.io/MAR-Studio/'
EMAIL = 'mailto:rosatomacarena@outlook.com'
ARROW = '<span aria-hidden="true">↗</span>'
COURSES = json.loads((ROOT / 'tools/courses.json').read_text(encoding='utf-8'))
EN_TAGS = {'Agentes IA':'AI agents','Reportes':'Reporting','Eventos':'Events','Asistentes IA':'AI assistants','Productividad':'Productivity','Bases de datos':'Databases','Comunicación':'Communication','Trabajo en equipo':'Teamwork','Organización':'Organization','Adaptabilidad':'Adaptability','Infraestructura':'Infrastructure'}

def external(url, label, cls='text-link'):
    return f'<a class="{cls}" href="{escape(url, quote=True)}" target="_blank" rel="noopener noreferrer">{label} {ARROW}</a>'

def tags(values):
    return '<ul class="tags">' + ''.join(f'<li>{v}</li>' for v in values) + '</ul>'

def build(lang, page):
    en = lang == 'en'
    t = lambda es, eng: eng if en else es
    root = '../' if en else ''
    filename = page + '.html'
    home = 'index.html'
    titles = {'index': t('Sistemas y automatización', 'Systems & automation'), 'work': t('Experiencia', 'Experience'), 'education': t('Formación', 'Education'), 'courses': t('Cursos y certificaciones', 'Courses & certificates')}
    descriptions = {
        'index': t('Macarena Ayelén Rosato. Sistemas, datos y automatización. Proyectos web, experiencia técnica y servicios con MAR Studio.', 'Macarena Ayelén Rosato. Systems, data and automation. Web projects, technical experience and services through MAR Studio.'),
        'work': t('Experiencia de Macarena Ayelén Rosato: soporte técnico, QA, automatización y coordinación de proyectos en una empresa del sector fintech.', 'Macarena Ayelén Rosato’s experience: technical support, QA, automation and project coordination at a fintech company.'),
        'education': t('Formación académica de Macarena Ayelén Rosato: Analista de Sistemas en ORT y base en Economía y Administración.', 'Macarena Ayelén Rosato’s academic background: Systems Analysis at ORT and secondary education in Economics and Administration.'),
        'courses': t('Cursos y certificaciones de Macarena Ayelén Rosato en backend, SQL, JavaScript, automatización, IA, desarrollo full stack y AWS.', 'Macarena Ayelén Rosato’s courses and certificates in backend development, SQL, JavaScript, automation, AI, full stack development and AWS.')}
    desc = descriptions[page]
    links = [(home+'#projects', t('Proyectos','Projects')), ('work.html',t('Experiencia','Experience')), ('education.html',t('Formación','Education')), ('courses.html',t('Cursos','Courses'))]
    nav = ''.join(f'<a href="{url}"'+(' aria-current="page"' if url==filename else '')+f'>{label}</a>' for url,label in links)
    spanish = '../'+filename if en else filename
    english = filename if en else 'en/'+filename
    canonical = ''
    if SITE_URL:
        spanish = SITE_URL+'/'+filename
        english = SITE_URL+'/en/'+filename
        canonical = f'<link rel="canonical" href="{english if en else spanish}"><meta property="og:url" content="{english if en else spanish}">'
    head = f'''<!doctype html>
<html lang="{lang}" data-theme="light">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{"Macarena Ayelén Rosato" if page == "index" else "Macarena Ayelén Rosato — " + titles[page]}</title>
<meta name="description" content="{desc}">
<meta name="color-scheme" content="light dark">
{canonical}
<meta property="og:title" content="Macarena Ayelén Rosato — {titles[page]}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<meta property="og:locale" content="{'en_US' if en else 'es_AR'}">
<meta property="og:image" content="https://marosato.github.io/portfolio/img/Logo%20-%20MAR.png">
<link rel="alternate" hreflang="es" href="{spanish}"><link rel="alternate" hreflang="en" href="{english}"><link rel="alternate" hreflang="x-default" href="{spanish}">
<link rel="icon" href="{root}img/Logo%20-%20MAR.png">
<link rel="stylesheet" href="{root}main.css?v=20261124-name"><script src="{root}script.js" defer></script>
</head><body>
<a class="skip-link" href="#main">{t('Saltar al contenido','Skip to content')}</a>
<header class="site-header"><div class="header-inner">
<a class="brand" href="{home}" aria-label="{t('Macarena Ayelén Rosato, inicio','Macarena Ayelén Rosato, home')}">Macarena Ayelén Rosato<span class="brand-dot">.</span></a>
<button class="menu-toggle" hidden type="button" aria-controls="navigation" aria-expanded="false">{t('Menú','Menu')} <span aria-hidden="true">☰</span></button>
<nav id="navigation" aria-label="{t('Navegación principal','Main navigation')}">{nav}<a href="{home}#contact">{t('Contacto','Contact')}</a></nav>
<div class="header-tools"><div class="languages" aria-label="{t('Idioma','Language')}"><a href="{spanish}" lang="es" hreflang="es" {'aria-current="true"' if not en else ''}>ES</a><span aria-hidden="true">/</span><a href="{english}" lang="en" hreflang="en" {'aria-current="true"' if en else ''}>EN</a></div>
<button class="theme-toggle" hidden type="button" aria-label="{t('Activar modo oscuro','Switch to dark mode')}" aria-pressed="false"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><circle cx="12" cy="12" r="8"/><path d="M12 4a8 8 0 0 0 0 16Z"/></svg></button></div>
</div></header><main id="main">'''

    def intro(kicker, title, text):
        return f'<section class="page-intro wrap"><p class="eyebrow">{kicker}</p><h1>{title}</h1><p class="intro-text">{text}</p></section>'

    def heading(number, label, title, aside=''):
        return f'<div class="section-heading"><div><p class="eyebrow">{number} / {label}</p><h2>{title}</h2></div>{aside}</div>'

    def contact():
        return f'''<section class="contact wrap" id="contact"><p class="eyebrow">{t('Contacto','Contact')}</p><div class="contact-grid"><h2>{t('Consultas y<br><em>propuestas de trabajo.</em>','Project inquiries and<br><em>job opportunities.</em>')}</h2><div><p>{t('Puedes escribirme por una oportunidad laboral o para consultar sobre desarrollo web y automatización.','Email me about a job opportunity or to discuss web development and automation services.')}</p><a class="contact-mail" href="{EMAIL}">{t('Enviar un correo','Send an email')} {ARROW}</a><div class="social-links">{external(LINKEDIN,'LinkedIn')}{external('https://github.com/marosato','GitHub')}</div></div></div></section>'''

    def capabilities():
        items = [
            (t('Análisis de datos','Data analysis'),t('Consultas SQL, comparación de registros y reportes para detectar diferencias entre operaciones.','SQL queries, record comparisons and reports to identify differences between operations.'),'SQL · SQL Server / SSMS · MySQL · Excel'),
            (t('APIs e integraciones','APIs and integrations'),t('Pruebas de APIs, lectura de logs y validación de transacciones para seguir el recorrido de un problema.','API testing, log analysis and transaction validation to trace a problem across systems.'),'Postman · REST APIs · JSON · Jira'),
            (t('Automatización de tareas','Task automation'),t('Flujos de automatización e IA aplicada para reducir pasos repetitivos y ordenar información.','Automation workflows and applied AI to reduce repetitive steps and organize information.'),'n8n · Make · Python · VBA'),
            (t('Desarrollo y pruebas','Development and testing'),t('Desarrollo de sitios web y aplicaciones backend. Pruebas funcionales para comprobar que respondan a lo esperado.','Website and backend application development. Functional testing to check that they behave as expected.'),'JavaScript · Node.js · MongoDB · QA')]
        examples = [
            (t('En mi puesto anterior utilicé SQL, MySQL y Excel para revisar datos y preparar reportes.','In my previous role, I used SQL, MySQL and Excel to review data and prepare reports.'),'work.html#job-2',t('Ver experiencia','View experience')),
            (t('En mi puesto anterior probé APIs con Postman y realicé tareas de QA para comprobar el funcionamiento de las integraciones.','In my previous role, I tested APIs with Postman and performed QA checks on integrations.'),'work.html#job-2',t('Ver tareas del puesto anterior','View previous responsibilities')),
            (t('En mi puesto anterior preparé reportes, macros y automatizaciones en Excel y trabajé con automatizaciones de IA. Mi formación también incluye n8n y Make.','In my previous role, I prepared Excel reports, macros and automations, and worked with AI automation. My training also includes n8n and Make.'),'courses.html',t('Ver formación en automatización','View automation training')),
            (t('En los proyectos puedes consultar los sitios publicados, mi aporte y los repositorios de código.','The projects include links to the published websites, my contributions and the code repositories.'),'index.html#projects',t('Explorar proyectos','Explore projects'))]
        return ''.join(f'<article class="capability"><span class="item-number">0{i}</span><div><h3>{a}</h3><p>{b}</p><p class="tool-line">{c}</p><details class="skill-detail"><summary>{t("Cómo lo aplico","How I use it")}</summary><p>{examples[i-1][0]}</p><a class="text-link" href="{examples[i-1][1]}">{examples[i-1][2]} {ARROW}</a></details></div></article>' for i,(a,b,c) in enumerate(items,1))


    if page == 'index':
        body = f'''<section class="hero wrap" id="home"><div class="hero-copy"><p class="eyebrow"><span class="small-line"></span> {t('Sistemas · Datos · Automatización','Systems · Data · Automation')}</p><h1>Macarena<br><span>Ayelén Rosato<span class="accent">.</span></span></h1><p class="hero-statement">{t('Desarrolladora SQL.<br><em>Datos y automatización.</em>','SQL Developer.<br><em>Data and automation.</em>')}</p><p class="hero-description">{t('Trabajo con SQL en Microsoft SQL Server Management Studio y gestiono tickets en Jira. También desarrollo sitios web y automatizo tareas con Python, n8n y Make.','I work with SQL in Microsoft SQL Server Management Studio and manage tickets in Jira. I also develop websites and automate tasks with Python, n8n and Make.')}</p><div class="hero-actions"><a class="button" href="work.html">{t('Ver mi experiencia','Explore my experience')} {ARROW}</a><a class="button" href="#contact">{t('Trabajemos juntos','Let’s work together')} {ARROW}</a></div><div class="hero-footnote"><span>SQL / APIs / n8n</span><a href="#about">{t('Un poco sobre mí','A little about me')} <span aria-hidden="true">↓</span></a></div></div>
<figure class="portrait"><div class="portrait-top"><span>{t('TECNOLOGÍA CON PROPÓSITO','TECHNOLOGY WITH PURPOSE')}</span><span aria-hidden="true">✳</span></div><img src="{root}assets/portrait.webp" srcset="{root}assets/portrait-small.webp 480w, {root}assets/portrait.webp 900w" sizes="(max-width: 760px) 90vw, 40vw" alt="{t('Retrato de Macarena Ayelén Rosato','Portrait of Macarena Ayelén Rosato')}" width="900" height="602" fetchpriority="high"><figcaption><span>{t('Entre la lógica<br>y las ideas.','Between logic<br>and ideas.')}</span><span class="portrait-signature">MAR</span></figcaption></figure></section>
<nav class="explore-paths wrap" aria-label="{t('Explorar el perfil','Explore the portfolio')}"><p>{t('¿Qué quieres conocer?','What would you like to explore?')}</p><a href="#experience">{t('Experiencia y herramientas','Experience and tools')} <span aria-hidden="true">↓</span></a><a href="#mar-studio">{t('Servicios para un proyecto','Services for a project')} <span aria-hidden="true">↓</span></a><a href="#projects">{t('Proyectos desarrollados','Web projects')} <span aria-hidden="true">↓</span></a></nav>
<section class="about profile-overview wrap" id="about"><span id="experience" class="anchor-alias"></span><div><p class="eyebrow">{t('Mi perfil profesional','My professional background')}</p><h2>{t('Mi experiencia laboral.','My work experience.')}</h2><p>{t('Soy estudiante avanzada de Analista de Sistemas en ORT. Mi experiencia combina trabajo con datos, pruebas de software y automatización de tareas.','I’m an advanced Systems Analysis student at ORT. My experience combines data work, software testing and task automation.')}</p><a class="text-link" href="work.html">{t('Ver mi recorrido completo','View my full experience')} {ARROW}</a></div><div class="profile-roles"><article><p class="eyebrow">{t('Noviembre 2024 — Agosto 2026 · 1 año y 9 meses','November 2024 — August 2026 · 1 year, 9 months')}</p><h3>{t('Soporte técnico','Technical support')}</h3>{t('Empresa del sector fintech','Fintech company')}<p>{t('SQL, MySQL, Postman y APIs. Reportes y macros en Excel, automatizaciones con IA, QA y coordinación de nuevos proyectos.','SQL, MySQL, Postman and APIs. Excel reports and macros, AI automations, QA and coordination of new projects.')}</p></article></div></section>
<section class="projects wrap section" id="projects"><span id="portfolio" class="anchor-alias"></span>{heading('01',t('Proyectos seleccionados','Selected projects'),t('Sitios web que <em>desarrollé.</em>','Websites I’ve <em>developed.</em>'),external('https://github.com/marosato',t('Más en GitHub','More on GitHub')))}<p class="projects-note">{t("Estos proyectos fueron diseñados y desarrollados íntegramente por mí.","I designed and developed each of these projects independently.")}</p><div class="project-grid">'''
        projects = [
            ('EMME Creations','emme',t('Marca y presencia digital','Brand & digital presence'),t('Un espacio para presentar servicios de contenido, redes sociales y diseño web.','A space for content, social media and web design services.'),t('Diseño y desarrollo de la web de mi proyecto de servicios digitales.','Website design and development for my digital services project.'),'HTML · CSS · JavaScript','https://emmecreations.netlify.app/','EMME-Creations'),
            ('CAC Movies','movies',t('Proyecto académico','Academic project'),t('Un catálogo de películas como práctica de desarrollo web en Codo a Codo.','A movie catalog built as a web development exercise at Codo a Codo.'),t('Estructura, estilos y navegación del trabajo práctico.','Page structure, styling and navigation for the coursework project.'),'HTML · CSS · JavaScript','https://marosato.github.io/CAC-Movies/','CAC-Movies'),
            ('Kéfir Argentina','kefir',t('Web informativa','Informational website'),t('Contenido educativo sobre kéfir, organizado en una experiencia de lectura simple.','Educational content about kefir, organized into a simple reading experience.'),t('Desarrollo de la interfaz y organización del contenido web.','Interface development and web content organization.'),'HTML · CSS · JavaScript · Bootstrap','https://kefir-argentina.vercel.app/','KEFIR-ARGENTINA')]
        features = [
            t('Presentación de la marca, secciones de servicios y acceso a planes desde la navegación principal.','Brand introduction, service sections and access to plans from the main navigation.'),
            t('Catálogo visual de películas, navegación por páginas y una sección de títulos destacados. Proyecto realizado como práctica académica.','A visual movie catalog, page navigation and a featured titles section. Built as an academic exercise.'),
            t('Contenido organizado por temas, navegación por secciones y preguntas frecuentes desplegables.','Content organized by topic, section navigation and expandable frequently asked questions.')]
        for i,(name,img,kind,purpose,role,stack,url,repo) in enumerate(projects,1):
            logo = 'assets/movies.webp' if img == 'movies' else 'assets/'+img+'.webp'
            body += f'''<article class="project-case"><div class="case-overview"><a class="case-preview project-logo {img}" href="#project-{i}" data-project-link aria-label="{t('Ver detalles de','View details for')} {escape(name)}"><img src="{root}{logo}" alt="{t('Portada de','Cover for')} {escape(name)}" width="640" height="640" loading="lazy"></a><div class="case-copy"><p class="eyebrow">0{i} / {kind}</p><h3>{name}</h3><p>{purpose}</p>{tags(stack.split(' · '))}<div class="project-links">{external(url,t('Ver sitio','Visit website'))}{external('https://github.com/marosato/'+repo,t('Ver código','View code'))}</div></div></div><details class="case-details" id="project-{i}"><summary>{t('Ver detalles','View details')}<span aria-hidden="true">＋</span></summary><div class="case-expanded"><p>{features[i-1]}</p></div></details></article>'''
        body += f'''</div></section>
<section class="wrap section" id="skills"><span id="tech-stack" class="anchor-alias"></span>{heading('02',t('Habilidades','Capabilities'),t('Qué hago y<br><em>qué herramientas uso.</em>','What I do and<br><em>the tools I use.</em>'))}<div class="capabilities">{capabilities()}</div></section>
<section class="studio wrap" id="mar-studio"><div class="studio-art" aria-hidden="true"><span class="studio-orbit"></span><span class="studio-word">MAR<span>STUDIO</span></span><span class="studio-star">✳</span><span class="studio-art-note">WEB · AUTOMATION · AI</span></div><div class="studio-copy"><p class="eyebrow">03 / {t('Servicios con MAR Studio','Services through MAR Studio')}</p><h2>{t('Desarrollo web<br>y <em>automatización.</em>','Web development<br>and <em>automation.</em>')}</h2><p>{t('MAR Studio es mi proyecto de servicios digitales. Diseño y desarrollo sitios web, preparo automatizaciones e integro herramientas de IA según las necesidades de cada proyecto.','MAR Studio is my digital services project. I design and develop websites, build automations and integrate AI tools according to each project’s needs.')}</p><ul class="service-deliverables"><li><h3>{t('Sitios web','Websites')}</h3><p>{t('Diseño y desarrollo de páginas adaptadas a móvil, tableta y escritorio.','Design and development of pages for phones, tablets and desktops.')}</p></li><li><h3>{t('Automatización de tareas','Task automation')}</h3><p>{t('Flujos para conectar herramientas, organizar datos y preparar reportes.','Workflows that connect tools, organize data and prepare reports.')}</p></li><li><h3>{t('Integración de IA','AI integration')}</h3><p>{t('Asistentes y flujos con IA para tareas definidas dentro de un proceso.','AI assistants and workflows for defined tasks within a process.')}</p></li></ul>{external(STUDIO,t('Ver MAR Studio','Explore MAR Studio'),'button studio-button')}</div></section>
<section class="learning wrap" id="certifications"><div><p class="eyebrow">04 / {t('Formación continua','Continuous learning')}</p><h2>{t('Estudios y<br><em>cursos realizados.</em>','Education and<br><em>professional courses.</em>')}</h2></div><div><a class="learning-row" href="education.html"><span><small>ORT ARGENTINA</small>{t('Analista de Sistemas','Systems Analysis')}</span>{ARROW}</a><a class="learning-row" href="courses.html"><span><small>CODERHOUSE · EDUCACIÓNIT · UTN</small>{t('Backend, automatización y datos','Backend, automation & data')}</span>{ARROW}</a></div></section>'''
    elif page == 'work':
        body = intro(t('Mi recorrido profesional','My professional journey'),t('Mi experiencia<br><em>profesional.</em>','My professional<br><em>experience.</em>'),t('Mi experiencia incluye soporte técnico, QA, automatización y coordinación de proyectos en fintech, además de contenido digital.','My experience includes technical support, QA, automation and project coordination in fintech, as well as digital content.'))
        jobs = [
            (t('Empresa del sector fintech','Fintech company'),t('Noviembre 2024 — Agosto 2026 · 1 año y 9 meses','November 2024 — August 2026 · 1 year, 9 months'),t('Soporte técnico','Technical support'),t('Trabajé en soporte técnico de productos financieros digitales. Además, realicé tareas de QA, automatización y coordinación de nuevos proyectos.','I worked in technical support for digital financial products, alongside QA, automation and coordination of new projects.'),[t('Consultas y revisión de datos con SQL y MySQL.','Queries and data reviews using SQL and MySQL.'),t('Pruebas de APIs e integraciones con Postman.','API and integration testing with Postman.'),t('Reportes, macros y automatizaciones en Excel.','Excel reports, macros and automations.'),t('Gestión y seguimiento de tickets en Jira.','Managing and tracking tickets in Jira.'),t('Automatización de tareas con herramientas de IA.','Task automation using AI tools.'),t('Pruebas de calidad (QA) y documentación de resultados.','Quality assurance (QA) testing and documentation of results.'),t('Coordinación y seguimiento de nuevos proyectos.','Coordinating and tracking new projects.')],['SQL','MySQL','Postman','APIs','Excel','Jira','IA / AI','QA'],''),
            (external('https://www.instagram.com/grupolumaseguros/','Grupo Luma Seguros','company-link'),t('Julio — Agosto 2024','July — August 2024'),t('Contenido digital','Digital content'),t('Diseñé contenido y organicé publicaciones para las redes sociales de Grupo Luma Seguros.','I designed content and organized social media posts for Grupo Luma Seguros.'),[t('Diseño de piezas visuales y contenido con Canva.','Designed visuals and content using Canva.'),t('Organización y publicación de contenido para redes sociales.','Organized and published social media content.'),t('Revisión de interacciones y métricas para orientar las publicaciones.','Reviewed engagement and metrics to guide future posts.')],['Canva',t('Comunicación','Communication')],external('https://www.instagram.com/grupolumaseguros/',t('Ver la marca','View the brand')))]
        body += '<section class="wrap timeline" aria-label="'+t('Historial laboral','Work history')+'">'
        for job_index,(org,date,title,description,bullets,tools,link) in enumerate(jobs,2):
            body += f'<article class="timeline-entry" id="job-{job_index}"><div class="timeline-aside"><p class="eyebrow">{org}</p><p>{date}</p></div><div><h2>{title}</h2><p class="entry-lead">{description}</p><ul class="detail-list">'+''.join(f'<li>{b}</li>' for b in bullets)+f'</ul>{tags(tools)}{link}</div></article>'
        body += '</section><section class="wrap process-section"><p class="eyebrow">'+t('Mi forma de trabajar','How I work')+'</p><div class="process-grid">'
        for i,(es,eng,esd,engd) in enumerate([('Entender','Understand','Síntoma, contexto e impacto.','Symptoms, context and impact.'),('Investigar','Investigate','Datos, logs e integraciones.','Data, logs and integrations.'),('Validar','Validate','Hipótesis, pruebas y evidencia.','Hypotheses, tests and evidence.'),('Comunicar','Communicate','Hallazgos y próximos pasos.','Findings and next steps.')],1):
            body += f'<article><span class="item-number">0{i}</span><h3>{t(es,eng)}</h3><p>{t(esd,engd)}</p></article>'
        body += '</div></section>'
    elif page == 'education':
        body = intro(t('Formación académica','Academic education'),t('Mi formación<br><em>académica.</em>','My academic<br><em>education.</em>'),t('Estudio Analista de Sistemas en ORT, donde me formo en programación, bases de datos, análisis funcional y gestión de proyectos.','I study Systems Analysis at ORT, with coursework in programming, databases, functional analysis and project management.'))
        records = [
            ('ORT Argentina',t('Desde marzo de 2024','Since March 2024'),t('Analista de Sistemas','Systems Analysis'),t('Estudiante avanzada','Advanced student'),t('Programación, bases de datos, análisis funcional, infraestructura, seguridad, testing y gestión de proyectos.','Programming, databases, functional analysis, infrastructure, security, testing and project management.'),[t('Modelado de información y estructuras de datos.','Information modeling and data structures.'),t('Análisis de requerimientos y diseño de soluciones.','Requirements analysis and solution design.'),t('Documentación y fundamentos de arquitectura de sistemas.','Documentation and systems architecture foundations.')]),
            ('Colegio José Ingenieros',t('2016 — 2018','2016 — 2018'),t('Bachiller en Economía<br>y Administración','Secondary education in<br>Economics & Administration'),t('Educación secundaria','Secondary education'),t('Formación secundaria con orientación en economía, administración y organización de empresas.','Secondary education focused on economics, administration and business organization.'),[t('Administración, economía y organización.','Administration, economics and organization.'),t('Comunicación y comprensión de procesos operativos.','Communication and understanding operational processes.')])]
        body += '<section class="wrap timeline" aria-label="'+t('Trayectoria académica','Academic background')+'">'
        for org,date,title,status,description,bullets in records:
            body += f'<article class="timeline-entry"><div class="timeline-aside"><p class="eyebrow">{org}</p><p>{date}</p></div><div><p class="status-label">{status}</p><h2>{title}</h2><p class="entry-lead">{description}</p><ul class="detail-list">'+''.join(f'<li>{b}</li>' for b in bullets)+'</ul></div></article>'
        body += f'</section><aside class="wrap next-page"><p>{t("También puedes consultar mis cursos y certificados.","You can also browse my courses and certificates.")}</p><a class="text-link" href="courses.html">{t("Ver cursos y certificaciones","Explore courses & certificates")} {ARROW}</a></aside>'
    else:
        body = intro(t('Cursos y certificaciones','Courses & certificates'),t('Cursos y<br><em>certificaciones.</em>','Courses and<br><em>certificates.</em>'),t('Aquí reúno mi formación en backend, datos, automatización e IA, con enlaces a los programas y certificados disponibles.','My training in backend development, data, automation and AI, with links to available syllabi and certificates.'))
        body += f'<section class="wrap course-section"><p class="document-note">{t("Los certificados y programas se abren en su idioma original.","Certificates and syllabi open in their original language.")}</p><div class="course-search" hidden><label for="course-query">{t("Buscar por tema, herramienta o institución","Search by topic, tool or institution")}</label><div class="search-controls"><input id="course-query" type="search" placeholder="{t('Por ejemplo: SQL, n8n, Coderhouse','For example: SQL, n8n, Coderhouse')}" aria-controls="course-results"><button type="button" class="button" data-clear-search>{t("Limpiar búsqueda","Clear search")}</button></div><p class="search-count" role="status" aria-live="polite"></p></div><div class="course-grid" id="course-results">'
        for course in COURSES:
            title = course['en_title'] if en else course['title']
            description = course['en_description'] if en else course['description']
            course_tags = [EN_TAGS.get(tag,tag) for tag in course['tags']] if en else course['tags']
            body += f'<article class="course"><p class="eyebrow">{course["provider"]}</p><h2>{title}</h2><p>{description}</p>{tags(course_tags)}<div class="course-links">'
            for link in course['links']:
                url = link['url'] if link['url'].startswith('http') else root+link['url']
                label = link['en_label'] if en else link['label']
                body += external(url,label)
            body += '</div></article>'
        body += '</div></section>'

    footer = f'''</main><footer class="site-footer wrap"><a class="brand" href="index.html">Macarena Ayelén Rosato<span class="brand-dot">.</span></a><p>© 2026 · {t('Sistemas y automatización.','Systems and automation.')}</p><a href="#main">{t('Volver arriba','Back to top')} <span aria-hidden="true">↑</span></a></footer></body></html>'''
    output = ROOT / ('en' if en else '') / filename
    output.parent.mkdir(exist_ok=True)
    output.write_text(head+body+contact()+footer,encoding='utf-8')

for lang in ['es','en']:
    for page in ['index','work','education','courses']:
        build(lang,page)
    (ROOT / ('en' if lang=='en' else '') / 'chatbot.html').write_text(f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta http-equiv="refresh" content="0; url=index.html#contact"><meta name="robots" content="noindex"><title>{'Contact' if lang=='en' else 'Contacto'} | Macarena Ayelén Rosato</title></head><body><a href="index.html#contact">{'Contact Macarena' if lang=='en' else 'Contactar a Macarena'}</a></body></html>''',encoding='utf-8')
print('Generated 8 content pages and 2 contact redirects.')
