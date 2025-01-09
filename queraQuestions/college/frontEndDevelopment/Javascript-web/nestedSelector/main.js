// https://quera.org/college/6092/chapter/20017/lesson/109619/?comments_page=1&comments_filter=ALL&submissions_page=1
const containerParagraphs = document.querySelectorAll('#container p');

containerParagraphs.forEach(p => {
  p.style.color = 'indigo';
});

const outsideParagraph = document.querySelector('body > p');

outsideParagraph.style.color = 'indianred';
