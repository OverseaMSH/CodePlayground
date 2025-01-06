// https://quera.org/college/6092/chapter/20016/lesson/248152/?comments_page=1&comments_filter=ALL&submissions_page=1
const temperatures = [
    22, 25, 21, 19, 24, 26, 23, 22, 21, 20, 25, 27, 28, 22, 23, 24, 19, 18, 22,
    23, 26, 27, 28, 25, 24, 22, 21, 20, 19, 18,
    ];
    let av=0
    for(let i=0;i<temperatures.length;i++){
    av+=temperatures[i]
    }
    averageTemperature=av/temperatures.length
    let max=temperatures[0];
    for(let i=0;i<temperatures.length;i++){
    if (temperatures[i]>max){
    max=temperatures[i]
    }
    }
    maxTemperature=max
    
    console.log("میانگین دما:", averageTemperature);
    let min=temperatures[0];
    for(let i=0;i<temperatures.length;i++){
    if (temperatures[i]<min){
    min=temperatures[i]
    }
    }
    minTemperature=min
    
    console.log("داغ‌ترین دما:", maxTemperature);
    console.log("سردترین دما:", minTemperature);
    let count=0
    for(let i=0;i<temperatures.length;i++){
    if (temperatures[i]>averageTemperature){
    count++;
    }
    }
    daysAboveAverage=count
    console.log("تعداد روزهای گرم‌تر از میانگین:", daysAboveAverage);
    
    module.exports = {
    temperatures,
    averageTemperature,
    maxTemperature,
    minTemperature,
    daysAboveAverage,
    };