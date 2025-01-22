// https://quera.org/college/6092/chapter/43168/lesson/144503/?comments_page=1&comments_filter=ALL&submissions_page=1
export function securePhoneNumbers(text) {
    const reg = /\b09\d{9}\b/g;
    
    return text.replace(reg, (match) => {
        return match.slice(0, 4) + '***' + match.slice(7);
    });
}
