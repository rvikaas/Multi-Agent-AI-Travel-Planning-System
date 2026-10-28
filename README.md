# ✈️ Multi-Agent AI Travel Booking System

A multi-agent travel planning application that combines LangGraph, Groq, PostgreSQL, Tavily Search, AviationStack, and Streamlit to generate personalized travel plans.

The system coordinates four specialized agents that work together to collect travel information and produce a complete itinerary:

1. **Flight Agent** — Retrieves flight information through the AviationStack API.
2. **Hotel Agent** — Creates a hotel search query and searches for accommodation information with Tavily.
3. **Itinerary Agent** — Uses the available flight and hotel results to generate a travel itinerary.
4. **Final Agent** — Combines all results into a concise final travel plan.

## ✨ Features

- Multi-agent orchestration with **LangGraph**
- LLM-powered planning with **Groq** and `openai/gpt-oss-120b`
- Flight data retrieval through **AviationStack**
- Hotel and destination research through **Tavily Search**
- Persistent conversation checkpoints with **PostgreSQL**
- Interactive Streamlit frontend
- Live agent progress updates in the web interface
- Automatic saving of generated travel plans to `travel_plans/`
- Downloadable Markdown travel plans
- Separate command-line and Streamlit entry points

## 🏗️ Architecture

```text
User request
     │
     ▼
┌───────────────┐
│  Flight Agent │─── AviationStack
└───────┬───────┘
        ▼
┌───────────────┐
│  Hotel Agent  │─── Tavily Search + Groq
└───────┬───────┘
        ▼
┌────────────────┐
│ Itinerary Agent│─── Groq
└────────┬───────┘
         ▼
┌───────────────┐
│  Final Agent  │─── Groq
└───────────────┘
         │
         ▼
   Final travel plan
```

The workflow is defined in `main.py` as a sequential LangGraph pipeline:

```text
START → flight_agent → hotel_agent → itinerary_agent → final_agent → END
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/rvikaas/Multi-Agent-AI-Travel-Booking-System.git
cd Multi-Agent-AI-Travel-Booking-System
```

### 2. Create and activate a virtual environment

#### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows PowerShell

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔐 Environment Variables

Create a file named `.env` in the project root:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
AVIATIONSTACK_API_KEY=your_aviationstack_api_key
DATABASE_URL=postgresql://username:password@localhost:5432/travel_planner
```

Keep `.env` private. It is included in `.gitignore` and should never be committed to the repository.

> `main.py` initializes a PostgreSQL checkpointer with `PostgresSaver` and calls `memory.setup()` when the application starts. Make sure the database is running and the connection string is valid before launching the application.

## ▶️ Usage

### Streamlit web application

The recommended way to use the project is through the Streamlit interface:

```bash
streamlit run frontend.py
```

Then open the local URL displayed by Streamlit, usually:

```text
http://localhost:8501
```

Enter a request such as:

```text
Plan a 7-day trip to Japan with flights, hotels, sightseeing, and a moderate budget.
```

The interface displays the progress of each agent, shows the final travel plan, allows the result to be downloaded, and saves a Markdown copy under `travel_plans/`.

### Command-line interface

You can also run the LangGraph workflow directly:

```bash
python main.py
```

Enter a travel request when prompted:

```text
Enter travel request: Plan a weekend trip to Paris with flights and hotels
```

## 🧠 How It Works

1. The user submits a travel request.
2. The **Flight Agent** calls the AviationStack integration and collects flight results.
3. The **Hotel Agent** asks the LLM to create a focused hotel-search query, then sends it to Tavily.
4. The **Itinerary Agent** uses the user request, flight results, and hotel results to create an itinerary.
5. The **Final Agent** combines the collected information into the final response.
6. LangGraph stores workflow checkpoints in PostgreSQL using the configured thread ID.
