import joblib

class Model:
    def __init__(self):
        self.model = joblib.load('model/rf_auc_score.pkl')

    def predict(self, input_features):
        return self.model.predict(input_features)