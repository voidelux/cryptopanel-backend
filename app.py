from fastapi import FastAPI
from src.endpoints.charts.chart import router as chart_router
from src.endpoints.change.change import router as change_router
from src.endpoints.prices.price import router as price_router
from src.endpoints.other.volume import router as volume_router

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.include_router(change_router)
app.include_router(price_router)
app.include_router(volume_router)
app.include_router(chart_router)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn # type: ignore
    uvicorn.run(app, host="localhost", port=5174)
