# 🏨 Hotel Booking Data Engineering Pipeline

An end-to-end Data Engineering project that processes synthetic hotel booking data using a Python ETL pipeline, stores the cleaned data in PostgreSQL, and visualizes business insights through an interactive Streamlit dashboard.

## 📊 Dashboard Preview

[![Hotel Booking Dashboard](images/dashboard.png)](https://hotel-booking-data-engineering-dashboard.streamlit.app/)

## 🎯 Project Overview

This project demonstrates an end-to-end Data Engineering workflow, starting from raw data ingestion and transformation to database storage and interactive data visualization.

The pipeline processes hotel booking records, performs data cleaning and transformation using Python and Pandas, and loads the resulting dataset into PostgreSQL for analytical purposes.

### Project Objectives

- Build a structured ETL pipeline using Python.
- Extract, clean, and transform raw hotel booking data.
- Store processed data in PostgreSQL.
- Build an interactive dashboard for business analysis.
- Practice essential Data Engineering tools and workflows.

## 🏗️ System Architecture

The following diagram illustrates the complete data workflow and the technologies used in this project.

![Hotel Booking Data Engineering Architecture](images/arsitektur.png)

### Architecture Workflow

1. **Source Data:** Raw hotel booking dataset in CSV format.
2. **Ingest & Transform:** Python and Pandas handle data extraction, cleaning, and transformation.
3. **Storage:** PostgreSQL 16 stores the processed booking data, running in a Docker container.
4. **Data Access:** SQLAlchemy and Psycopg provide database connectivity.
5. **Visualization:** Streamlit and Plotly create interactive dashboards.
6. **Output:** Business insights through booking trends, cancellation analysis, revenue, and other key metrics.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data processing and transformation |
| SQLAlchemy | Database connection and SQL toolkit |
| Psycopg | PostgreSQL database driver |
| PostgreSQL 16 | Relational database storage |
| Docker | Database containerization |
| Docker Compose | Container configuration and management |
| Streamlit | Interactive dashboard development |
| Plotly | Data visualization |
| Git & GitHub | Version control and source code hosting |
| Visual Studio Code | Development environment |

## ⚙️ ETL Pipeline

### 1. Extract

Reads the raw hotel booking dataset from a CSV file using Python and Pandas.

### 2. Transform

The transformation process includes:

- Removing duplicate records.
- Handling missing values.
- Creating `total_nights` and `total_guests` columns.
- Calculating `estimated_revenue`.
- Setting estimated revenue to zero for canceled bookings.
- Filtering invalid records.

### 3. Load

Loads the cleaned dataset into the PostgreSQL table named `hotel_bookings` using SQLAlchemy and Psycopg.

### Processing Results

| Description | Records |
|---|---:|
| Raw Dataset | 10,000 |
| Processed Dataset | 9,691 |
| Removed Records | 309 |

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
│   ├── dashboard.png
│   └── architecture.png
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

The dataset is intended for learning and demonstrating Data Engineering workflows. It is not presented as an official hotel booking dataset.

## 👨‍💻 Author

Roni Ramdani

- GitHub: [@ronidee369](https://github.com/ronidee369)
- Project Repository: [Hotel Booking Data Engineering Pipeline](https://github.com/ronidee369/hotel-booking-data-engineering)

---

*Built as a hands-on project to explore Data Engineering, ETL development, database management, and data visualization.*