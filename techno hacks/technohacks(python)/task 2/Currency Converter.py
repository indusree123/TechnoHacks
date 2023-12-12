from forex_python.converter import CurrencyRates

def convert_currency():
    c = CurrencyRates()

    print("Welcome to the Currency Converter!")
    
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the source currency code (e.g., USD): ").upper()
    to_currency = input("Enter the target currency code (e.g., EUR): ").upper()

    try:
        exchange_rate = c.get_rate(from_currency, to_currency)
        converted_amount = round(amount * exchange_rate, 2)
        print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    convert_currency()
