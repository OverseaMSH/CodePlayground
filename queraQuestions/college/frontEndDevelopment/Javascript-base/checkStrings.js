// https://quera.org/college/6092/chapter/20016/lesson/248155/?comments_page=1&comments_filter=ALL&submissions_page=1
function countCharacters(str) {
    return str.replaceAll(" ", "").length;
}

function reverseString(str) {
    return str.split("").reverse().join("");
}

function replaceWord(str, target, replacement) {
    return str.replaceAll(target, replacement);
}

function isPalindrome(str) {
    const cleanedStr = str.replaceAll(" ", "").toLowerCase();
    const reversedStr = cleanedStr.split("").reverse().join("");
    return cleanedStr === reversedStr;
}

module.exports = {
    countCharacters,
    reverseString,
    replaceWord,
    isPalindrome,
};