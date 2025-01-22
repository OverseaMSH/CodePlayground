// https://quera.org/college/6092/chapter/73476/lesson/138795/?comments_page=1&comments_filter=ALL&submissions_page=1
let str = readline();

function check1(str) {
    let counter = 0;
    for (let c of str) {
        if (c === "R") {
            counter++;
        }
    }
    return counter >= 3; 
}

function check2(str) {
    let rCounter = 0, yCounter = 0;
    for (let c of str) {
        if (c === "R") {
            rCounter++;
        } else if (c === "Y") {
            yCounter++;
        }
    }
    return rCounter >= 2 && yCounter >= 2;
}

function check3(str) {
    let counter = 0;
    for (let c of str) {
        if (c === "G") {
            counter++;
        }
    }
    return counter === 0;
}

if (check1(str) || check2(str) || check3(str)) {
    console.log("nakhor lite");
} else {
    console.log("rahat baash");
}