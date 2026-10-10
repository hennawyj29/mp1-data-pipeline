This project is a data pipeline that loads, checks, cleans, and saves data. The pipeline first loads the data and the configuration file. It then validates the data to make the required columns are there and the numeric values are valid. Next, it processes the data by removing duplicates, missing values, and outliers. The different files in the src foler handle loading, validation, processing, saving, and other helpful functions. The pipeline.py file connects all of these steps and runs the full pipeline. At the end, the cleaned data is saved to a CSV file and a cleaning report is printed.

Example Command:
python pipeline.py --input fixtures/sample_data.csv --output output/clean.csv --config config/config.yaml --verbose

Example Output:
The sample data starts with 100 rows. Validation leaves 98 rows, and after cleaning, 92 rows remain. The cleaned data is saved to output/clean.csv