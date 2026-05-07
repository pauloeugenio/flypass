from fast_flights import FlightQuery, Passengers, create_query, get_flights
from datetime import datetime
import csv
import os

ORIGIN = "ORY"
DESTINATION = "NAT"
DATE = "2026-09-18"
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
    seat="economy",
    trip="one-way",
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
            "price",
            "airline",
            "duration"
        ])

    if not result:
        writer.writerow([
            datetime.now().isoformat(),
            ORIGIN,
            DESTINATION,
            DATE,
            "NO_RESULT",
            "",
            ""
        ])
    else:
        for flight in result:
            writer.writerow([
                datetime.now().isoformat(),
                ORIGIN,
                DESTINATION,
                DATE,
                getattr(flight, "price", ""),
                getattr(flight, "name", ""),
                getattr(flight, "duration", "")
            ])
