/* Toggle Navigation Menu visibility */

const nav_bar = document.getElementById('main_nav');
const nav_btn = document.getElementById('nav-btn');

nav_btn.addEventListener('click', () => {
    nav_bar.classList.toggle('show');
});

/* Toggle Side Nav Visibility */

const side_nav = document.getElementById('side_nav');
const side_nav_btn = document.getElementById('side_nav_btn');
const side_nav_items = document.getElementsByClassName('sidenav-item');

if(side_nav && side_nav_btn && side_nav_items) {
    side_nav_btn.addEventListener('click', () => {
        side_nav.classList.toggle('show');
    });

    for (let i = 0; i < side_nav_items.length; i++) {
        side_nav_items[i].addEventListener('click', () => {
            side_nav.classList.toggle('show');
        });
    }
}