# 🏨 Hotel Booking Data Engineering Pipeline

An end-to-end Data Engineering project that processes synthetic hotel booking data using a Python ETL pipeline, stores the cleaned data in PostgreSQL, and visualizes business insights through an interactive Streamlit dashboard.

## 📊 Dashboard Preview

[![Hotel Booking Dashboard](images/dashboard.png)](YOUR_STREAMLIT_APP_URL)

*Click the dashboard preview to explore the interactive version.*

> Replace `YOUR_STREAMLIT_APP_URL` with your published Streamlit app URL once deployment is ready.

## 🎯 Project Overview

This project demonstrates a simple end-to-end data engineering workflow, from raw data extraction to interactive data visualization.

The pipeline processes hotel booking records, performs data cleaning and transformation, and loads the resulting dataset into a PostgreSQL database for analytical purposes.

### Project Objectives

- Build a structured ETL pipeline using Python.
- Clean and transform raw hotel booking data.
- Store processed data in PostgreSQL.
- Create an interactive dashboard for business analysis.
- Practice essential Data Engineering tools and workflows.

## 🏗️ Architecture

```text
Raw CSV Dataset
      │
      ▼
   EXTRACT
      │
      ▼
  TRANSFORM
  - Remove duplicates
  - Handle missing values
  - Create calculated columns
      │
      ▼
     LOAD
      │
      ▼
  PostgreSQL
      │
      ▼
 Streamlit Dashboard
      │
      ▼
 Business Insights
```

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data cleaning and transformation |
| SQLAlchemy | Database connection |
| PostgreSQL 16 | Data storage |
| Docker | PostgreSQL containerization |
| Streamlit | Interactive dashboard |
| Plotly | Data visualization |
| Git & GitHub | Version control |

## ⚙️ ETL Pipeline

**1. Extract**

Reads the raw hotel booking dataset from a CSV file.

**2. Transform**

- Removes duplicate records.
- Handles missing values.
- Creates `total_nights` and `total_guests`.
- Calculates `estimated_revenue`.
- Sets estimated revenue to zero for canceled bookings.
- Filters invalid records.

**3. Load**

Loads the cleaned dataset into the PostgreSQL table named `hotel_bookings`.

**Processing Result**

- Raw records: 10,000
- Processed records: 9,691

## 📈 Dashboard Features

The dashboard provides interactive visualizations to explore hotel booking performance.

### Key Performance Indicators (KPIs)

- Total Bookings
- Cancellation Rate
- Estimated Revenue
- Average ADR

### Visualizations

- Monthly Booking Trends
- Bookings by Hotel Type
- Cancellation Distribution
- Top 10 Customer Countries
- Customer Type Distribution
- Distribution Channel Analysis

### Interactive Filters

- Arrival Year
- Hotel Type
- Booking Status

## 📁 Project Structure

```text
Hotel-Booking-Data-Engineering/
│
├── data/
│   ├── raw/
│   │   └── hotel_bookings.csv
│   └── processed/
│       └── hotel_bookings_clean.csv
│
├── database/
│   └── init.sql
│
├── pipeline/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── dashboard/
│   └── app.py
│
├── images/
│   └── dashboard.png
│
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ronidee369/hotel-booking-data-engineering.git

cd hotel-booking-data-engineering
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file based on `.env.example` and configure your PostgreSQL connection.

Example:

```env
POSTGRES_DB=hotel_booking
POSTGRES_USER=hotel_user
POSTGRES_PASSWORD=your_password

DATABASE_URL=postgresql+psycopg://hotel_user:your_password@localhost:5432/hotel_booking
```

### 5. Start PostgreSQL with Docker

```bash
docker compose up -d
```

### 6. Run the ETL Pipeline

Run the scripts in sequence:

```bash
python pipeline/extract.py
python pipeline/transform.py
python pipeline/load.py
```

### 7. Launch the Dashboard

```bash
streamlit run dashboard/app.py
```

The dashboard will open in your browser.

## 📂 Dataset Information

This project uses a synthetic hotel booking dataset containing 10,000 initial records and 32 columns.

The dataset is intended for learning and demonstrating data engineering workflows. It is not presented as an official hotel booking dataset.

## 👨‍💻 Author

**Roni Ramdani**

- GitHub: [@ronidee369](https://github.com/ronidee369)
- Project Repository: [Hotel Booking Data Engineering Pipeline](https://github.com/ronidee369/hotel-booking-data-engineering)

---

*Built as a hands-on project to explore Data Engineering, ETL development, database management, and data visualization.*