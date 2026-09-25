/* ─── NAVBAR SCROLL ─────────────────────────────────── */
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    navbar?.classList.toggle('scrolled', window.scrollY > 50);
});

/* ─── HAMBURGER MENU ────────────────────────────────── */
const hamburger = document.getElementById('hamburger');
const navLinks  = document.getElementById('navLinks');
hamburger?.addEventListener('click', () => {
    navLinks?.classList.toggle('open');
    hamburger.classList.toggle('open');
});

/* ─── CLOSE MENU ON LINK CLICK ──────────────────────── */
document.querySelectorAll('.nav-link, .btn-nav').forEach(link => {
    link.addEventListener('click', () => {
        navLinks?.classList.remove('open');
        hamburger?.classList.remove('open');
    });
});

/* ─── REVEAL ON SCROLL ──────────────────────────────── */
const revealEls = document.querySelectorAll(
    '.card, .event-card, .event-detail-card, .stat-card, .form-card, .table-wrapper'
);

revealEls.forEach(el => el.classList.add('reveal'));

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
            setTimeout(() => entry.target.classList.add('visible'), i * 80);
            observer.unobserve(entry.target);
        }
    });
}, { threshold: 0.1 });

revealEls.forEach(el => observer.observe(el));

/* ─── AUTO-DISMISS FLASH MESSAGES ───────────────────── */
setTimeout(() => {
    document.querySelectorAll('.flash').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateX(60px)';
        el.style.transition = 'all 0.4s ease';
        setTimeout(() => el.remove(), 400);
    });
}, 4000);

/* ─── CONFIRM DELETE ────────────────────────────────── */
function confirmDelete() {
    return confirm('¿Seguro que deseas eliminar esta reserva? Esta acción no se puede deshacer.');
}

/* ─── COUNTER ANIMATION ─────────────────────────────── */
function animateCounter(el) {
    const target = parseInt(el.textContent, 10);
    if (isNaN(target)) return;
    let current = 0;
    const step = Math.ceil(target / 30);
    const timer = setInterval(() => {
        current = Math.min(current + step, target);
        el.textContent = current;
        if (current >= target) clearInterval(timer);
    }, 40);
}

const statNumbers = document.querySelectorAll('.stat-number');
const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animateCounter(entry.target);
            counterObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

statNumbers.forEach(el => {
    if (!isNaN(parseInt(el.textContent))) counterObserver.observe(el);
});
