import pandas as pd

def clean(df):
    df = df.drop_duplicates()
    df = df.fillna(df.median(numeric_only=True))
    return df

def split_data(df, target='target'):
    X = df.drop(target, axis=1)
    y = df[target]
    return X, y  

def normalize(df):
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    cols = df.select_dtypes(include=['int64', 'float64']).columns
    df[cols] = scaler.fit_transform(df[cols])
    return df

def load_data(path):
    return pd.read_csv(path)

def encode(df):
    return pd.get_dummies(df)