import re

def validate_email(mail):
    return bool(re.match(r'^[\w.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$', mail))

def calculate_area(x, y):
    if x < 0 or y < 0:
        raise ValueError("Dimensions must be positive")
    return x * y

def get_even_numbers(data):
    result = []
    for num in data:
        if num % 2 == 0:
            result.append(num)
    return result

def convert_date(input_date):
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', input_date):
        raise ValueError("Invalid date format")
    
    parts = input_date.split('-')
    return f"{parts[2]}.{parts[1]}.{parts[0]}"

def check_palindrome(text):
    clean_text = ''.join(re.findall(r'[a-zA-Z0-9]', text)).lower()
    return clean_text == clean_text[::-1]