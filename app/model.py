from pathlib import Path
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

try:
    from .preprocessing import load_data, preprocess_data, get_feature_target
except ImportError:
    from preprocessing import load_data, preprocess_data, get_feature_target

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / 'models' / 'fraud_detection_model.pkl'


def train_model(save_path: Path = MODEL_PATH, test_size: float = 0.2, random_state: int = 42):
    df = load_data()
    df = preprocess_data(df)

    X, y = get_feature_target(df)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    model = RandomForestClassifier(random_state=random_state)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print('Model accuracy:', accuracy_score(y_test, y_pred))
    print('Classification report:')
    print(classification_report(y_test, y_pred))

    save_model(model, save_path)
    return model


def save_model(model, path: Path = MODEL_PATH):
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)
    print(f'Model saved to {path}')


def load_model(path: Path = MODEL_PATH):
    return joblib.load(path)


if __name__ == '__main__':
    train_model()
