"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import chardet
import subprocess


ping_resurs = [['ping', 'yandex.ru'],['ping', 'youtube.com']]

for ping_now in ping_resurs:

    ping_process = subprocess.Popen(ping_now, stdout=subprocess.PIPE)

    i = 0

    for line in ping_process.stdout:

        if i<10:
            print(line)
            line = line.decode('cp866').encode('utf-8')
            print(line.decode('utf-8'))
            i += 1
        else:
            break