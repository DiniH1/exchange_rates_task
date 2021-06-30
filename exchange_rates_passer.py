from app.exchange_currencies import ExchangeCurrency
import json

currency = open("exchange_rates.json", 'r')
currency_dict = json.load(currency)

print(currency_dict)
print(ExchangeCurrency.show_currency_base(currency_dict))
print(ExchangeCurrency.show_currency_base())
print(ExchangeCurrency.show_exchange_currencies(currency_dict))
print(ExchangeCurrency.show_rate(currency_dict))