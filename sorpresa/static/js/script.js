const boton = document.querySelector("#boton-sorpresa");
const sorpresa = document.querySelector("#sorpresa");

boton.addEventListener("click", () => {
  sorpresa.hidden = !sorpresa.hidden;
  boton.setAttribute("aria-expanded", String(!sorpresa.hidden));
  boton.textContent = sorpresa.hidden ? "Abrir mi sorpresa" : "Volver";
});
