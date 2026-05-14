🚆 German Public Transport ETL Pipeline (BVG API → PostgreSQL)
📌 Overview

This project is a lightweight data engineering ETL pipeline that extracts real-time public transport data from the BVG (Berlin transport) API, 
transforms it into a structured format, and loads it into a PostgreSQL database running inside Docker.

The pipeline processes multiple station inputs and stores both station metadata and real-time departure information.

⚙️ Tech Stack
Python 3,
PostgreSQL,
Docker & Docker Compose,
Pandas,
SQLAlchemy,
BVG Transport API,

🏗️ Architecture
stops.txt
    ↓
extract.py (BVG API)
    ↓
transform.py (clean + structure JSON)
    ↓
load.py (PostgreSQL)
    ↓
PostgreSQL (Docker container)


📊 Data Model
stations table
column	                    description
station_id (PK)	            unique station identifier
station_name	n             ame of station
ingested_at               	timestamp of ingestion
departures table
column	                   description
trip_id(PK)	               trip identifier
station_id	               related station
delay	                     delay in seconds
direction	                 route direction
ingested_at	               timestamp of ingestion


🚀 How to Run
1. Start PostgreSQL (Docker)
docker compose up -d
2. Install dependencies
pip install -r requirements.txt
3. Run pipeline
python src/main.py
4. Input stops

Example:

mehringdamm
alexanderplatz
berlin hbf

📌 Features
API-based data ingestion
Modular ETL pipeline (extract / transform / load)
Batch processing of multiple stations
PostgreSQL persistence using Docker
Primary key enforcement (no duplicate stations)
Real-time departure data extraction


📈 Future Improvements
Add UPSERT logic for incremental updates
Add Airflow for scheduling
Add logging system
Add data validation layer
Store historical snapshots
