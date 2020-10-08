"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet
"""

import subprocess
import chardet


PINGS = [
    ['ping', 'yandex.ru'],
    ['ping', 'youtube.com']]

for ping in PINGS:
    ping_process = subprocess.Popen(ping, stdout=subprocess.PIPE)
    LIMIT = 10
    for line in ping_process.stdout:
        result = chardet.detect(line)
        print(f"result: {result}")
        line = line.decode(result['encoding']).encode('utf-8')
        print(f"answer: {line.decode('utf-8')}")
        LIMIT -= 1
        if LIMIT <= 0:
            break
