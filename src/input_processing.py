def format_model_inputs(input_dict):
    age = int(input_dict['age'])
    gender = input_dict['gender']
    married = input_dict['married']
    senior_citizen = input_dict['senior_citizen']
    has_internet_service = input_dict['has_internet_service']
    internet_type = input_dict['internet_type']
    has_unlimited_data = input_dict['has_unlimited_data']
    has_multiple_lines = input_dict['has_multiple_lines']
    contract_type = input_dict['contract_type']

    return [age, gender, married, senior_citizen, has_internet_service, internet_type, has_unlimited_data, has_multiple_lines, contract_type]


def validate(input_dict):
    errors = []

    required_fields = ['age', 'gender', 'married', 'senior_citizen', 'has_internet_service', 'internet_type', 'has_unlimited_data', 'has_multiple_lines', 'contract_type']

    for field in required_fields:

        if field not in input_dict:
            errors.append(f'{field} not found in request.')

        if field in ['age'] and type(input_dict[field]) != int \
                and not input_dict[field].isnumeric():
            errors.append(f'Age field must be int type.')

    return errors
