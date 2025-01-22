// https://quera.org/college/6092/chapter/20019/lesson/64945/?comments_page=1&comments_filter=ALL&submissions_page=1
function fetchPrice() {
    return window.fetch('http://localhost:3000/random').then(res => res.json());
  }
  
  function renderPrice(price) {
    const priceElement = document.getElementById('price');
    priceElement.innerHTML = price;
  }
  
  fetchPrice()
    .then(res => res.price)
    .then(renderPrice);
  
  setInterval(() => {
    fetchPrice()
      .then(res => res.price)
      .then(renderPrice);
  }, 1000);
  
  