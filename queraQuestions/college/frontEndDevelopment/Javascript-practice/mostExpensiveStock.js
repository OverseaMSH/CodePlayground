// https://quera.org/college/6092/chapter/73476/lesson/138806/?comments_page=1&comments_filter=ALL&submissions_page=1
const stocks = [
    {
        name: "Electric Khodro",
        price: 12912,
    },
    {
        name: "Iran Khodro",
        price: 15218,
    },
    {
        name: "Iran arghaam",
        price: 8853,
    },
    // ...
];

export function getHighestPrice(stocks) {
    if (stocks.length === 0) {
        return null;
    }

    let highestPriceStock = stocks[0]; 

    for (let i = 1; i < stocks.length; i++) {
        if (stocks[i].price > highestPriceStock.price) {
            highestPriceStock = stocks[i]; 
        }
    }

    return highestPriceStock.name;
}

console.log(getHighestPrice(stocks)); 
