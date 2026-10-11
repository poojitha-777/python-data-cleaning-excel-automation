# Python Data Cleaning and Excel Automation

## Project Overview
This project uses Python and pandas to clean sales data and automate CSV and Excel file creation.

## Features
- Reads sales data from CSV files.
- Identifies missing values.
- Removes duplicate rows.
- Handles missing product, quantity, and sales values.
- Exports cleaned data to CSV and Excel formats.

## Technologies Used
- Python
- Pandas
- OpenPyXL
- CSV and Excel

## Project Structure
```text
python-data-cleaning-excel-automation/
├── data/
│   └── messy_sales.csv
├── output/
│   ├── cleaned_sales.csv
│   └── cleaned_sales.xlsx
├── clean_sales.py
└── README.md
```

## How to Run
1. Install the required packages:
   `py -m pip install pandas openpyxl`
2. Run the script:
   `py clean_sales.py`

## Learning Outcome
Practised data cleaning, duplicate removal, missing-value handling, and Excel automation using Python.
