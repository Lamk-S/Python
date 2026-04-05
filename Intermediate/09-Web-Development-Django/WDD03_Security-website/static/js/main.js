// Función para ocultar un toast con animación
function cerrarToast(elemento) {
    // 1. Desplazar hacia la derecha y volverlo transparente
    elemento.classList.remove('translate-x-0', 'opacity-100');
    elemento.classList.add('translate-x-full', 'opacity-0');
    
    // 2. Esperar a que termine la animación de CSS (500ms) para borrarlo del HTML
    setTimeout(() => {
        elemento.remove();
    }, 500);
}

// Inicializar scripts cuando el DOM esté listo
document.addEventListener("DOMContentLoaded", function() {
    
    // Auto-ocultar todos los toasts (mensajes) después de 4 segundos
    const toasts = document.querySelectorAll('.toast-message');
    
    toasts.forEach(toast => {
        setTimeout(() => {
            // Verificar que no lo hayan cerrado manual
            if (document.body.contains(toast)) { 
                cerrarToast(toast);
            }
        }, 4000); 
    });
});