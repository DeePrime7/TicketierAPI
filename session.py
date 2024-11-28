from models import engine, Ticket
from sqlmodel import Session, select


def create(tick_time, passenger_name, source, destination, price):
    with Session(engine) as session:

        ticket = Ticket(
            tick_time=tick_time,
            passenger_name=passenger_name,
            source=source,
            destination=destination,
            price=price
        )
       
        session.add(ticket)
        session.commit()
        return "Ticket Created successfully"


def get_all():
    with Session(engine) as session:
        tickets = session.exec(select(Ticket)).all()
        return tickets    