# 🏏 IPL Momentum Intelligence Agent

### Real-Time Match Analytics & Fantasy Decision Engine (Agentic AI)

---

## 📌 Overview

The **IPL Momentum Intelligence Agent** is an **Agentic AI-powered system** that provides real-time cricket match insights, win probability predictions, and fantasy cricket recommendations.

Instead of showing raw statistics, the system behaves like a **professional cricket analyst**, delivering:

* Key insights
* Supporting data
* Actionable recommendations

---

## 🚀 Key Features

### 🔴 Live Match Analysis

* Tracks score, wickets, overs, run rate
* Identifies match phase (Powerplay / Middle / Death)
* Provides context-aware insights

---

### 📈 Player Momentum Engine *(Core Innovation)*

* Custom **momentum score (0–100)**
* Labels players as:

  * 🔥 Hot
  * 🌤️ Warm
  * ❄️ Cold
* Based on performance trends and match impact

---

### 📊 Win Probability Prediction

* Uses:

  * Run rate vs required run rate
  * Wickets in hand
  * Match pressure
* Outputs:

  * Batting team win %
  * Bowling team win %
  * Clear prediction summary

---

### 🧠 Fantasy XI Recommendation

* Suggests:

  * Captain & Vice-Captain
  * Differential picks (low ownership players)
  * Players to avoid
  * Complete playing XI

---

### 🏟️ Historical Venue Insights

* Pitch behavior analysis
* Average scores
* Chase success rates
* Venue-based strategic insights

---

## 🧩 Tech Stack

* **Python**
* **Google ADK (Agent Development Kit)**
* **Gemini API (gemini-flash-latest)**
* **FastAPI (via ADK Web Server)**

---

## ⚙️ Project Structure

```
ipl_agent/
│
├── ipl_agent/
│   ├── __init__.py
│   └── agent.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔧 Setup & Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/Padmavathi-42/ipl_project.git
cd ipl_project
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Add API Key

Create a `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
GOOGLE_GENAI_USE_VERTEXAI=0
```

---

### 5️⃣ Run the Project

```
adk web --port 8001
```

Open in browser:
👉 [http://127.0.0.1:8001](http://127.0.0.1:8001)

---

## 🧠 How It Works (Agentic Flow)

1. Agent receives user query
2. Calls `get_live_match_state`
3. Chains tools intelligently:

   * Momentum → Prediction → Fantasy
4. Generates expert-style response

---

## 💡 Example Use Cases

* “Who is likely to win this match?”
* “Best captain for fantasy team?”
* “Current match situation analysis”

---

## 🌟 Innovation Highlights

* ✅ Agentic AI with tool chaining
* ✅ Custom **Momentum Scoring Algorithm**
* ✅ Multi-layer decision system
* ✅ Analyst-style intelligent responses

---

## 📊 Novelty

⭐ **4/5**

* Strong system design + agentic behavior
* Unique momentum-based approach
* Limited by mock data (can be improved with real APIs)

---

## 🔮 Future Improvements

* 🔗 Real-time cricket API integration
* 🤖 Machine learning-based predictions
* 📊 Visual dashboards
* 🌍 Multi-match live tracking

---

## 👩‍💻 Author

**Padmavathi**
GitHub: [https://github.com/Padmavathi-42](https://github.com/Padmavathi-42)

---

## 📜 License

This project is for educational and demonstration purposes.

---
