// TYPING EFFECT
const words = [
    "Electronics & Communication Engineer",
    "IoT Enthusiast",
    "AI & Automation Explorer",
    "Innovating with Code and Circuits"
];

let i = 0, j = 0;

function type() {
    if (i < words.length) {
        if (j < words[i].length) {
            document.querySelector(".typing-text").textContent = words[i].slice(0, j+1);
            j++;
            setTimeout(type, 80);
        } else {
            j = 0;
            i++;
            setTimeout(type, 900);
        }
    } else {
        i = 0;
        type();
    }
}

type();

// DARK MODE TOGGLE
function toggleDarkMode() {
    document.body.classList.toggle("dark");
}
