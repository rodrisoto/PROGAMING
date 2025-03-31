
    // Asignar evento al botón de registro
    document.getElementById('btnRegistrar').addEventListener('click', function() {
      validarYEnviar();
    });
    
    // Función para validar y enviar el formulario
    function validarYEnviar() {
      let form = document.getElementById('registroForm');
      let isValid = true;
      
      // Validar nombre completo
      const nombreCompleto = document.getElementById('nombreCompleto');
      if (!nombreCompleto.value.trim()) {
        nombreCompleto.classList.add('is-invalid');
        isValid = false;
      } else {
        nombreCompleto.classList.remove('is-invalid');
        nombreCompleto.classList.add('is-valid');
      }
      
      // Validar usuario
      const usuario = document.getElementById('usuario');
      if (!usuario.value.trim() || usuario.value.length < 4) {
        usuario.classList.add('is-invalid');
        isValid = false;
      } else {
        usuario.classList.remove('is-invalid');
        usuario.classList.add('is-valid');
      }
      
      // Validar correo
      const correo = document.getElementById('correo');
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!correo.value.trim() || !emailRegex.test(correo.value)) {
        correo.classList.add('is-invalid');
        isValid = false;
      } else {
        correo.classList.remove('is-invalid');
        correo.classList.add('is-valid');
      }
      
      // Validar contraseña
      const password = document.getElementById('password');
      if (!password.value || password.value.length < 8) {
        password.classList.add('is-invalid');
        isValid = false;
      } else {
        password.classList.remove('is-invalid');
        password.classList.add('is-valid');
      }
      
      // Validar confirmación de contraseña
      const confirmPassword = document.getElementById('confirmPassword');
      if (!confirmPassword.value || confirmPassword.value !== password.value) {
        confirmPassword.classList.add('is-invalid');
        isValid = false;
      } else {
        confirmPassword.classList.remove('is-invalid');
        confirmPassword.classList.add('is-valid');
      }
      
      // Validar fecha de nacimiento
      const fechaNacimiento = document.getElementById('fechaNacimiento');
      if (!fechaNacimiento.value) {
        fechaNacimiento.classList.add('is-invalid');
        isValid = false;
      } else {
        fechaNacimiento.classList.remove('is-invalid');
        fechaNacimiento.classList.add('is-valid');
      }
      
      // Validar términos
      const terminos = document.getElementById('terminos');
      if (!terminos.checked) {
        terminos.classList.add('is-invalid');
        isValid = false;
      } else {
        terminos.classList.remove('is-invalid');
        terminos.classList.add('is-valid');
      }
      
      // Si todo es válido, mostrar mensaje de éxito y redirigir
      if (isValid) {
        alert('¡Registro exitoso! Bienvenido a PROGAMING. Serás redirigido a la página de inicio.');
        // Redirección directa y forzada a index.html
        window.location.replace('index.html');
      }
    }
    
    // Función para limpiar el formulario
    function limpiarFormulario() {
      const form = document.getElementById('registroForm');
      form.reset();
      
      // Eliminar clases de validación
      const formControls = form.querySelectorAll('.form-control');
      formControls.forEach(control => {
        control.classList.remove('is-invalid');
        control.classList.remove('is-valid');
      });
      
      document.getElementById('terminos').classList.remove('is-invalid');
    }
    
    // Función para mostrar/ocultar contraseña
    function togglePassword(id) {
      const passwordField = document.getElementById(id);
      if (passwordField.type === 'password') {
        passwordField.type = 'text';
      } else {
        passwordField.type = 'password';
      }
    }
