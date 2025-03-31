document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('btnLogin').addEventListener('click', validarLogin);
  });
  
  function validarLogin() {
    const usuario = document.getElementById('usuario');
    const password = document.getElementById('password');
    let isValid = true;
  
    if (!usuario.value.trim()) {
      marcarInvalido(usuario);
      isValid = false;
    } else {
      marcarValido(usuario);
    }
  
    if (!password.value.trim()) {
      marcarInvalido(password);
      isValid = false;
    } else {
      marcarValido(password);
    }
  
    if (isValid) {
      alert('Inicio de sesión exitoso. Redirigiendo...');
      window.location.href = 'index.html'; // Redirige a la página principal
    }
  }
  
  function togglePassword(id) {
    const field = document.getElementById(id);
    field.type = field.type === 'password' ? 'text' : 'password';
  }
  
  function marcarInvalido(elemento) {
    elemento.classList.add('is-invalid');
    elemento.classList.remove('is-valid');
  }
  
  function marcarValido(elemento) {
    elemento.classList.remove('is-invalid');
    elemento.classList.add('is-valid');
  }
  