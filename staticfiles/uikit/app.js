// Invoke Functions Call on Document Loaded

let alertWrapper = document.querySelector('.alert')
let alertClose = document.querySelector('.alert__close')
console.log(alertWrapper);
console.log(alertClose);
if (alertWrapper) {
  alertClose.addEventListener('click', () =>
    alertWrapper.style.display = 'none'
  )
}