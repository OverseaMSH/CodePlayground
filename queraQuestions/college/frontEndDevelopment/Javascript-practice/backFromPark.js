// https://quera.org/college/6092/chapter/73476/lesson/138796/?comments_page=1&comments_filter=ALL&submissions_page=1
const [x, y] = readline().split(" ").map(n => +n);
const [x1, y1] = readline().split(" ").map(n => +n);

if (x1 > x) {
    console.log("Right");
} else {
    console.log("Left");
}