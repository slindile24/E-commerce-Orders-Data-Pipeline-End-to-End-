import unittest
import pandas as pd
from ETL_Pipeline.etl_pipeline import *

from unittest.mock import patch

class TestETL(unittest.TestCase):
    @patch("ETL_Pipeline.etl_pipeline.requests.get")
    def test_extract_returns_dataframe(self, mock_get):
        #created mock test for a fake api response 
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {
                'rate': 3.9, 
                'count': 120
            }
        ]
        df = extract()

        self.assertIsInstance(df,pd.DataFrame) #testing if df is indeed a dataframe
        self.assertFalse(df.empty) # testing if we got data back 
        self.assertIn('rate',df.columns) # testing if rate is in columns
        self.assertIn('count',df.columns) # testing if count is in columns

    
    def test_correct_datatypes(self):

        raw_df = pd.DataFrame({
        "id": ["1", "2"],  # inserted strings on purpose
        "title": ["Bag", "Shirt"],
        "price": ["109.95", "29.99"], 
        "rating": [
            {"rate": 3.9, "count": 120},
            {"rate": 4.5, "count": 10}
        ]
        })

        transformed_df = transform(raw_df)
        print(transformed_df.dtypes)


        self.assertTrue(pd.api.types.is_integer_dtype(transformed_df["id"]))
        self.assertTrue(pd.api.types.is_float_dtype(transformed_df["price"]))
        self.assertTrue(pd.api.types.is_float_dtype(transformed_df["rate"]))
        self.assertTrue(pd.api.types.is_integer_dtype(transformed_df["count"]))
        self.assertTrue(pd.api.types.is_string_dtype(transformed_df["title"]))
  






   
        
        

if __name__ == "__main__":
    unittest.main()



