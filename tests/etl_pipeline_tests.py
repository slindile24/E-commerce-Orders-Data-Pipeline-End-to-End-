import unittest
import pandas as pd
from ETL_Pipeline.etl_pipeline import extract

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
        

if __name__ == "__main__":
    unittest.main()



