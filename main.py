from fastapi import FastAPI
from session import create, get_all
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class Ticket(BaseModel):
    tick_time: str 
    passenger_name: str
    source: str
    destination: str
    price: str

app = FastAPI(
    title="Ticketier API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,  # Allow cookies and credentials
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.get('/')
def home():
    return "Ticketier API"


@app.post("/create")
def add(ticket: Ticket):
    data = create(ticket.tick_time, ticket.passenger_name, ticket.source, ticket.destination, ticket.price)
    return data


@app.get("/all=ticket")
def all_ticket():
    data = get_all()
    return data
