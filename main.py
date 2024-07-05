import asyncio

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import time, requests
from functools import reduce

async def main():
    coins = [
        "SHIB", "BTC", "DOGE"
    ]
    users = [
        1893217856,
    ]
    current_time = time.localtime()
    current_date_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
    async with Bot(
        token="6545393934:AAFOhBNw6w6MqSjcDBr9KgHfZdu6qGlJ6W0",
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
        ),
    ) as bot:

        [await bot.send_message(
            chat_id=user_id,
            text=f"{current_date_time}\n\n" + reduce(
                lambda a, b: a + b,
                [get_prices(coin) for coin in coins]
            )
        ) for user_id in users]

def get_prices(coin: str) -> dict:
    time_stamp=str(int(time.time() * 10 ** 3))
    url="https://api.bybit.com/v5/market/tickers"
    params=f'category=spot&symbol={coin}USDT'
    headers = {
        'X-BAPI-SIGN-TYPE': '2',
        'X-BAPI-TIMESTAMP': time_stamp,
        'X-BAPI-RECV-WINDOW': "5000",
    }
    response = requests.get(
        url,
        headers=headers,
        params=params
    ).json()

    current_time = time.localtime()

    current_date_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)

    return f"💰 {coin}\n" + \
        f"🟩: {response["result"]["list"][0]["ask1Price"]} | " +  \
        f"🟥: {response["result"]["list"][0]["bid1Price"]}\n\n"


if __name__ == "__main__":
    asyncio.run(main())
