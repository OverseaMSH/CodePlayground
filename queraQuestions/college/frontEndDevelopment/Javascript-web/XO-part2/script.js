// https://quera.org/college/6092/chapter/20017/lesson/64912/?comments_page=1&comments_filter=ALL&submissions_page=1let turn = 1;
let turn = 1;
const statusDisplay = document.querySelector('.game--status');
const gameState = Array(9).fill("");
document.querySelector('.game--status').innerHTML = "It's X's turn";


document.querySelectorAll('.cell').forEach(cell => {
    cell.addEventListener('click', () => {
        const cellIndex = cell.getAttribute("data-cell-index");
        if (gameState[cellIndex] !== "") return;

        gameState[cellIndex] = turn % 2 === 0 ? "O" : "X";
        cell.innerHTML = gameState[cellIndex];

        turn++;
        const currentPlayer = turn % 2 === 0 ? "O" : "X";
        statusDisplay.innerHTML = `It's ${currentPlayer}'s turn`;
    });
});

document.querySelector(".game--restart").addEventListener("click", () => {
  document.querySelectorAll('.cell').forEach((cell) => (cell.innerHTML = ""));
  gameState.fill("");
  turn = 1;
  statusDisplay.innerHTML = "It's X's turn";
});
