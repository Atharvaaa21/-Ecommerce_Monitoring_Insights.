# E-commerce Data Pipeline & Monitoring Project

## 📌 Project Overview
This project simulates an **end-to-end data pipeline** for monitoring e-commerce operations, detecting SLA breaches, and generating business insights using publicly available datasets.
It aligns closely with Data Analyst job requirements involving **Python, Pandas, SQL, AWS QuickSight, Power BI, and Linux**.

---

## 🎯 Goals
- Automate **data ingestion, cleaning, and transformation** using Python (Pandas).
- Store processed data in **MySQL** for querying.
- Build **dashboards** in Power BI and AWS QuickSight.
- Simulate incident detection and root cause analysis (RCA).
- Automate daily health checks in a **Linux environment**.

---

## 🛠 Tech Stack
- **Programming:** Python (Pandas, SQLAlchemy)
- **Database:** MySQL
- **Visualization:** Power BI, AWS QuickSight
- **Automation:** Bash scripting, cron jobs
- **OS:** Linux/Windows
- **Cloud:** AWS (S3 for storage, QuickSight for BI)

---

## 📂 Project Structure
```
ecommerce-data-pipeline/
│
├── README.md
├── data/                  # Sample datasets from Kaggle (Olist dataset)
├── scripts/
│   ├── data_pipeline.py   # ETL process
│   ├── health_check.sh    # Linux-based automation script
├── sql/
│   ├── create_tables.sql
│   ├── monitoring_queries.sql
├── dashboards/
│   ├── powerbi_screenshot.png
│   ├── quicksight_screenshot.png
├── docs/
│   ├── rca_template.md
│   ├── pipeline_diagram.png
└── LICENSE
```

---

## 🚀 How to Run
1. Clone this repo
2. Install Python dependencies:
   ```bash
   pip install pandas sqlalchemy mysql-connector-python
   ```
3. Create MySQL DB using `sql/create_tables.sql`
4. Load data using `scripts/data_pipeline.py`
5. Run monitoring queries from `sql/monitoring_queries.sql`
6. Automate daily check using:
   ```bash
   bash scripts/health_check.sh
   ```

---

## 📊 Dashboards
- **Power BI:** SLA compliance, order trends, regional performance
- **AWS QuickSight:** Revenue trends, customer segmentation

---

## 📄 License
MIT License
