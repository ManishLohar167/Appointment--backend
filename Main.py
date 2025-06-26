from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class Appointment(BaseModel):
    name: str
    email: str
    date: str
    time: str

@app.post("/book")
def book_appointment(data: Appointment):
    return {"message": f"Appointment booked for {data.name} on {data.date} at {data.time}"}
