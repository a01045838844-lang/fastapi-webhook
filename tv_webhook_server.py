# tv_webhook_server.py

from fastapi import FastAPI, Request
import json
import gate_api
from gate_api.exceptions import GateApiException
from pprint import pprint

# Gate.io API 설정
api_key = "8746befa2ed54be32c7bf906e9aaaeb2"
secret_key = "f76db8ace26e29a3e120d0829480fc50a7fe8dc3010788070b4796ab108243b5"

# 기본 설정
default_currency_pair = "BTC_USDT"
fixed_amount = "0.02"  # 💰 고정 수량 (BTC)

# Gate API 초기화
configuration = gate_api.Configuration(
    host="https://api.gate.io",
    key=api_key,
    secret=secret_key
)
api_client = gate_api.ApiClient(configuration)
spot_api = gate_api.SpotApi(api_client)

# FastAPI 서버
app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("📩 웹훅 수신됨:")
    pprint(data)

    message = data.get("message", "").lower()

    try:
        if "buy" in message:
            print("🟢 매수 시그널 감지됨! 0.02 BTC 주문 실행 중...")
            order = spot_api.create_order(gate_api.Order(
                currency_pair=default_currency_pair,
                side="buy",
                amount=fixed_amount,
                price="",  # 시장가 주문
                type="market"
            ))
            print("✅ 매수 주문 완료:")
            pprint(order)

        elif "sell" in message:
            print("🔴 매도 시그널 감지됨! 0.02 BTC 주문 실행 중...")
            order = spot_api.create_order(gate_api.Order(
                currency_pair=default_currency_pair,
                side="sell",
                amount=fixed_amount,
                price="",  # 시장가 주문
                type="market"
            ))
            print("✅ 매도 주문 완료:")
            pprint(order)

        else:
            print("❌ 알 수 없는 메시지:", message)

    except GateApiException as e:
        print("🚨 주문 실패:")
        print(e)

    return {"status": "✅ received"}
