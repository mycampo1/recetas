document.addEventListener('DOMContentLoaded', function() {
    // Referencias a elementos del modal
    const modal = document.getElementById('modalCrearReceta');
    const openButton = document.getElementById('openModalButton');
    const closeButton = document.querySelector('.modal-close');
    const cancelButton = document.getElementById('cancelModalButton');
    
    // Si no encontramos los elementos necesarios, no hacemos nada
    if (!modal || !openButton) return;
    
    // Función para abrir modal
    function openModal() {
        modal.style.display = 'flex';
        setTimeout(() => {
            modal.style.opacity = '1';
            modal.querySelector('.modal-content').style.transform = 'translateY(0)';
        }, 10);
    }
    
    // Función para cerrar modal
    function closeModal() {
        modal.style.opacity = '0';
        modal.querySelector('.modal-content').style.transform = 'translateY(-20px)';
        setTimeout(() => {
            modal.style.display = 'none';
        }, 300);
    }
    
    // Event listeners
    openButton.addEventListener('click', openModal);
    
    if (closeButton) {
        closeButton.addEventListener('click', closeModal);
    }
    
    if (cancelButton) {
        cancelButton.addEventListener('click', closeModal);
    }
    
    // Cerrar modal al hacer clic fuera
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            closeModal();
        }
    });
});