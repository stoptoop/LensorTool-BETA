
# from Utils.serverinfo import *
# from Utils.config import *
# from main import options
from Utils.config import *





import subprocess
import sys

# Список модулей для проверки
modules = [
    "fade", "os", "datetime", "time", "colorama", "requests", 
    "random", "subprocess", "threading", "selenium", 
    "sys", "bs4", "pystyle", "ipaddress", "ping3"
]

# Функция для проверки модуля
def check_module(module_name):
    try:
        __import__(module_name)
        print(f"Модуль '{module_name}' установлен.")
    except ImportError:
        print(f"Модуль '{module_name}' не установлен. Пытаюсь установить...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
        print(f"Модуль '{module_name}' успешно установлен.")

# Проходим по списку модулей и проверяем каждый
for module in modules:
    check_module(module)



# try:
#     token = Choice1TokenDiscord()
#     r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
#     if r.status_code == 200:
#         pass
#     else:
#         print("Error")

#     def DmDeleter(token, channels):
#         for channel in channels:
#             try:
#                 requests.delete(f'https://discord.com/api/v7/channels/'+channel['id'], headers={'Authorization': token})
#                 print(f" Status: Delete| Channel: {channel['id']}")
#             except Exception as e:
#                 print(f"Status: Error: {e}")

#     processes = []
#     channel_id = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': token}).json()
#     if not channel_id:
#         print(f"No Dm found.")
#         main()

#     for channel in [channel_id[i:i+3] for i in range(0, len(channel_id), 3)]:
#             t = threading.Thread(target=DmDeleter, args=(token, channel))
#             t.start()
#             processes.append(t)
#     for process in processes:
#         process.join()

# except Exception as e:
#     print(e)


# def leaver():
#     try:
#         def leaver(guilds, token):
#             for guild in guilds:
#                 try:
#                     time.sleep(1)
#                     response = requests.delete(f'https://discord.com/api/v8/users/@me/guilds/'+guild['id'], headers={'Authorization': token})
#                     if response.status_code == 204 or response.status_code == 200:
#                         print(f"{colored_green(f"[ Success ]")} Leave Server: {colored_green(f"{guild['name']}")}")
#                     elif response.status_code == 400:
#                         response = requests.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], headers={'Authorization': token})
#                         if response.status_code == 204 or response.status_code == 200:
#                             print(f"{colored_green(f"[ Success ]")} Leave {colored_green("Server:")} {guild['name']}")
#                     else:
#                         print(f"{colored_red_purple(f"[ Error ]")} Error {colored_red_purple(f"{response.status_code}")} Server: {colored_red_purple(f"{guild['name']}")}")
#                 except Exception as e:
#                     print(f"{colored_red_purple(f"[ Error ]")} Error: {colored_red_purple(f"{e}")}")
        
#         token = Choice1TokenDiscord()

#         processes = []
#         guilds_id = requests.get("https://discord.com/api/v8/users/@me/guilds", headers={'Authorization': token}).json()
#         if not guilds_id:
#             print(f"{colored_red_purple("No Server found.")}")
#         for guild in [guilds_id[i:i+3] for i in range(0, len(guilds_id), 3)]:
#             leaver(guild, token)
#     except Exception as e:
#        print(e)



# leaver()



# os.system('cls||clear')
# try:
#     def raid(tokens, channels, message):
#         try:
#             token = random.choice(tokens)
#             token_lens = token[:15] + "..."
#             channel = random.choice(channels)
#             response = requests.post(f"https://discord.com/api/channels/{channel}/messages", data={'content': message}, headers={'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7', 'Authorization': token})
#             response.raise_for_status()
#             print(f"{now_time()}{colored_green("[ Success ]")} {colored_green(f"Message:")} {message_sensur} {colored_green("Channel id: ")}{channel} {colored_green("Token: ")}{token_lens}")
#         except:
#             if response.status_code == 429:
#                 retry_after = response.json().get('retry_after')  # Получаем время ожидания
#                 print(f"{now_time()}{colored_yellow(f"[ Rate limit: {retry_after} ]")} {colored_yellow(f"Message:")} {message_sensur} {colored_yellow("Channel id: ")}{channel} {colored_yellow("Token: ")}{token_lens}")
#             else:
#                 print(f"{now_time()}{colored_red_purple(f"[ Error {response.status_code} ]")} {colored_red_purple(f"Message:")} {message_sensur} {colored_red_purple("Channel id: ")}{channel} {colored_red_purple("Token: ")}{token_lens}")


#     tokens = ChoiceMultiTokenDisord()
#     channels = ChoiceMultiChannelDiscord()



#     def Status_Change():
#         yes_in = ["yes", "y", "Y", "Yes", "YES"]
#         change_status = input(f"{now_time()}~ Change Status Tokens (y/n) ~ {purple}[ {end}> {purple}]  {end}")


#         if change_status in yes_in:
#             CustomStatus = {"custom_status": {"text": "Made By Lensor..."},
#                             "status": "online"
#                             }

#             def change_status_for_token(token):
#                 try:
#                     headers = {'Authorization': token, 'Content-Type': 'application/json'}
#                     # Отправляем PATCH-запрос для изменения статуса
#                     r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus)
                    
#                     # Проверяем статус ответа
#                     if r.status_code == 200:
#                         print(f"{colored_green("[ Success ]")} Статус для токена {colored_yellow(f"{token[:12]}...")} изменен")
#                     else:
#                         print(f"{colored_red_purple(f"[ Error {r.status_code} - {r.text} ]")} Статус для токена {colored_yellow(f"{token[:12]}...")} не изменен")
#                 except Exception as e:
#                     print(f"{colored_red_purple(f"[ Error {e} ]")} Статус для токена {colored_yellow(f"{token[:12]}...")} не изменен")
#             # Итерация по всем токенам и изменение статуса для каждого
#             for token in tokens:
#                 change_status_for_token(token)

#         else: 
#             return



#     def ping_everyone():
#         yes_in = ["yes", "y", "Y", "Yes", "YES"]
#         ping_everyone = input(f"{now_time()}~ Ping Everyone (y/n) ~ {purple}[ {end}> {purple}]  {end}")
#         if ping_everyone in yes_in:
#             ping_everyone = True
#             return " @everyone"
#         else: 
#             ping_everyone = False
#             return ""
        

#     message = input(f"{now_time()}~ Spam Message ~ {purple}[ {end}> {purple}]  {end}")
#     message = message +  ping_everyone()
#     message_len = len(message)
#     if message_len > 12:
#         message_sensur = message[:12]
#         message_sensur = message_sensur + "..."
#     else:
#         message_sensur = message

#     Status_Change()
            
#     def request():
#         threads = []
#         try:
#             while True:
#                 time.sleep(0.09)
#                 t = threading.Thread(target=raid, args=(tokens, channels, message))
#                 t.start()
#                 threads.append(t)
#         except:
#             print("error")
            

#         for thread in threads:
#             thread.join()

#     while True:
#         request()
# except Exception as e:
#     print(e)







# import requests

# # Список токенов
# tokens = ChoiceMultiTokenDisord()

# # Статус, который вы хотите установить
# CustomStatus = {"custom_status": {"text": "By Lensor..."}}

# # Функция для изменения статуса
# def change_status_for_token(token):
#     try:
#         headers = {'Authorization': token, 'Content-Type': 'application/json'}
#         # Отправляем PATCH-запрос для изменения статуса
#         r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus)
        
#         # Проверяем статус ответа
#         if r.status_code == 200:
#             print(f"Статус для токена {token[:10]}... изменен успешно")
#         else:
#             print(f"Ошибка изменения статуса для токена {token[:10]}...: {r.status_code} - {r.text}")
#     except Exception as e:
#         print(f"Произошла ошибка с токеном {token[:10]}...: {str(e)}")

# # Итерация по всем токенам и изменение статуса для каждого
# for token in tokens:
#     change_status_for_token(token)






# import time
# import sys

# # Символи для індикації завантаження
# loading_symbols = ["│", "╱", "─", "╲"] 

# # Основний цикл
# while True:
#     for symbol in loading_symbols:
#         # Виведення символу без переносу на новий рядок
#         sys.stdout.write(f"\rloading biblioteks {symbol}")
#         sys.stdout.flush()
#         time.sleep(0.5)  # Затримка 1 секунда



# def port_scanner_func():
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     try:
#         def port_scanner(ip):
#             port_protocol_map = {
#                 21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 69: "TFTP",
#                 80: "HTTP", 110: "POP3", 123: "NTP", 143: "IMAP", 194: "IRC", 389: "LDAP",
#                 443: "HTTPS", 161: "SNMP", 3306: "MySQL", 5432: "PostgreSQL", 6379: "Redis",
#                 1521: "Oracle DB", 3389: "RDP", 1900: "SSDP"
#             }

#             def scan_port(ip, port):
#                 try:
#                     now_sock = datetime.now()
#                     current_time_sock = now_sock.strftime("%H:%M:%S")
#                     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#                     sock.settimeout(0.1)
#                     result = sock.connect_ex((ip, port))
#                     if result == 0:
#                         protocol = identify_protocol(ip, port)
#                         print(f"{now_time()}", colored_green(f"Port: {port} Status: Open Protocol: {protocol}"))
#                     sock.close()
#                 except:
#                     pass

#             def identify_protocol(ip, port):
#                 try:
#                     if port in port_protocol_map:
#                         return port_protocol_map[port]
#                     else:
#                         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#                         sock.settimeout(0.5)
#                         sock.connect((ip, port))
                        
#                         sock.send(b"GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(ip).encode('utf-8'))
#                         response = sock.recv(100).decode('utf-8')
#                         if "HTTP" in response:
#                             return "HTTP"
                        
#                         sock.send(b"\r\n")
#                         response = sock.recv(100).decode('utf-8')
#                         if "FTP" in response:
#                             return "FTP"
                        
#                         sock.send(b"\r\n")
#                         response = sock.recv(100).decode('utf-8')
#                         if "SSH" in response:
#                             return "SSH"
#                         return "Unknown"
                    
#                 except:
#                     return "Unknown"


#             with concurrent.futures.ThreadPoolExecutor() as executor:
#                 results = {executor.submit(scan_port, ip, port): port for port in range(1, 65535 + 1)}
#             concurrent.futures.wait(results)



#         def is_valid_ip(ip):
#             try:
#                 ipaddress.ip_address(ip)
#                 return True
#             except ValueError:
#                 return False
            
#         def is_ip_reachable(ip):
#             try:
#                 response = ping(ip, timeout=2)
#                 return response is not None
#             except Exception as e:
#                 print(f"Error: {e}")
#                 return False


#         ip = input(f"{now_time()}~ Insert Ip ~ {purple}[ {end}> {purple}]  {end}")
#         input_without_dots = ip.replace('.', '')




#         if is_valid_ip(ip):
#             if is_ip_reachable(ip):
#                 print(f"{now_time()}", colored_yellow(f"Start Scanning...                          Restart the program to stop"))
#                 port_scanner(ip)
#             else:
#                 print(f"{now_time()}", colored_red_purple(f"IP address unavailable"))
#                 port_scanner_func()
#         elif ip == "15":
#             banner()
#             main()
#         else:
#             print(f"{now_time()}", colored_red_purple(f"Something went wrong please check your input"))
#             port_scanner_func()



#         # if input_without_dots.isdigit():
#         #   print(f"{purple}[ {end}{current_time} {purple}] {end}", colored_yellow(f"Start Scanning...                          Restart the program to stop"))
#         #   port_scanner(ip)

#         # else:
#         #   print(f"{purple}[ {end}{current_time} {purple}] {end}", colored_red_purple(f"Something went wrong please check your input"))
#         #   port_scanner_func()
#         # print()

#     except Exception as e:
#         print(e)



# port_scanner_func()


# import requests


# try:
#     response = requests.get(f"https://discordstatus.com/api/v2/summary.json")
#     api = response.json()

#     # Получаем все компоненты
#     components = api.get('components', [])

#     # Устанавливаем список нужных id
#     target_ids = ["rhznvxg4v7yh", "ly7bf56hshjc", "dmyjqtpgpjkr", "8r4xqnt9jslk", "gvg1c6688r5y", "x7rnz0t7dpnp", "6j5lgxtyjfc2", "jk03xttfcz9b"]

#     # Проходим по каждому компоненту и выводим только те, у которых id совпадает
#     for component in components:
#         if component.get('id') in target_ids:   
#             print(now_time(), colored_yellow(f"ID: {component.get('id')}"))
#             print(now_time(), colored_yellow(f"Name: {component.get('name')}"))
#             print(now_time(), colored_yellow(f"Description: {component.get('description')}"))
#             print(now_time(), colored_green(f"Status: {component.get('status')}"))
#             print(now_time(), colored_yellow(f"Updated at: {component.get('updated_at')}"))
#             print("-" * 40)  # Разделитель для наглядности между компонентами
#     main()





# except Exception as e:
#     print(colored_red_purple(f"Error occured try again later or Contact the developer"))













# options = {
#     1: "Tokens Info Check",
#     2: "Server Info Check ",
#     3: "Token Browser Open",
#     4: "Test option",
#     5: "Test option",
#     6: "Test option",
#     7: "Test option",
#     8: "Ip Port Scanner",
#     9: "Ip Pinger",
#     10: "Test option",
#     11: "Test option",
#     12: "Test option",
#     13: "Test option",
#     14: "Test option",
#     15: "Clear"
# }




# import fade
# import os
# from datetime import datetime, timezone
# import time
# import colorama
# import requests, random, subprocess, threading
# from selenium import webdriver
# import sys
# from bs4 import BeautifulSoup
# import socket
# import concurrent.futures
# from pystyle import Colors, Colorate
# import ipaddress
# from ping3 import ping






# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")


# end = "\033[0m"
# purple = "\033[1;35m"
# red = "\033[0;31m"
# green = "\033[0;32m"
# white  = "\033[37m"


# def colored_red_purple(text):
#     return Colorate.Horizontal(Colors.red_to_purple, f"{text}", 1)











# def now_time():
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     return (f"{purple}[ {end}{current_time} {purple}] {end}")








# def ip_ping():
#     try:
#         def ping_ip(hostname, port, bytes):
#             try:
#                 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#                 sock.settimeout(2)
#                 start_time = time.time() 
#                 sock.connect((hostname, port))
#                 data = b'\x00' * bytes
#                 sock.sendall(data)
#                 end_time = time.time() 
#                 elapsed_time = (end_time - start_time) * 1000 
#                 print(colored_red_purple(f'Hostname: {white}{hostname}{red} time: {white}{elapsed_time:.2f}ms{red} port: {white}{port}{red} bytes: {white}{bytes}{red} status: {white}succeed{red}'))
#             except:
#                 elapsed_time = 0
#                 print(f'Hostname: {white}{hostname}{red} time: {white}{elapsed_time}ms{red} port: {white}{port}{red} bytes: {white}{bytes}{red} status: {white}fail{red}')


#         hostname = input(f"{now_time()}Ip -> " )

#         try:
#             port_input = input(f"{now_time()}port (enter for default) -> ")
#             if port_input.strip():
#                 port = int(port_input)
#             else:
#                 port = 80  
            
#             bytes_input = input(f"{now_time()}Bytes (enter for default) -> " )
#             if bytes_input.strip():
#                 bytes = int(bytes_input)
#             else:
#                 bytes = 64
#         except:
#             print(": ERROR")

#         while True:
#             ping_ip(hostname, port, bytes)

#     except Exception as e:
#         print(f": ERROR as {e}")


# ip_ping()













# while True:




#     def is_valid_ip(ip):
#         try:
#             ipaddress.ip_address(ip)
#             return True
#         except ValueError:
#             return False




#     def is_ip_reachable(ip):
#         try:
#             response = ping(ip, timeout=2)
#             return response is not None
#         except Exception as e:
#             print(f"Ошибка: {e}")
#             return False

#     ip = input("Введите IP-адрес: ")

#     if is_valid_ip(ip):
#         if is_ip_reachable(ip):
#             print(f"IP-адрес {ip} доступен.")
#         else:
#             print(f"IP-адрес {ip} недоступен.")
#     else:
#         print(f"IP-адрес {ip} некорректен.")