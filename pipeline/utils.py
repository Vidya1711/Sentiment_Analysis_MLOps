import logging
import pandas as pd
from src.data_cleaning import DataCleaning,DataPreprocessingStrategy

def get_data_for_test():
    try:
        df = pd.read_csv("/home/miniuser/MLOPS/SentimentAnalysis/data/all-data.csv",encoding='iso-8859-1')
        df = df.sample(n=100)
        preprocess_strategy = DataPreprocessingStrategy()
        data_cleaning = DataCleaning(df,preprocess_strategy)
        df = data_cleaning.handle_data()
        df.drop(["Sentiments"], axis=1, inplace=True)
        result = df.to_json(orient = "split")
        return result
    except Exception as e:
        logging.error(e)
        raise e 