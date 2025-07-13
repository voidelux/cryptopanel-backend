import aiohttp
from fastapi import APIRouter
from config import config

router = APIRouter()

symbols = ['BTC', 'XMR', 'TON']

async def fetch_all_prices():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': config.get_token()
    }

    async with aiohttp.ClientSession() as session:
        params = {
            'symbol': ','.join(symbols),
            'convert': 'USD'
        }
        async with session.get(url, headers=headers, params=params) as resp:
            data = await resp.json()
            return {
                symbol: round(data['data'][symbol]['quote']['USD']['price'], 2)
                for symbol in symbols
            }

@router.get("/bitcoin")
async def get_bitcoin():
    prices = await fetch_all_prices()
    return {"price": f"{prices['BTC']:,.2f}"}

@router.get("/monero")
async def get_monero():
    prices = await fetch_all_prices()
    return {"price": f"{prices['XMR']:,.2f}"}

@router.get("/toncoin")
async def get_ton():
    prices = await fetch_all_prices()
    return {"price": f"{prices['TON']:,.2f}"}
