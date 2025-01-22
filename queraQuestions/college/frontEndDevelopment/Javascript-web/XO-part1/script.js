// https://quera.org/college/6092/chapter/20017/lesson/64911/?comments_page=1&comments_filter=ALL&submissions_page=1
let turn = 1;
document.querySelector('.game--status').innerHTML= "it's X's turn";
document.querySelectorAll('.cell').forEach(e => {
    e.addEventListener('click', () => {
        turn++;
        e.innerHTML = turn % 2 == 0 ? 'X' : 'O';
        document.querySelector('.game--status').innerHTML = `it's ${turn % 2 == 0 ? 'O' : 'X'}'s turn `;
    });
});
document.querySelector('.game--restart').addEventListener('click', () => {
    document.querySelectorAll('.cell').forEach(e => e.innerHTML = '');
    turn = 1;
});