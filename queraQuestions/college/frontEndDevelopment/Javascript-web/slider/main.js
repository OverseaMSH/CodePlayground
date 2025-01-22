// https://quera.org/college/6092/chapter/20017/lesson/109620/?comments_page=1&comments_filter=ALL&submissions_page=1
const sliderImages = [
  "./images/image1.jpg",
  "./images/image2.jpg",
  "./images/image3.jpg",
  "./images/image4.jpg",
];
const sliderDom = document.getElementById("slider");

let currentImage = 0;

function renderImages() {
  sliderImages.forEach((image) => {
    const imgElement = document.createElement("img");
    imgElement.src = image;
    imgElement.style.opacity = 0;
    sliderDom.appendChild(imgElement);
  });
}

function clearImages() {
  const images = sliderDom.getElementsByTagName("img");
  for (let i = 0; i < images.length; i++) {
    images[i].style.opacity = 0;
  }
}

function showImage(imageIndex) {
  clearImages();
  const images = sliderDom.getElementsByTagName("img");
  if (images[imageIndex]) {
    images[imageIndex].style.opacity = 1;
  }
}

document.querySelector("#prevButton").addEventListener("click", () => {
  currentImage = (currentImage - 1 + sliderImages.length) % sliderImages.length;
  showImage(currentImage);
});

document.querySelector("#nextButton").addEventListener("click", () => {
  currentImage = (currentImage + 1) % sliderImages.length;
  showImage(currentImage);
});

function init() {
  renderImages();
  showImage(currentImage);
}

init();
