document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("registroForm");
  const btnRegistrar = document.getElementById("btnRegistrar");

  btnRegistrar.addEventListener("click", (event) => {
    event.preventDefault(); // Evita el envío del formulario por defecto

    // Validar cada campo
    let isValid = true;

    const nombreCompleto = document.getElementById("nombreCompleto");
    const usuario = document.getElementById("usuario");
    const correo = document.getElementById("correo");
    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirmPassword");
    const fechaNacimiento = document.getElementById("fechaNacimiento");
    const terminos = document.getElementById("terminos");

    // Validaciones
    if (nombreCompleto.value.trim() === "") {
      nombreCompleto.classList.add("is-invalid");
      isValid = false;
    } else {
      nombreCompleto.classList.remove("is-invalid");
    }

    if (usuario.value.trim().length < 4) {
      usuario.classList.add("is-invalid");
      isValid = false;
    } else {
      usuario.classList.remove("is-invalid");
    }

    const correoRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!correoRegex.test(correo.value.trim())) {
      correo.classList.add("is-invalid");
      isValid = false;
    } else {
      correo.classList.remove("is-invalid");
    }

    if (password.value.trim().length < 8) {
      password.classList.add("is-invalid");
      isValid = false;
    } else {
      password.classList.remove("is-invalid");
    }

    if (confirmPassword.value.trim() !== password.value.trim()) {
      confirmPassword.classList.add("is-invalid");
      isValid = false;
    } else {
      confirmPassword.classList.remove("is-invalid");
    }

    if (fechaNacimiento.value.trim() === "") {
      fechaNacimiento.classList.add("is-invalid");
      isValid = false;
    } else {
      fechaNacimiento.classList.remove("is-invalid");
    }

    if (!terminos.checked) {
      terminos.classList.add("is-invalid");
      isValid = false;
    } else {
      terminos.classList.remove("is-invalid");
    }

    // Si todo es válido, guardar los datos en localStorage y redirigir
    if (isValid) {
      alert("Registro exitoso. Serás redirigido al inicio de sesión.");
      localStorage.setItem("usuario", usuario.value.trim()); // Guardar el nombre de usuario
      localStorage.setItem("password", password.value.trim()); // Guardar la contraseña
      localStorage.setItem("logueado", "true"); // Marcar como logueado
      window.location.href = "login.html"; // Redirigir a login.html
    }
  });
});