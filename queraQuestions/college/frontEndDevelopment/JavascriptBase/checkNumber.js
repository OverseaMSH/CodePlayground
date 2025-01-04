// https://quera.org/college/6092/chapter/20016/lesson/248151/?comments_page=1&comments_filter=ALL&submissions_page=1
function getNumberInput() {
    const input = prompt("لطفا عدد وارد کنید");
    const number = parseInt(input);
    if (isNaN(number)) {
        return null;
    }
    return number;
}

function checkPositivity(number) {
    if (number > 0) {
        return "عدد مثبت است.";
    } else if (number < 0) {
        return "عدد منفی است.";
    } else {
        return "عدد صفر است.";
    }
}

function checkParity(number) {
    if (number % 2 === 0) {
        return "عدد زوج است.";
    } else {
        return "عدد فرد است.";
    }
}

function checkMultipleOfTen(number) {
    if (number % 10 === 0) {
        return "عدد مضرب ۱۰ است.";
    } else {
        return "عدد مضرب ۱۰ نیست.";
    }
}



module.exports = {
    getNumberInput,
    checkPositivity,
    checkParity,
    checkMultipleOfTen,
};