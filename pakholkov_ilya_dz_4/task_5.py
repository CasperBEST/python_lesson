# Импорт sys для возможности запуска из терминала
import sys

import utils

if len(sys.argv) <= 1:
    sys.argv.append('')
print(*utils.currency_rates(sys.argv[1]))
