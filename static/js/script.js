
const cardMessages = [
    "Eres mi mundo y mi inspiración 🌎❤️",
    "Gracias por llenar mis días de amor y alegría 🥰",
    "Eres la persona que siempre soñé 💭💕",
    "Cada día contigo es una bendición 🙏💖",
    "Te amo más de lo que las palabras pueden expresar 🌟",
    "Nuestro amor es lo mejor que me ha pasado 💑",
    "Eres mi todo, mi alma gemela 🤝💞",
    "Cada momento contigo es inolvidable ✨",
    "Siempre estaré contigo, pase lo que pase 🫶"
];

function showCard(index) {
    const modal = document.getElementById('card-modal');
    const cardText = document.getElementById('card-text');
    cardText.textContent = cardMessages[index - 1];
    modal.classList.remove('hidden');
}

function closeCard() {
    const modal = document.getElementById('card-modal');
    modal.classList.add('hidden');
}