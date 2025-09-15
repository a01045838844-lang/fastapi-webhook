from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root():
    return "HELLO RENDER"

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    return {"received": data}
