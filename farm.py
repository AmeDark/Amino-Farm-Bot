print("Created by Ame.\n")

def modules():
    import os
    import time
    
    while True:
        try:
            import threading
            import samino, aminofix, uuid
            
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
    
print("Проверка модулей.\n")
modules()

import os, sys, time, uuid
import samino, aminofix
from threading import Thread
from getpass import getpass

print("Проверка модулей прошла успешно.\n")

client = aminofix.Client()
req = client.get_from_code(input("Link for blog >> ")).json["extensions"]["linkInfo"]
print()

com_id = req["ndcId"]
blog_id = req["objectId"]

password = getpass()
print()

for email in open("emails.txt", "r").read().split():
    client = samino.Client(uuid.uuid4())
    
    client.login(email = email, password = password)
    
    print(email + ": " + str(0) + "%.      ")
    for x in range(200):
        Thread(target = client.watch_ad).start()
        res = round(((x + 1) / 200) * 100, 2)
        print("\033[A" + email + ": " + str(res) + "%.")
		
    time.sleep(10)

    client.logout()
	
print("""\nФарм окончен.
	Подготовка к отправке монет.\n""")
time.sleep(5)

os.system("mkdir meow")

x = 1
for email in open("emails.txt", "r").read().split():
    open("meow/{}.py".format(x), "w").write("""import os
import aminofix
    
client = aminofix.Client()
email = '""" + str(email) + """'
password = '""" + str(password) + """'
com_id = '""" + str(com_id) + """'
blog_id = '""" + str(blog_id) + """'

client.login(email = email, password = password)

client.join_community(com_id)
sub_client = aminofix.SubClient(comId = com_id, profile = client.profile)
	
coins = int(client.get_wallet_info().totalCoins)
try:
    sub_client.send_coins(coins, blogId = blog_id)
		
except: pass
	
print(f"{email} sended: {coins} coins.")
	
client.leave_community(com_id)

client.logout()""")

    x += 1
	
for i in range(x - 1):
    os.system("python meow/{}.py & Ананасик".format(i + 1))

print("""\nПодготовка окончена
	Отправляем монеты.\n""")

time.sleep(10)
os.system("rm -r meow")
			
time.sleep(100)
