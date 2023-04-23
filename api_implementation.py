import json
import requests

url = 'https://9eb5-35-240-234-68.ngrok.io/diabetes_prediction'

input_data_for_model = {

    'Pregnancies' :  6  ,
    'Glucose' :  148,
    'BloodPressure' : 72,
    'SkinThickness' : 35,
    'Insulin' : 0,
    'BMI' : 33.6,
    'DiabetesPedigreeFunction' : 0.627,
    'Age' : 50
}

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)