"use strict";

const modeToggler = document.getElementById('darkmode');
const documentBody = document.body; 

function applyTheme(isDarkMode) {
  if (isDarkMode) {
    documentBody.classList.add('dark-mode');
    modeToggler.checked = true;
    console.log('Dark mode applied');
  } else {
    documentBody.classList.remove('dark-mode');
    modeToggler.checked = false;
    console.log('Light mode applied');
  }
}

function setThemeFromLocalStorage() {
  const isDarkMode = localStorage.getItem('mode') === 'dark';
  applyTheme(isDarkMode);
}

setThemeFromLocalStorage();

modeToggler.addEventListener('change', () => {
  const isDarkMode = modeToggler.checked;
  applyTheme(isDarkMode);
  
  if (isDarkMode) {
    localStorage.setItem('mode', 'dark');
  } else {
    localStorage.removeItem('mode');
  }
});
