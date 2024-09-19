import pandas as pd

class DataLoader:
    def __init__(self, data_path):
        self.data_path = data_path
        self.train = None
        self.test = None
        self.store = None
        self.sample_submission = None

    def load_data(self):
        # Load the data
        self.train = pd.read_csv(f"{self.data_path}/train.csv")
        self.test = pd.read_csv(f"{self.data_path}/test.csv")
        self.store = pd.read_csv(f"{self.data_path}/store.csv")
        self.sample_submission = pd.read_csv(f"{self.data_path}/sample_submission.csv")
        
        print("Data Loaded Successfully")
        return self.train, self.test, self.store, self.sample_submission

    def check_missing_data(self, df):
        # Check for missing data in a dataframe
        missing_data = df.isnull().sum()
        print("Missing Data in the Dataset:")
        print(missing_data)
        return missing_data

    def initial_exploration(self, df):
        # Basic exploration: shape, columns, head
        print(f"Shape of dataset: {df.shape}")
        print(f"Columns: {df.columns}")
        print(f"First 5 rows:\n{df.head()}")