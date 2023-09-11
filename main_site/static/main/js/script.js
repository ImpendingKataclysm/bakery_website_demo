/* Toggle Navigation Menu visibility */

const nav_bar = document.getElementById('main_nav');
const nav_btn = document.getElementById('nav-btn');

nav_btn.addEventListener('click', () => {
    nav_bar.classList.toggle('show');
});