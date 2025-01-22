// https://quera.org/college/6092/chapter/73476/lesson/138801/?comments_page=1&comments_filter=ALL&submissions_page=1
const n = +readline()

for (let i = 1; i <= n; i++) {
    const row = [];
    for (let j = 1; j <= n; j++) {
        row.push(i * j);
    }
    console.log(row.join(" "));
}
