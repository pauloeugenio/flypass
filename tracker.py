from fast_flights import FlightQuery, Passengers, create_query, get_flights
from datetime import datetime
import csv
import os

ORIGIN = "PAR"
DESTINATION = "ROM"
DATE = "2026-08-15"
DATA_FILE = "data/prices.csv"

os.makedirs("data", exist_ok=True)

query = create_query(
    flights=[
        FlightQuery(
            date=DATE,
            from_airport=ORIGIN,
            to_airport=DESTINATION
        )
    ],
    trip="one-way",
    seat="economy",
    passengers=Passengers(adults=1),
    language="en-US"
)

result = get_flights(query)

exists = os.path.exists(DATA_FILE)

with open(DATA_FILE, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    if not exists:
        writer.writerow([
            "timestamp",
            "origin",
            "destination",
            "date",
            "current_price",
            "price",
            "airline",
            "duration"
        ])

    if not result.flights:
        writer.writerow([
            datetime.now().isoformat(),
            ORIGIN,
            DESTINATION,
            DATE,
            result.current_price,
            "NO_RESULT",
            "",
            ""
        ])
    else:
        for flight in result.flights:
            writer.writerow([
                datetime.now().isoformat(),
                ORIGIN,
                DESTINATION,
                DATE,
                result.current_price,
                flight.price,
                flight.name,
                flight.duration
            ])
