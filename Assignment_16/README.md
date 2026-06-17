# Assignment 16 - PySpark RDD Processing

## Objective

Process employee data using PySpark RDDs.

### Tasks Performed

1. Read CSV file into RDD.
2. Sort employees by salary in descending order.
3. Calculate department-wise total salary.
4. Identify top 3 highest-paid employees.
5. Save top 3 employees to output file.

## Technologies Used

- Python
- Apache Spark
- PySpark
- Docker
- Jupyter Notebook

## Dataset

employee.csv

## Build Docker Image

docker build -t assignment16-app .

## Run Container

docker run -it --rm -p 8080:8080 -v "$(pwd):/workspace" assignment16-app

## Output

Top 3 Employees:
- Priya
- Neha
- Rohit