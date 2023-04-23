// DOM elements
const container = document.querySelector('.container');
const note = document.querySelector('.note');
const credits = document.querySelector('.credits');
const support = document.querySelector('.support');

// Hide/show elements on click
note.addEventListener('click', () => {
  note.classList.toggle('hidden');
});

credits.addEventListener('click', () => {
  credits.classList.toggle('hidden');
});

support.addEventListener('click', () => {
  support.classList.toggle('hidden');
});

// Hide/show elements on scroll
window.addEventListener('scroll', () => {
  const scrollY = window.scrollY;
  if (scrollY > 100) {
    container.classList.add('scrolled');
  } else {
    container.classList.remove('scrolled');
  }
});
