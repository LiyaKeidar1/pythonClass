from fastapi import FastAPI
from pydantic import BaseModel

import random

import uvicorn

app = FastAPI()
# uvicorn Visa:app --host 0.0.0.0 --port 8001

class payment(BaseModel):
    costumer: str
    card_number: int
    price: int

transactions=[]
failed_transactions=[]
i, j = 0, 0

@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post("/run_transaction/")
async def buy_vehicle_with_visa(pay: payment):
    global i
    global j
    if random.random()<0.8:
        i+=1
        transactions.append({i:pay})
        return {"approved": "Vehicle bought successfully"}
    else:
        failed_transactions.append({j:pay})
        return {"failed": "Vehicle's payment failed"}

@app.get("/transactions/{passed}")
async def get_vehicle(passed: bool):
    if passed:
        return transactions
    else:
        return failed_transactions


if __name__=="main":
    uvicorn.run(app, host="0.0.0.0", port="8001")