import pandas as pd


def load_data(file_path):
    """
    Loads data from a CSV file into a pandas DataFrame.
    """
    return pd.read_csv(file_path)


def clean_data(df):
    """
    Cleans the DataFrame by removing duplicates and handling missing values.
    """
    df.drop_duplicates(inplace=True)
    df.fillna(method='ffill', inplace=True)
    return df


def preprocess_data(file_path):
    """
    Full preprocessing pipeline for the data.
    """
    df = load_data(file_path)
    df = clean_data(df)
    return df


if __name__ == '__main__':
    # Example usage
    file_path = 'data.csv'
    processed_data = preprocess_data(file_path)
    print(processed_data.head())
