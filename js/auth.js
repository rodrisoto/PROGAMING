document.addEventListener("DOMContentLoaded", () => {
    const loginBtn = document.getElementById("btn-login");
    const registroBtn = document.getElementById("btn-registro");
    const logoutBtn = document.getElementById("btn-logout");
  
    // Verificamos si hay sesión activa
    const usuario = localStorage.getItem("usuario");
  
    if (usuario) {
      // Ocultar login y registro
      if (loginBtn) loginBtn.style.display = "none";
      if (registroBtn) registroBtn.style.display = "none";
      if (logoutBtn) logoutBtn.style.display = "inline";
    }
  
    if (logoutBtn) {
      logoutBtn.addEventListener("click", (e) => {
        e.preventDefault();
        localStorage.removeItem("usuario");
        window.location.href = "index.html";
      });
    }
  });
  