// https://quera.org/college/6092/chapter/73476/lesson/138792/?comments_page=1&comments_filter=ALL&submissions_page=1
function estimateReadingTime(text) {
    const cleanedText = text.replace(/[.,?!;:]/g, "");

    const words = cleanedText.split(/\s+/).filter(word => word.length > 0);

    return Math.ceil(words.length / 200);
}

export default estimateReadingTime;