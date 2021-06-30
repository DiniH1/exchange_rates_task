class ExchangeCurrency:
    def show_currency_base(currency_dict):
        currency_base = currency_dict['base']
        print(f"The base currency is {currency_base}")

    def show_exchange_currencies(currency_dict):
        currency_rates = currency_dict["rates"]
        for key, value in currency_rates.items():
            print(f" The currency is {key} and the rate is {value}")

    def show_rate(currency_dict):
        user_prompt = input("What currency do want to see the rate for? ").upper()
        currency_rate = currency_dict['rates'][user_prompt]
        print(currency_rate)