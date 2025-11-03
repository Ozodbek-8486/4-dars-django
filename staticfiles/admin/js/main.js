document.addEventListener("DOMContentLoaded", () => {
  const el = document.querySelector(".brand-text") || document.querySelector(".welcome-sign") || null;
  if (!el) return;

  const text = el.innerText.trim();
  el.innerHTML = "";

  const glitch = document.createElement("div");
  glitch.className = "edex-glitch";
  glitch.setAttribute("data-text", text);
  el.appendChild(glitch);

  let i = 0;
  function typeTick() {
    if (i <= text.length) {
      glitch.setAttribute("data-text", text.slice(0, i));
      glitch.innerText = text.slice(0, i);
      i++;
      setTimeout(typeTick, 40 + Math.random() * 60);
    } else {
      glitch.classList.add("glitch-active");
    }
  }
  typeTick();
});
