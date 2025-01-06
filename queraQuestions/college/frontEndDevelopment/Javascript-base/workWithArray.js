// https://quera.org/college/6092/chapter/20016/lesson/248154/?comments_page=1&comments_filter=ALL&submissions_page=1
function sortArray(arr) {
    arr.sort()
    return arr
}

function findLargestNumber(arr) {
    return Math.max(...arr)
}

function removeDuplicates(arr) {
       return [...new Set(arr)];
}

function rotateArray(arr, times) {
    times = times % arr.length;
    if (times < 0) {
        times += arr.length; 
    }

    for (let i = 0; i < times; i++) {
        const lastElement = arr.pop(); 
        arr.unshift(lastElement);
    }
    
    return arr;
}



module.exports = {
  sortArray,
  findLargestNumber,
  removeDuplicates,
  rotateArray,
};
