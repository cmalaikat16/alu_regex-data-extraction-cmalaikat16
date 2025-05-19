# ALU Regex Data Extraction

This project implements various validation functions using Regular Expressions (Regex) to validate different types of data, including Phone numbers, Credit Card Number, Hashtags, Currency amounts, and HTML tags.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Validation Functions](#validation-functions)
- [Example Data](#example-data)
- [License](#license)

## Features

- Validate phone numbers in various formats
- Validate Credit card Numbers
- Validate Hashtags
- Validate currency amounts
- Validate HTML tags

## Installation

To get started, clone the repository:

```bash
git clone https://github.com/yourusername/alu_regex-data-extraction-yourusername.git
cd alu_regex-data-extraction-yourusername
```

## Usage

- Run the script using Python i.e python regex.py

## Validation Functions

- Phone Number Validation
Function: is_valid_phone(phone)
Validates various phone number formats.
Regex Pattern: '^(\(\d{3}\)\s|\d{3}[-.])\d{3}[-.]\d{4}$'

- Currency Amount Validation
Function: is_valid_currency(amount)
Checks if the currency amount is in the correct format.
Regex Pattern: '^\$\d{1,3}(,\d{3})*(\.\d{2})?$'

- HTML Tag Validation
Function: is_valid_html_tag(tag)
Validates if the provided string is a valid HTML tag.
Regex Pattern: '^<\s*\w+(\s+[\w\-]+(=\s*"(?:[^"]|\\")*")?)?\s*/?>$'

- Hashtag Validation
Function: is_valid_hashtag(hashtag)
Description: Validates if the provided string is a valid hashtag.
Regex Pattern: '^#\w+$'

- Credit Card Number Validation
Function: is_valid_credit_card(card_number)
Description: Validates if the provided credit card number is in a valid format.
Regex Pattern: '^(\d{4}[-\s]?){3}\d{4}$'

## Example Data

- Phones:
Valid: (123) 456-7890, 123-456-7890
Invalid: 4567890

- Credit Card Numbers:
Valid: 1234-5678-9012-3456, 1234 5678 9012 3456
Invalid: 1234567890123456

- Hashtags:
Valid: #example, #ThisIsAHashtag
Invalid: #invalid hashtag

- HTML Tags:
Valid: <p>, <div class='example'>
Invalid: <invalid-tag>

- Currencies:
Valid: $19.99, $1,234.56
Invalid: $123456.78

## License
This project is licensed under the MIT License. See the LICENSE file for details.