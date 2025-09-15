from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "server is live"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("📩 웹훅 수신됨:", data)
    return {"status": "ok", "data": data}
