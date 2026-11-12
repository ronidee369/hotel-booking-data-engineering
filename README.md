Hotel Booking Data Engineering Pipeline

An end-to-end data engineering project that transforms raw hotel booking data into an analytics-ready PostgreSQL database and an interactive business intelligence dashboard.







Project Overview

The Hotel Booking Data Engineering Pipeline is an end-to-end data engineering project designed to demonstrate a practical data processing workflow.

The project processes raw hotel booking data through an ETL (Extract, Transform, Load) pipeline, stores the cleaned data in PostgreSQL, and presents business insights through an interactive dashboard built with Streamlit and Plotly.

The main objective is to transform raw booking records into structured, reliable, and analytics-ready data that can support hotel business analysis.

Project Objectives

Build an end-to-end ETL pipeline using Python.

Perform data cleaning and transformation with Pandas.

Store structured data in PostgreSQL.

Manage the database using Docker.

Develop an interactive dashboard using Streamlit and Plotly.

Analyze hotel booking trends, cancellations, customer behavior, and estimated revenue.

Project Architecture

Raw CSV Dataset
      |
      v
   EXTRACT
 Python / Pandas
      |
      v
  TRANSFORM
 Data Cleaning
 Data Validation
 Feature Engineering
      |
      v
    LOAD
  SQLAlchemy
      |
      v
 PostgreSQL 16
    Docker
      |
      v
Streamlit Dashboard
     Plotly
      |
      v
 Business Insights

Tech Stack

Technology

Purpose

Python

Main programming language

Pandas

Data extraction and transformation

SQLAlchemy

Database connection and data loading

PostgreSQL 16

Relational database

Docker Compose

Database container management

Streamlit

Interactive dashboard

Plotly

Data visualization

python-dotenv

Environment variable management

Git & GitHub

Version control and project hosting

VS Code

Development environment

Project Structure

Hotel-Booking-Data-Engineering/
│
├── data/
│   ├── raw/
│   │   └── hotel_bookings.csv
│   │
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
│   └── dashboard-preview.png
│
├── .env.example
├── .gitignore
├── docker-compose.yml
├── requirements.txt
└── README.md

ETL Pipeline

1. Extract

Reads the raw hotel booking dataset from a CSV file using Pandas.

Input: data/raw/hotel_bookings.csv

Script: pipeline/extract.py

2. Transform

Cleans and prepares the raw dataset for analysis.

Key transformations include:

Removing duplicate records.

Handling missing values.

Creating total_nights.

Creating total_guests.

Calculating estimated_revenue.

Setting estimated revenue to zero for canceled bookings.

Filtering records with invalid guest or stay counts.

Output: data/processed/hotel_bookings_clean.csv

Script: pipeline/transform.py

3. Load

Loads the processed dataset into PostgreSQL using Pandas and SQLAlchemy.

Destination table: hotel_bookings

Script: pipeline/load.py

The successful local pipeline execution loaded 9,691 cleaned records into PostgreSQL.

Dashboard Preview

The interactive dashboard provides an overview of hotel booking performance, including booking trends, cancellation rates, estimated revenue, and customer behavior.



Key Performance Indicators

Total Bookings

Cancellation Rate

Estimated Revenue

Average ADR (Average Daily Rate)

Visualizations

Monthly Booking Trends

Bookings by Hotel Type

Cancellation Distribution

Top 10 Customer Countries

Customer Type Distribution

Distribution Channel Analysis

Interactive Filters

Arrival Year

Hotel Type

Booking Status

The dashboard is built with Streamlit and Plotly to provide interactive data exploration and visualization.

Getting Started

Follow these instructions to run the project locally.

Prerequisites

Make sure you have installed:

Python 3.12 or compatible version

Docker Desktop

Git

Visual Studio Code

1. Clone the Repository

git clone https://github.com/ronidee369/hotel-booking-data-engineering.git

cd hotel-booking-data-engineering

2. Create a Virtual Environment

python -m venv .venv

Activate the environment on Windows PowerShell:

.\.venv\Scripts\Activate.ps1

3. Install Dependencies

pip install -r requirements.txt

4. Configure Environment Variables

Create a local .env file:

Copy-Item .env.example .env

Update .env with your local PostgreSQL configuration:

POSTGRES_DB=hotel_booking
POSTGRES_USER=hotel_user
POSTGRES_PASSWORD=your_local_password

DATABASE_URL=postgresql+psycopg://hotel_user:your_local_password@localhost:5432/hotel_booking

Important: Never commit your .env file or expose database credentials publicly.

5. Start PostgreSQL with Docker

Make sure Docker Desktop is running:

docker compose up -d

Check the running container:

docker ps

6. Run the ETL Pipeline

Execute the scripts in the following order.

Extract:

python pipeline/extract.py

Transform:

python pipeline/transform.py

Load:

python pipeline/load.py

7. Run the Dashboard

Start the Streamlit application:

streamlit run dashboard/app.py

Open the local URL displayed in the terminal, usually:

http://localhost:8501

Dataset Information

This project uses a synthetic hotel booking dataset containing approximately 10,000 raw records and 32 columns.

The dataset includes:

Hotel type

Booking status

Arrival date

Length of stay

Number of guests

Customer type

Country

Distribution channel

Average Daily Rate (ADR)

After data cleaning and transformation, the pipeline produced 9,691 records in the local execution.

Note: This dataset is synthetic and is used for educational and portfolio demonstration purposes. It should not be interpreted as official hotel business data.

Author

Roni Ramdani

GitHub: @ronidee369

Project Repository: Hotel Booking Data Engineering Pipeline