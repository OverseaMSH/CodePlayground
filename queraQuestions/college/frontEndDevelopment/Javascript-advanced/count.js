// https://quera.org/college/6092/chapter/43168/lesson/144502/?comments_page=1&comments_filter=ALL&submissions_page=1
function timeit(fn) {
    return function(...args) {
        const start = Date.now();  
        return new Promise((resolve, reject) => {
            Promise.resolve(fn(...args))
                .then((value) => {
                    const time = (Date.now() - start) / 1000; 
                    resolve({ value, time }); 
                })
                .catch(reject); 
        });
    };
}
