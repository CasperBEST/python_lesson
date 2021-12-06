import re

PATTERN = re.compile(r'([0-9a-fA-F]{1,4}(?:[.:][0-9a-fA-F]{,4}){3,7})\s-\s-\s\['
                     r'(\d{2}/\w{3}/\d{4}(?:[:]\d{2}){3}\s\+\d{4})]\s"'
                     r'(\w+)\s/\w+/\w+\d\s\w+/\d\.\d"\s'
                     r'(\d{3})\s(\d+)')

with open('nginx_logs.txt', encoding='UTF-8') as f:
    for line in f:
        result = PATTERN.findall(line)
        print(*result)
