import re

# Phone number validation
def is_valid_phone(phone):
    pattern = r'^(\(\d{3}\)\s|\d{3}[-.])\d{3}[-.]\d{4}$'
    return re.match(pattern, phone) is not None

# Credit card number validation
def is_valid_credit_card(card_number):
    pattern = r'^(\d{4}[-\s]?){3}\d{4}$'
    return re.match(pattern, card_number) is not None

# Time validation (12-hour and 24-hour format)
def is_valid_time(time):
    pattern = r'^([01]?\d|2[0-3]):([0-5]\d)(\s?[APap][mM])?$'
    return re.match(pattern, time) is not None

# Currency amount validation
def is_valid_currency(amount):
    pattern = r'^\$\d{1,3}(,\d{3})*(\.\d{2})?$'
    return re.match(pattern, amount) is not None

# Example usage
test_data = {
    "phones": [
        "(123) 456-7890",
        "123-456-7890",
        "123.456.7890",
        "4567890"
    ],
    "credit_cards": [
        "1234-5678-9012-3456",
        "1234 5678 9012 3456",
        "1234567890123456"
    ],
    "times": [
        "14:30",
        "2:30 PM",
        "12:00 AM",
        "25:00"
    ],
    "currencies": [
        "$19.99",
        "$1,234.56",
        "$123456.78"
    ]
}

# Testing all fields
for phone in test_data["phones"]:
    print(f"Phone '{phone}' is valid? {is_valid_phone(phone)}")

for card in test_data["credit_cards"]:
    print(f"Credit Card '{card}' is valid? {is_valid_credit_card(card)}")

for time in test_data["times"]:
    print(f"Time '{time}' is valid? {is_valid_time(time)}")

for currency in test_data["currencies"]:
    print(f"Currency '{currency}' is valid? {is_valid_currency(currency)}")
    