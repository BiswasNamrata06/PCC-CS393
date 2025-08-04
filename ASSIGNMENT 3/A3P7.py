import math

station_full_names = {
    "TH": "THANERAILWAYSTN",
    "GA": "GAONDEVI",
    "IC": "ICEFACTORY",
    "HA": "HARINIWASCIRCLE",
    "TE": "TEENHATHNAKA",
    "LU": "LUISWADI",
    "NI": "NITINCOMPANYJUNCTION",
    "CA": "CADBURRYJUNCTION"
}

BusStops = ["TH", "GA", "IC", "HA", "TE", "LU", "NI", "CA"]
Path = [800, 600, 750, 900, 1400, 1200, 1100, 1500]

def getFare(source, destination):
    n = len(BusStops)

    if source not in station_full_names or destination not in station_full_names:
        return "Invalid source or destination stop code."

    src_index = BusStops.index(source)
    dest_index = BusStops.index(destination)

    distance = 0
    i = src_index
    while i != dest_index:
        distance += Path[i]
        i = (i + 1) % n

    fare = math.ceil(distance / 1000) * 5

    src_name = station_full_names[source]
    dest_name = station_full_names[destination]

    print(f"\nJourney: {src_name} → {dest_name}")
    print(f"Distance Travelled: {distance} meters")
    print(f"Fare: ₹{fare}")
    return fare


source = input("Enter source stop code : ").strip().upper()
destination = input("Enter destination stop code : ").strip().upper()

getFare(source, destination)
