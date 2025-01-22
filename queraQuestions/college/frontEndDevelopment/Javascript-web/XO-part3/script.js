// https://quera.org/college/6092/chapter/20017/lesson/64913/?comments_page=1&comments_filter=ALL
let turn = 1;
const statusDisplay = document.querySelector('.game--status');
const gameState = Array(9).fill("");
const winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
];
let gameActive = true;

statusDisplay.innerHTML = "It's X's turn";

function checkWin() {
    for (let condition of winningConditions) {
        const [a, b, c] = condition;
        if (gameState[a] && gameState[a] === gameState[b] && gameState[a] === gameState[c]) {
            statusDisplay.innerHTML = `Player ${gameState[a]} has won`;
            gameActive = false;
            return;
        }
    }
    if (!gameState.includes("")) {
        statusDisplay.innerHTML = "Game ended in a draw";
        gameActive = false;
    }
}

document.querySelectorAll('.cell').forEach(cell => {
    cell.addEventListener('click', () => {
        if (!gameActive) return;
        const cellIndex = cell.getAttribute("data-cell-index");
        if (gameState[cellIndex] !== "") return;

        gameState[cellIndex] = turn % 2 === 0 ? "O" : "X";
        cell.innerHTML = gameState[cellIndex];

        checkWin();

        if (gameActive) {
            turn++;
            const currentPlayer = turn % 2 === 0 ? "O" : "X";
            statusDisplay.innerHTML = `It's ${currentPlayer}'s turn`;
        }
    });
});

document.querySelector(".game--restart").addEventListener("click", () => {
    document.querySelectorAll('.cell').forEach(cell => cell.innerHTML = "");
    gameState.fill("");
    turn = 1;
    gameActive = true;
    statusDisplay.innerHTML = "It's X's turn";
});