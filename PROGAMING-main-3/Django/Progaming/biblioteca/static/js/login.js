document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('btnLogin').addEventListener('click', validarLogin);
});

function validarLogin() {
  const usuario = document.getElementById('usuario');
  const password = document.getElementById('password');
  let isValid = true;

  // Obtener datos almacenados en localStorage
  const storedUsuario = localStorage.getItem('usuario');
  const storedPassword = localStorage.getItem('password');

  // Validar campos vacíos
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

  // Verificar credenciales
  if (isValid) {
    if (usuario.value.trim() === storedUsuario && password.value.trim() === storedPassword) {
      alert('Inicio de sesión exitoso. Redirigiendo...');
      localStorage.setItem('logueado', 'true'); // Marcar como logueado
      window.location.href = 'index.html'; // Redirigir a la página principal
    } else {
      alert('Usuario o contraseña incorrectos.');
      marcarInvalido(usuario);
      marcarInvalido(password);
    }
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