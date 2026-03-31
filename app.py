from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def get_data():
    data = []
    with open("data.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                data.append((int(row["co2"]), row["time"]))
            except:
                continue
    return data

@app.route("/")
def index():
    mode = request.args.get("mode", "data")
    date = request.args.get("date")

    all_data = get_data()
    data = []

    if date:
        data = [d for d in all_data if d[1].startswith(date)]

    if data:
        co2 = data[-1][0]
        if co2 < 800:
            status = "Labs"
            color = "green"
        elif co2 < 1200:
            status = "Vidējs"
            color = "orange"
        else:
            status = "Slikts"
            color = "red"
    else:
        co2 = None
        status = None
        color = None

    time_range = f"{all_data[0][1]} — {all_data[-1][1]}" if all_data else "Nav datu"

    return render_template(
        "index.html",
        co2=co2,
        status=status,
        color=color,
        data=data,
        all_data=all_data,
        mode=mode,
        date=date,
        time_range=time_range
    )

if __name__ == "__main__":
    app.run(debug=True)