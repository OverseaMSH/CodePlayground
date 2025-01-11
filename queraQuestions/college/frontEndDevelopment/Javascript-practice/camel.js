// https://quera.org/college/6092/chapter/73476/lesson/138805/?comments_page=1&comments_filter=ALL&submissions_page=1
function camelCase(text) {
    text = text.trim();
    
    const words = text.split(/\s+/);
    
    const camelCased = words
        .map((word, index) => {
            if (index === 0) {
                return word.toLowerCase();
            }
            return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
        })
        .join('');
    
    return camelCased;
}

export default camelCase;
