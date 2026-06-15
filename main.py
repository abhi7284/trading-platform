from fastapi import FastAPI

from api.controllers.auth_controller import router as auth_router

app = FastAPI(title="Trading Platform", version="1.0.0")

app.include_router(auth_router)


@app.get("/health")
def health():
    return {"status": "UP"}
