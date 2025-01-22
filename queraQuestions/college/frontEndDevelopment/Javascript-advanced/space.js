// https://quera.org/college/6092/chapter/43168/lesson/144504/?comments_page=1&comments_filter=ALL&submissions_page=1
function getAreaFunctions(shapes) {
    const areaCalculators = {
        square: (side) => side * side,
        circle: (radius) => Math.PI * radius * radius,
        rectangle: (length, width) => length * width,
        triangle: (base, height) => 0.5 * base * height
    };

    return shapes.map(shape => areaCalculators[shape]);
}

export default getAreaFunctions;
