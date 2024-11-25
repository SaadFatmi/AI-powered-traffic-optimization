from flask import Flask, render_template
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Smart City Traffic Optimization System!"

@app.route('/traffic-data')
def traffic_data():
    traffic_info = {
        "Intersection 1": [40, 74, 75, 84, 70],
        "Intersection 2": [92, 37, 95, 51, 65],
        "Intersection 3": [91, 85, 94, 49, 35],
    }
    return render_template("traffic_data.html", data=traffic_info)

@app.route('/traffic-graph')
def traffic_graph():
    traffic_info = {
        "Intersection 1": [40, 74, 75, 84, 70],
        "Intersection 2": [92, 37, 95, 51, 65],
        "Intersection 3": [91, 85, 94, 49, 35],
    }

    intersections = list(traffic_info.keys())
    averages = [sum(data) / len(data) for data in traffic_info.values()]

    plt.figure(figsize=(8, 5))
    plt.bar(intersections, averages, color='blue')
    plt.title("Average Traffic Flow")
    plt.xlabel("Intersections")
    plt.ylabel("Average Cars Per Hour")
    plt.tight_layout()

    # Save the graph to the static folder
    graph_path = os.path.join("static", "traffic_graph.png")
    plt.savefig(graph_path)
    plt.close()

    return render_template("traffic_graph.html", graph_url=graph_path)

if __name__ == "__main__":
    app.run(debug=True)