import requests
import pandas as pd

def extract(): 

    FAKE_STORE_URL = "https://fakestoreapi.com/products" # url for all products 

    try:
        response = requests.get(FAKE_STORE_URL)  #response from api
        response.raise_for_status()  # automatically raises an exception when an error occurs

        data = response.json() #returns the data as json
        df = pd.DataFrame(data)
        return df # returns data in the form of a dataFrame .

    except requests.exceptions.RequestException as e:
        print(f"An error occurred : {e}")

if __name__ == "__main__":
    print(extract().head())