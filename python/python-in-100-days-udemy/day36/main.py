import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "IU1ONJ3XX0EUWTLU"
NEWS_API_KEY = "d862ce13080e467ca0b3a2cb61f81342"   

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response=requests.get(url=STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
dataList = [value for (key, value) in data.items()]
yesterdayData = dataList[0]
yesterdayClosingPrice = yesterdayData["4. close"]
dayBeforeYesterdayData = dataList[1]
dayBeforeYesterdayClosingPrice = dayBeforeYesterdayData["4. close"]

difference = abs(float(yesterdayClosingPrice) - float(dayBeforeYesterdayClosingPrice))
diffPercent = (difference / float(yesterdayClosingPrice)) * 100
if diffPercent >  1:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }
    newsResponse=requests.get(NEWS_ENDPOINT, params=news_params)
    newsData = newsResponse.json()["articles"]
    firstThreeArticles = newsData[:3]
    formattedArticles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in firstThreeArticles]


    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    # since i dont have a twilio account i will just copy this part of the code which is not working.
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to="+989197650107"
        )

