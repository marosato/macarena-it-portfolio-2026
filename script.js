document.addEventListener("DOMContentLoaded", () => {
    setupNavigation();
    setupChatbot();
});

function setupNavigation() {
    const nav = document.querySelector(".nav-shell");
    const toggle = document.querySelector(".nav-toggle");
    const menuLinks = document.querySelectorAll(".nav-menu a");

    if (!nav || !toggle) return;

    toggle.addEventListener("click", () => {
        const isOpen = nav.classList.toggle("is-open");
        toggle.setAttribute("aria-expanded", String(isOpen));
    });

    menuLinks.forEach((link) => {
        link.addEventListener("click", () => {
            nav.classList.remove("is-open");
            toggle.setAttribute("aria-expanded", "false");
        });
    });
}

function setupChatbot() {
    const toggle = document.getElementById("chatbot-toggle");
    const box = document.getElementById("chatbot-box");
    const close = document.getElementById("chatbot-close");
    const form = document.getElementById("chatbot-form");
    const input = document.getElementById("chatbot-input");
    const messages = document.getElementById("chatbot-messages");

    if (!toggle || !box || !close || !form || !input || !messages) return;

    const suggestions = [
        "¿Quién eres?",
        "¿Qué tecnologías manejas?",
        "¿Tenés experiencia laboral?",
        "¿Qué estudias?",
        "¿Qué cursos hiciste?",
        "¿Cómo puedo contactarte?"
    ];

    const answers = [
        {
            match: ["quién eres", "quien eres", "quién sos", "quien sos"],
            text: "Soy Macarena Ayelén Rosato, profesional IT orientada a Sistemas, Soporte Técnico L2, backend, datos, automatización e inteligencia artificial."
        },
        {
            match: ["tecnologías", "tecnologias", "lenguajes", "stack", "herramientas"],
            text: "Trabajo con SQL, MySQL, MariaDB, PostgreSQL, MongoDB, Node.js, JavaScript, Java, Python, HTML, CSS, Postman, Jira, DBeaver, Excel, Git, GitHub, AWS, n8n, Make y ChatGPT."
        },
        {
            match: ["experiencia", "trabajo", "trabajaste", "laboral"],
            text: "Actualmente trabajo en IBBA GROUP, en el sector fintech. Participo en soporte técnico, análisis operativo, validación de datos, revisión de logs, pruebas de APIs, seguimiento de tickets y documentación de mejoras."
        },
        {
            match: ["estudias", "estudios", "formación", "formacion"],
            text: "Estoy cursando Analista de Sistemas en ORT Argentina y la Carrera de Desarrollo Backend en Coderhouse. Mi formación se enfoca en sistemas, programación, bases de datos, APIs, arquitectura y resolución de problemas."
        },
        {
            match: ["cursos", "certificaciones", "certificados"],
            text: "Tengo formación en AI Automation, SQL, JavaScript, Desarrollo Full Stack Java, AWS Cloud Computing, Desarrollo Full Stack Python, n8n e Inteligencia Artificial aplicada a productividad."
        },
        {
            match: ["contactarte", "contacto", "email", "linkedin"],
            text: "Podés escribirme a rosatomacarena@outlook.com o contactarme por LinkedIn: https://www.linkedin.com/in/macarena-ayelen-rosato/"
        },
        {
            match: ["dónde sos", "donde sos", "dónde eres", "donde eres"],
            text: "Soy de Buenos Aires, Argentina."
        },
        {
            match: ["inglés", "ingles", "idiomas"],
            text: "Tengo inglés avanzado escrito y oral, útil para documentación técnica, APIs, herramientas SaaS, investigación de errores y comunicación profesional."
        }
    ];

    function openChat() {
        box.hidden = false;
        toggle.setAttribute("aria-expanded", "true");
        if (!messages.dataset.ready) {
            resetChat();
            messages.dataset.ready = "true";
        }
        input.focus();
    }

    function closeChat() {
        box.hidden = true;
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
    }

    function resetChat() {
        messages.innerHTML = "";
        appendMessage("¡Hola! Soy el chatbot de Macarena. ¿En qué puedo ayudarte?", "bot", suggestions);
    }

    function getAnswer(value) {
        const normalized = normalize(value);
        const found = answers.find((answer) => answer.match.some((term) => normalized.includes(normalize(term))));
        return found
            ? found.text
            : "Puedo contarte sobre mi perfil, tecnologías, experiencia laboral, estudios, cursos, idiomas o formas de contacto.";
    }

    function appendMessage(text, sender, nextSuggestions = []) {
        const message = document.createElement("div");
        message.className = `chatbot-message ${sender}`;

        if (sender === "bot" && text.includes("https://")) {
            message.innerHTML = linkify(text);
        } else {
            message.textContent = text;
        }

        if (sender === "bot" && nextSuggestions.length > 0) {
            const container = document.createElement("div");
            container.className = "chatbot-suggestions";
            nextSuggestions.forEach((suggestion) => {
                const button = document.createElement("button");
                button.type = "button";
                button.textContent = suggestion;
                button.addEventListener("click", () => submitQuestion(suggestion));
                container.appendChild(button);
            });
            message.appendChild(container);
        }

        messages.appendChild(message);
        messages.scrollTop = messages.scrollHeight;
    }

    function submitQuestion(question) {
        appendMessage(question, "user");
        window.setTimeout(() => {
            appendMessage(getAnswer(question), "bot", suggestions.filter((item) => item !== question).slice(0, 4));
        }, 250);
    }

    toggle.addEventListener("click", () => {
        if (box.hidden) {
            openChat();
        } else {
            closeChat();
        }
    });

    close.addEventListener("click", closeChat);

    form.addEventListener("submit", (event) => {
        event.preventDefault();
        const value = input.value.trim();
        if (!value) return;
        input.value = "";
        submitQuestion(value);
    });
}

function normalize(value) {
    return value
        .toLowerCase()
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "");
}

function linkify(text) {
    return text.replace(
        /(https?:\/\/[^\s]+)/g,
        '<a href="$1" target="_blank" rel="noopener noreferrer">$1</a>'
    );
}
