import joblib

class Model:
    def __init__(self):
        self.model = joblib.load('model/rf_AI300.pkl')

    def predict(self, input_features):
        return self.model.predict_proba(input_features)