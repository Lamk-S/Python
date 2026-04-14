// ==========================================
// FUNCIONES GLOBALES
// ==========================================

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

// ==========================================
// INICIALIZACIÓN (Cuando el DOM está listo)
// ==========================================
document.addEventListener("DOMContentLoaded", function() {
    
    // --- 1. Lógica de Toasts (Mensajes Flash) ---
    // Auto-ocultar todos los toasts después de 4 segundos
    const toasts = document.querySelectorAll('.toast-message');
    
    toasts.forEach(toast => {
        setTimeout(() => {
            // Verificar que el usuario no lo haya cerrado manualmente
            if (document.body.contains(toast)) { 
                cerrarToast(toast);
            }
        }, 4000); 
    });


    // --- 2. Lógica del Menú Desplegable (Dropdown del Perfil) ---
    const button = document.getElementById('user-menu-button');
    const menu = document.getElementById('user-dropdown-menu');

    if (button && menu) {
        // Alternar menú al hacer clic en el botón del perfil
        button.addEventListener('click', function(event) {
            event.stopPropagation(); // Evita que el clic se propague y cierre el menú inmediatamente
            menu.classList.toggle('hidden');
        });

        // Cerrar menú si se hace clic en cualquier otra parte de la pantalla
        document.addEventListener('click', function(event) {
            if (!menu.contains(event.target) && !button.contains(event.target)) {
                menu.classList.add('hidden');
            }
        });
    }
    
});