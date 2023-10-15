import requests

data = {
    
    "gender": 0,
    "height": 183,
    "weight": 93.0,
    "ap_hi": 168,
    "ap_lo": 62.0,
    "cholesterol": 1,
    "gluc": 0,
    "smoke": 0,
    "alco": 1,
    "active": 0,
    "age_years": 50.0,
    "bmi": 25.0,  # Fill in the value for "bmi"
    "pulse_pressure": 106,  # Fill in the value for "pulse_pressure"
    # Fill in the value for "bmi_category"
    "age_category_elderly": 0,  # Fill in the value for "age_category_elderly"
    "age_category_middle_aged": 1,  # Fill in the value for "age_category_middle_aged"
    "age_category_young": 0,  # Fill in the value for "age_category_young"
    "bmi_category_normal": 1,  # Fill in the value for "bmi_category_normal"
    "bmi_category_obese": 0,  # Fill in the value for "bmi_category_obese"
    "bmi_category_overweight": 0,  # Fill in the value for "bmi_category_overweight"
    "bmi_category_underweight": 0,  # Fill in the value for "bmi_category_underweight"
    "bmi_category_nan": 0,  # Fill in the value for "bmi_category_nan"
    "age_years_1": 50.0,  # Fill in the value for "age_years_1"
    "pulse_pressure_1": 106,  # Fill in the value for "pulse_pressure_1"
    "age_years_pulse_pressure": 50.0  # Fill in the value for "age_years_pulse_pressure"
}

response = requests.get('http://127.0.0.1:8001/predict', json=data)

result = response.json()

print(result)