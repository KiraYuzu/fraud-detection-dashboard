from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / 'data' / 'transactions.csv'


def load_data(path: Path = None) -> pd.DataFrame:
    """Load the transaction dataset from disk."""
    if path is None:
        path = DATA_PATH
    return pd.read_csv(path)


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocess transaction data for modeling."""
    df = df.copy()

    # Ensure datetime values are parsed
    df['transaction_time'] = pd.to_datetime(df['transaction_time'], errors='coerce')

    # Create the features used in the model
    df['hour'] = df['transaction_time'].dt.hour
    df['is_overseas'] = (df['country'] != 'Singapore').astype(int)

    # Keep only the required columns for modeling
    return df


def get_feature_target(df: pd.DataFrame, features=None):
    """Return feature matrix X and target vector y."""
    if features is None:
        features = ['amount', 'hour']

    X = df[features]
    y = df['is_fraud']
    return X, y
