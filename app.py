from flask import Flask, render_template, request, jsonify
import serpapi
import time
import os

app = Flask(__name__)
client = serpapi.Client(api_key="YOUR_SERPAPI_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/explore", methods=["POST"])
def explore():
    start_time = time.time()
    data = request.json
    lat, lng = data["lat"], data["lng"]

    # SerpAPI Local Results (e.g., cafes, startups)
    local_results = client.search({
        "engine": "google_maps",
        "q": "startups near me",
        "ll": f"@{lat},{lng},15z",
        "type": "search",
        "google_domain": "google.com",
        "hl": "en"
    })

    # SerpAPI News (e.g., events)
    news_results = client.search({
        "engine": "google_news",
        "q": "tech events",
        "location": "Paris,France",
        "hl": "en",
        "gl": "FR"
    })

    latency = round(time.time() - start_time, 2)

    return jsonify({
        "local": local_results.get("local_results", []),
        "news": news_results.get("news_results", []),
        "latency": latency,
        "coordinates": {"lat": lat, "lng": lng}
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
