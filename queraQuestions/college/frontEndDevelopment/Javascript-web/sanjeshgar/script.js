// https://quera.org/college/6092/chapter/20017/lesson/64915/?comments_page=1&comments_filter=ALL&submissions_page=1
const localStorageKey = 'greeting';
const localStorageValue = 'سلام دنیا!';
setInterval(()=>{
    const greeting=localStorage.getItem(localStorageKey)
    if (greeting) {
        document.querySelector("#result").textContent = greeting;
    } else {
        document.querySelector("#result").textContent = '';
    }
}, 1000);
document.querySelector("#btn").addEventListener('click', () => {
    localStorage.setItem(localStorageKey, localStorageValue);
    });
    document.querySelector("#remove").addEventListener('click', () => {
    localStorage.removeItem(localStorageKey)
    });

