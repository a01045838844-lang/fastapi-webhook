from fastapi import FastAPI, Request

app = FastAPI()

# 서버 살아있는지 확인용
@app.get("/")
async def root():
    return {"status": "server is live"}

# 웹훅 엔드포인트
@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("📩 웹훅 수신됨:", data)
    return {"status": "ok", "data": data}
