# Проверка работоспособности импорта модуля utils.py
import utils

print(*utils.currency_rates('usd'))
print(*utils.currency_rates('EUR'))
print(*utils.currency_rates('www'))
