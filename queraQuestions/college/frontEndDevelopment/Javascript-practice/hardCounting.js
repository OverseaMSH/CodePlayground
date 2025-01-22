// https://quera.org/college/6092/chapter/73476/lesson/138791/?comments_page=1&comments_filter=ALL&submissions_page=1
export function solver(n) {
    let str = n.toString(2); 
    let counter = 0; 
    for (let i = 0; i < str.length; i++) { 
        if (str[i] == "1") {
            counter++;
        }
    }
    return counter; 
}