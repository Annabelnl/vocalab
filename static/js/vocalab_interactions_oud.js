// JavaScript voor verbeterde gebruikerservaring

document.addEventListener('DOMContentLoaded', function() {
    // Header - Verklein het logo bij scrollen
    const headerContainer = document.querySelector('.header-container');
    const logo = document.querySelector('.banner img');

    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            headerContainer.style.padding = '10px 20px';
            logo.style.maxWidth = '100px';
        } else {
            headerContainer.style.padding = '20px 40px';
            logo.style.maxWidth = '150px';
        }
    });

            logo.style.opacity = '1';
        logo.style.transform = 'translateY(0) scale(1)';
    }, 100);

    // Smooth scrolling voor ankerlinks
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Animatie voor call-to-action knoppen bij hover
    const ctaButtons = document.querySelectorAll('.cta-button');
    ctaButtons.forEach(button => {
        button.addEventListener('mouseover', function() {
            button.style.transform = 'scale(1.1)';
        });
        button.addEventListener('mouseout', function() {
            button.style.transform = 'scale(1)';
        });
    });

    // Back to top knop
    const backToTopButton = document.createElement('button');
    backToTopButton.innerText = '⬆️';
    backToTopButton.classList.add('back-to-top');
    document.body.appendChild(backToTopButton);

    window.addEventListener('scroll', function() {
        if (window.scrollY > 300) {
            backToTopButton.style.display = 'block';
        } else {
            backToTopButton.style.display = 'none';
        }
    });

    backToTopButton.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});

// Styling voor de back-to-top knop
const style = document.createElement('style');
style.textContent = `
    .back-to-top {
        position: fixed;
        bottom: 30px;
        right: 30px;
        padding: 10px;
        background-color: #e63946;
        color: #ffffff;
        border: none;
        border-radius: 50%;
        cursor: pointer;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        display: none;
        transition: transform 0.3s;
    }
    .back-to-top:hover {
        transform: scale(1.1);
    }
`;
document.head.appendChild(style);
