"use strict";

const isLocalStorageSupported = () => {
  try {
    return 'localStorage' in window && window.localStorage !== null;
  } catch (e) {
    return false;
  }
};

const saveTheme = (theme) => {
  if (isLocalStorageSupported()) {
    localStorage.setItem('selectedTheme', theme);
  }
}

const getSavedTheme = () => {
  if (isLocalStorageSupported()) {
    return localStorage.getItem('selectedTheme');
  }
  return null;
}

const configTrigger = document.getElementById('config-trigger');
const configClose = document.getElementById('config-close');
const configPanel = document.getElementById('config-panel');
const colorOptionsContainer = document.getElementById('color-options');
const themeStyleSheet = document.getElementById('theme-style');

const toggleConfigPanel = () => {
  configPanel.classList.toggle('config-panel-open');
  configPanel.classList.toggle('config-panel-hide');
};

configTrigger.addEventListener('click', (e) => {
  e.preventDefault();
  toggleConfigPanel();
});

configClose.addEventListener('click', (e) => {
  e.preventDefault();
  toggleConfigPanel();
});

colorOptionsContainer.addEventListener('click', (e) => {
  const colorOption = e.target.closest('a[data-style]');
  if (!colorOption) return;

  const style = colorOption.getAttribute('data-style');
  saveTheme(style);

  if (themeStyleSheet.getAttribute('href') !== style) {
    themeStyleSheet.setAttribute('href', style);
  }

  Array.from(colorOptionsContainer.children).forEach(el => {
    el.classList.remove('active');
  });

  colorOption.parentElement.classList.add('active');
});

const savedTheme = getSavedTheme();
if (savedTheme) {
  themeStyleSheet.setAttribute('href', savedTheme);
}
