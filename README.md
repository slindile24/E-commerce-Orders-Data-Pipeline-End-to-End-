# E-commerce-Orders-Data-Pipeline-End-to-End-

# This is an end-to-end data pipeline that :
1. Extract

Data is extracted from a public REST API.

For this project, the Fake Store API is used to retrieve e-commerce product/order data.

2. Transform

The extracted data is cleaned and validated.

This step ensures:

Required fields are present

Data types are correct

Invalid or inconsistent records are handled appropriately

3. Load

The transformed data is loaded into a PostgreSQL database.

The database serves as the final storage layer for analytics and reporting.

## Tech Stack
- Python  
- Pandas  
- Requests  
- PostgreSQL  
- SQLAlchemy  
- psycopg2  
- python-dotenv  

## How to Run the Project
1. Just hit that run button on vscode as I made it easier to just run the whole pipeline at once .

The end output will be : "Data is loaded successfully into Postgres"