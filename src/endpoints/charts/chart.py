import aiohttp
from fastapi import APIRouter

router = APIRouter()

symbols_map = {
    "BTC": "bitcoin",
    "XMR": "monero",
    "TON": "solana"
}

async def fetch_ohlc(symbol_id: str):
    url = f"https://api.coingecko.com/api/v3/coins/{symbol_id}/ohlc"
    params = {
        "vs_currency": "usd",
        "days": "1"
    }
    headers = {"accept": "application/json"}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as resp:
            data = await resp.json()
            return data

@router.get("/bitcoin/chart")
async def get_btc_chart():
    data = await fetch_ohlc(symbols_map["BTC"])
    return {"chart": data}

@router.get("/monero/chart")
async def get_xmr_chart():
    data = await fetch_ohlc(symbols_map["XMR"])
    return {"chart": data}

@router.get("/toncoin/chart")
async def get_ton_chart():
    data = await fetch_ohlc(symbols_map["TON"])
    return {"chart": data}
