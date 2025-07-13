import aiohttp
from fastapi import APIRouter
#from config import config

router = APIRouter()

async def fetch_global_metrics(start_date: str, end_date: str):
    url = "https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/historical"
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '87ff2eab-493f-49f2-b716-895a61496bd1'
    }
    params = {
        'time_start': start_date,
        'time_end': end_date,
        'count': 100,
        'interval': 'daily'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as resp:
            data = await resp.json()
            return data

@router.get("/global-metrics")
async def get_global_metrics():
    from datetime import datetime, timedelta
    end = datetime.utcnow()
    start = end - timedelta(days=7)

    data = await fetch_global_metrics(
        start_date=start.strftime("%Y-%m-%dT%H:%M:%SZ"),
        end_date=end.strftime("%Y-%m-%dT%H:%M:%SZ")
    )
    return data
