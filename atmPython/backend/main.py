from fastapi import FastAPI
from pydantic import BaseModal

app = FastAPI()

# A model of the comming data from the frontend
class InsertCardRequest(BaseModal):
    card_number: str

# ATM state 

atm_state = {
    "current_card": None,
    "is_authenticated": False
}

@app.post("/insert-card")
def insert_card(request: InsertCardRequest):
    atm_state["current_card"] = request.card_number
    atm_state["is_authenticated"] = False

    return {
        "message": "Card inserted successfully. Please authenticate.",
        "state": "CARD_INSERTED"
    }