// https://quera.org/college/6092/chapter/20017/lesson/64914/?comments_page=1&comments_filter=ALL&submissions_page=1
const data = [
  'Teal',
  'SkyBlue',
  'DarkSeaGreen',
  'Purple',
  'LightPink',
  'Crimson'
];
const defaultColor = 'Silver';

const select = document.getElementById('color-select');
const box = document.getElementById('box');

data.forEach(color => {
  const option = document.createElement('option');
  option.value = color; 
  option.textContent = color; 
  select.appendChild(option);
});

select.addEventListener('change', (event) => {
  const color = event.target.value; 

  if (color === '') {
    box.style.backgroundColor = defaultColor;
  } else {
    box.style.backgroundColor = color; 

    setTimeout(() => {
      box.style.backgroundColor = defaultColor;
    }, 1000);
  }
});