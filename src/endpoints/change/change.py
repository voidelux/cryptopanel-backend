import aiohttp
from fastapi import APIRouter
from config import config

router = APIRouter()

symbols = ['BTC', 'XMR', 'TON']

async def fetch_all_changes():
    url = "https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/historical"
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
                symbol: round(data['data'][symbol]['quote']['USD']['percent_change_24h'], 2)
                for symbol in symbols
            }

@router.get("/bitcoin/change")
async def get_btc_change():
    changes = await fetch_all_changes()
    return {"change": changes['BTC']}

@router.get("/monero/change")
async def get_xmr_change():
    changes = await fetch_all_changes()
    return {"change": changes['XMR']}

@router.get("/toncoin/change")
async def get_ton_change():
    changes = await fetch_all_changes()
    return {"change": changes['TON']}
