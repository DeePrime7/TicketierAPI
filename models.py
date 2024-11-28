from sqlmodel import SQLModel, create_engine, Field

# Corrected database URL
url = "sqlite:///tt.db"
engine = create_engine(url, echo=True)

def create_db_and_table():
    SQLModel.metadata.create_all(engine)

class Ticket(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tick_time: str
    passenger_name: str
    source: str
    destination: str
    price: str

create_db_and_table()
