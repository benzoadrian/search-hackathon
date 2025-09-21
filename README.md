# Inttrest: Real-Time Geospatial Intelligence

**Turn any map coordinate into actionable insights—live, fast, and relevant.**

---

## **🚀 Overview**
Coordinate Explorer is a **real-time geospatial intelligence tool** that fetches and visualizes location-based data (startups, events, points of interest) for any coordinate on Earth. Built for speed and relevance, it demonstrates:
- **Sub-second data ingestion** from SerpAPI
- **Live visualization** with Leaflet.js
- **Extensible architecture** for vector search and agent orchestration

**Built in <1 hour for the MistralAI Hackathon.**

---

## **🛠 Tech Stack**
| Component       | Technology          | Purpose                                  |
|-----------------|---------------------|------------------------------------------|
| Backend         | Flask (Python)      | Lightweight API for SerpAPI integration  |
| Frontend        | Leaflet.js          | Interactive map and results display      |
| Data Provider   | [SerpAPI](https://serpapi.com/) | Live local results and news              |
| Metrics         | Python `time`       | Latency tracking                         |
| Deployment      | Localhost           | Ready for Docker/cloud deployment        |

---

## **🔧 Setup**
### **Prerequisites**
- Python 3.8+
- SerpAPI key ([get one here](https://serpapi.com/))

### **Installation**
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/coordinate-explorer.git
   cd coordinate-explorer
