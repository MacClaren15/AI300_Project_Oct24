from flask import Flask, request, render_template
from model import Model

app = Flask(__name__)


# Method 1: Via HTML Form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_input = dict(request.form)
        age = int(form_input['age'])
        gender = form_input['gender']
        married = form_input['married']
        senior_citizen = form_input['senior_citizen']
        has_internet_service = form_input['has_internet_service']
        internet_type = form_input['internet_type']
        has_unlimited_data = form_input['has_unlimited_data']
        has_multiple_lines = form_input['has_multiple_lines']
        contract_type = form_input['contract_type']

        model_inputs = [age, gender, married, senior_citizen, has_internet_service, internet_type, has_unlimited_data, has_multiple_lines, contract_type]
        prediction = Model().predict(model_inputs)
        return render_template('index.html', prediction=prediction)

    return render_template('index.html')


# Method 2: Via POST API
@app.route('/api/predict', methods=['POST'])
def predict():
    request_data = request.get_json()
    print(request_data)

    return {'success': False}, 500


if __name__ == '__main__':
    app.run(debug=True)
