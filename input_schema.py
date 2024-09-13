INPUT_SCHEMA = {
    "questions": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["What is your age?"]
    },
    "responses": {
        'datatype': 'STRING',
        'required': True,
        'shape': [2],
        'example': ["I am 20 years old.","good morning"]
    },
    "response_contexts": {
        'datatype': 'STRING',
        'required': True,
        'shape': [2],
        'example': ["I will be 21 next year.", "great day."]
    }
}
