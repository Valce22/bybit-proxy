from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/price/{symbol}")
async def get_price(symbol: str):
    url = f"https://api.bybit.com/v5/market/tickers?category=spot&symbol={symbol}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()
