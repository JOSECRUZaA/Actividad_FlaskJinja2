// Validación de formulario de Bootstrap
(function () {
    'use strict'
  
    // Obtener todos los formularios a los que queremos aplicar estilos de validación de Bootstrap
    var forms = document.querySelectorAll('.needs-validation')
  
    // Bucle sobre ellos y evitar el envío
    Array.prototype.slice.call(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }
  
          form.classList.add('was-validated')
        }, false)
      })
  })()
  
  // Script para animaciones simples al hacer scroll
  document.addEventListener("DOMContentLoaded", function() {
      // Ocultar mensajes flash después de 5 segundos
      setTimeout(function() {
          let alerts = document.querySelectorAll('.alert');
          alerts.forEach(function(alert) {
              let bsAlert = new bootstrap.Alert(alert);
              bsAlert.close();
          });
      }, 5000);
  });
