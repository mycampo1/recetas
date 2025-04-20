// document.addEventListener('DOMContentLoaded', () => {
//     const modal = document.getElementById('modalCrearReceta');
//     const openModalButton = document.getElementById('openModalButton');
//     const closeModalButton = document.querySelector('.modal-close');

//     if (openModalButton) {
//         openModalButton.addEventListener('click', () => {
//             modal.style.display = 'flex';
//         });
//     }

//     if (closeModalButton) {
//         closeModalButton.addEventListener('click', () => {
//             modal.style.display = 'none';
//         });
//     }

//     // Cerrar el modal al hacer clic fuera del contenido
//     window.addEventListener('click', (event) => {
//         if (event.target === modal) {
//             modal.style.display = 'none';
//         }
//     });
// });

document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('modalCrearReceta');
    const openModalButton = document.getElementById('openModalButton');
    const closeModalButton = document.querySelector('.modal-close');
    const cancelModalButton = document.getElementById('cancelModalButton');

    if (openModalButton) {
        openModalButton.addEventListener('click', () => {
            modal.style.display = 'flex';
        });
    }

    if (closeModalButton) {
        closeModalButton.addEventListener('click', () => {
            modal.style.display = 'none';
        });
    }

    if (cancelModalButton) {
        cancelModalButton.addEventListener('click', () => {
            modal.style.display = 'none';
        });
    }

    // Cierra el modal al hacer clic fuera del contenido
    window.addEventListener('click', (event) => {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
});
