# Assignment 17 - PySpark DataFrame Application

## Objective

This project demonstrates PySpark DataFrame operations on a sales dataset.

## Dataset

The dataset contains product sales information with the following fields:

* product_id
* product_name
* category
* sales

## Tasks Performed

1. Read the CSV file into a PySpark DataFrame.
2. Display all products sorted by sales in descending order.
3. Display the top 3 products with the highest sales.
4. Filter products with sales greater than 80,000.
5. Save the filtered output as a CSV file.

## Project Structure

```
Assignment17/
│
├── sales.csv
├── assignment17.ipynb
├── Dockerfile
├── requirements.txt
├── output/
│   └── high_sales_products/
└── README.md
```

## Technologies Used

* Python 3.12
* Apache Spark 3.5.6
* PySpark
* Docker
* JupyterLab

## Build Docker Image

```bash
docker build -t assignment17-app .
```

## Run Docker Container

```bash
docker run -it --rm -p 8080:8080 -v "$(pwd):/workspace" assignment17-app
```

## Output

The application generates:

* Products sorted by sales in descending order.
* Top 3 highest-selling products.
* CSV output containing products with sales greater than 80,000.

## Author

Tashu Gupta
SKIT Jaipur

```
```
