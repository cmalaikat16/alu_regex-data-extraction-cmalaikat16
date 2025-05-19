import re

# Phone number validation
def is_valid_phone(phone):
    pattern = r'^(\(\d{3}\)\s|\d{3}[-.])\d{3}[-.]\d{4}$'
    return re.match(pattern, phone) is not None

# Credit card number validation
def is_valid_credit_card(card_number):
    pattern = r'^(\d{4}[-\s]?){3}\d{4}$'
    return re.match(pattern, card_number) is not None

# Hashtag validation
def is_valid_hashtag(hashtag):
    pattern = r'^#\w+$'
    return re.match(pattern, hashtag) is not None

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
    "hashtags": [
        "#example",
        "#ThisIsAHashtag",
        "#123",
        "#"
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

for hashtag in test_data["hashtags"]:
    print(f"Hashtag '{hashtag}' is valid? {is_valid_hashtag(hashtag)}")

for currency in test_data["currencies"]:
    print(f"Currency '{currency}' is valid? {is_valid_currency(currency)}")
