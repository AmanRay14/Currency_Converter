def currency_converter():
    conversion_rates = {
        "USD": {
            "EUR": 0.82,
            "JPY": 110.58,
            "GBP": 0.76,
            "AUD": 1.28,
            "CAD": 1.18,
            "CHF": 0.88,
            "CNY": 6.52,
            "SEK": 8.92,
            "NZD": 1.36,
            "RUB": 78.65,
        },
        "EUR": {
            "USD": 1.22,
            "JPY": 128.71,
            "GBP": 0.91,
            "AUD": 1.63,
            "CAD": 1.50,
            "CHF": 1.10,
            "CNY": 7.16,
            "SEK": 11.25,
            "NZD": 1.79,
            "RUB": 88.42,
        },
        "JPY": {
            "USD": 0.0090,
            "EUR": 0.0078,
            "GBP": 0.0065,
            "AUD": 0.0117,
            "CAD": 0.0106,
            "CHF": 0.0079,
            "CNY": 0.057,
            "SEK": 0.081,
            "NZD": 0.0123,
            "RUB": 0.67,
            "INR": 0.66, 
        },
        "INR": {
            "USD": 0.0142,
            "EUR": 0.0125,
            "JPY": 1.81,
            "GBP": 0.0102,
            "AUD": 0.016,
            "CAD": 0.015,
            "CHF": 0.011,
            "CNY": 0.082,
            "SEK": 0.12,
            "NZD": 0.018,
            "RUB": 1.09, 
        },
    }

    # Rest of the code remains the same
    from_currency = input("Enter the currency you want to convert from (e.g. USD, EUR): ").upper()
    if from_currency not in conversion_rates:
        return "The entered currency is not supported."

    try:
        amount = float(input("Enter the amount you want to convert: "))
    except ValueError:
        return "The amount entered is not a valid number."

    to_currency = input("Enter the currency you want to convert to (e.g. USD, EUR): ").upper()
    if to_currency not in conversion_rates[from_currency]:
        return "The conversion currency entered is not supported."

    converted_amount = amount * conversion_rates[from_currency][to_currency]
    return f"{amount} {from_currency} is {converted_amount} {to_currency}"

print(currency_converter())
