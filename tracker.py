from fast_flights import FlightData, Passengers, create_filter, get_flights
from datetime import datetime
import csv
import os

ORIGIN = "ORY"
DESTINATION = "NAT"
DATE = "2026-08-15"
DATA_FILE = "data/prices.csv"

os.makedirs("data", exist_ok=True)

filter = create_filter(
    flight_data=[
        FlightData(
            date=DATE,
            from_airport=ORIGIN,
            to_airport=DESTINATION
        )
    ],
    trip="one-way",
    passengers=Passengers(adults=1),
    seat="economy"
)

result = get_flights(filter=filter)

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

    for flight in result.flights:
        writer.writerow([
            datetime.now().isoformat(),
            ORIGIN,
            DESTINATION,
            DATE,
            flight.price,
            flight.name,
            flight.duration
        ])
