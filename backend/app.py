from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

with open("bra_aircraft.json") as f:
    BRA_AIRCRAFT = json.load(f)["aircraft"]

@app.route("/api/flights")
def flights():

    url = "https://opensky-network.org/api/states/all"
    r = requests.get(url)
    data = r.json()

    results = []

    if data["states"]:

        for state in data["states"]:
            callsign = state[1]

            if callsign:
                for aircraft in BRA_AIRCRAFT:
                    if aircraft in callsign:

                        results.append({
                            "aircraft": aircraft,
                            "callsign": callsign.strip(),
                            "lat": state[6],
                            "lon": state[5],
                            "altitude": state[7],
                            "velocity": state[9]
                        })

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
