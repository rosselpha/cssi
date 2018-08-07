const redButton = document.querySelector('.red');
const greenButton = document.querySelector('.green');
const blueButton = document.querySelector('.blue');

const buttons = document.querySelectorAll('button');

buttons.forEach(button => {
  button.addEventListener('click', () => {
    const color = button.innerHTML;
    box.style.background = color;
  });
});
