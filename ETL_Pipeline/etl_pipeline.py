import requests
import pandas as pd

def extract(): 

    FAKE_STORE_URL = "https://fakestoreapi.com/products" # url for all products 

    try:
        response = requests.get(FAKE_STORE_URL)  #response from api
        response.raise_for_status()  # automatically raises an exception when an error occurs

        data = response.json() #returns the data as json
        df = pd.DataFrame(data)
        return(df)# returns data in the form of a dataFrame .

    except requests.exceptions.RequestException as e:
        print(f"An error occurred : {e}")

raw_df = extract()

def transform(df):
    """Took a snippet of how the json response looks so that I can highlight what to clean and validate:
    {'id': 1, 'title': 'Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops',
      'price': 109.95,
    'description': 'Your perfect pack for everyday use and walks in the forest.
    Stash your laptop (up to 15 inches) in the padded sleeve, your everyday', 
    'category': "men's clothing", 
    'image': 'https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png', 
    'rating': {'rate': 3.9, 'count': 120} }
    """
    # print(df["rating"].iloc[0])
    df["rate"] = df["rating"].apply(lambda x: x['rate'])
    df["count"] = df["rating"].apply(lambda x: x['count'])
    # created two new columns rate and count to drop the nested dict column
    df = df.drop(columns=["rating"])
    df["rate"] = df["rate"].astype(float)
    df["count"] = df["count"].astype(int)
    df["id"] = df["id"].astype(int)
    df['price'] = df['price'].astype(float)
    df["title"] = df["title"].astype(str)
    
    df = df[df["id"] > 0]
    df = df[df["price"] > 0]
    df = df[df["count"] >= 0]
    df = df[(df["rate"] >= 0)]
    df = df[df["title"].notna()]

    return df

    
 



if __name__ == "__main__":
    # print(extract())
    print(transform(raw_df).head())