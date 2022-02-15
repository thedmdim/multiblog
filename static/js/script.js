if (sessionStorage.getItem('dark-mode') === "true"){
  document.querySelector("#dark-mode").checked = true;
  darkMode()
}

function darkMode() {
  document.querySelector("#dark-mode").checked ? sessionStorage.setItem('dark-mode', true) : sessionStorage.setItem('dark-mode', false);
  document.body.classList.toggle("dark");
  document.querySelector('html').classList.toggle("night");
}
