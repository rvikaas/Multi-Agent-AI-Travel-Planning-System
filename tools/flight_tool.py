import os
from dotenv import load_dotenv
import requests

load_dotenv()

key = os.getenv("AVIATIONSTACK_API_KEY")

def search_flights(query):

    url = "http://api.aviationstack.com/v1/flights"

    params = {
        "access_key" : key,
        "limit" : 5
    }

    response = requests.get(url, params=params)

    data = response.json()

    flights = []

    if "data" in data:
        
        for flight in data["data"][:5]:
            airline = flight.get("airline", {}).get("name", "unknown")

            arrival_data = flight.get("arrival") or {}
            arrival = arrival_data.get("airport", "unknown")

            departure_data = flight.get("departure") or {}
            departure = arrival_data.get("airport", "unknown")
            
            status = flight.get("flight_status", "unknown")

            flights.append(
                f"""
                Airline: {airline}
                Departure: {departure}
                Arrival: {arrival}
                Status: {status}
                """
            )

    return "\n".join(flights)        