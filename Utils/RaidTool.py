from Utils.config import *
import requests


def raidtool():
    try:
        def raid(tokens, channels, message):
            try:
                token = random.choice(tokens)
                token_lens = token[:15] + "..."
                channel = random.choice(channels)
                response = requests.post(f"https://discord.com/api/channels/{channel}/messages", data={'content': message}, headers={'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7', 'Authorization': token})
                response.raise_for_status()
                print(f"{now_time()}{colored_green("[ Success ]")} {colored_green(f"Message:")} {message_sensur} {colored_green("Channel id: ")}{channel} {colored_green("Token: ")}{token_lens}")
            except:
                if response.status_code == 429:
                    retry_after = response.json().get('retry_after')  # Получаем время ожидания
                    print(f"{now_time()}{colored_yellow(f"[ Rate limit: {retry_after} ]")} {colored_yellow(f"Message:")} {message_sensur} {colored_yellow("Channel id: ")}{channel} {colored_yellow("Token: ")}{token_lens}")
                else:
                    print(f"{now_time()}{colored_red_purple(f"[ Error {response.status_code} ]")} {colored_red_purple(f"Message:")} {message_sensur} {colored_red_purple("Channel id: ")}{channel} {colored_red_purple("Token: ")}{token_lens}")


        tokens = ChoiceMultiTokenDisord()
        channels = ChoiceMultiChannelDiscord()



        def Status_Change():
            yes_in = ["yes", "y", "Y", "Yes", "YES"]
            change_status = input(f"{now_time()}~ Change Status Tokens (y/n) ~ {purple}[ {end}> {purple}]  {end}")


            if change_status in yes_in:
                CustomStatus = {"custom_status": {"text": "Made By Lensor..."},
                                "status": "online"
                                }

                def change_status_for_token(token):
                    try:
                        headers = {'Authorization': token, 'Content-Type': 'application/json'}
                        # Отправляем PATCH-запрос для изменения статуса
                        r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus)
                        
                        # Проверяем статус ответа
                        if r.status_code == 200:
                            
                            print(f"{colored_green("[ Success ]")} Статус для токена {colored_yellow(f"{token[:12]}...")} изменен")
                        else:
                            print(f"{colored_red_purple(f"[ Error {r.status_code} - {r.text} ]")} Статус для токена {colored_yellow(f"{token[:12]}...")} не изменен")
                    except Exception as e:
                        print(f"{colored_red_purple(f"[ Error {e} ]")} Статус для токена {colored_yellow(f"{token[:12]}...")} не изменен")
                # Итерация по всем токенам и изменение статуса для каждого
                for token in tokens:
                    change_status_for_token(token)

            else: 
                return



        def ping_everyone():
            yes_in = ["yes", "y", "Y", "Yes", "YES"]
            ping_everyone = input(f"{now_time()}~ Ping Everyone (y/n) ~ {purple}[ {end}> {purple}]  {end}")
            if ping_everyone in yes_in:
                ping_everyone = True
                return " @everyone"
            else: 
                ping_everyone = False
                return ""
            

        message = input(f"{now_time()}~ Spam Message ~ {purple}[ {end}> {purple}]  {end}")
        message = message +  ping_everyone()
        message_len = len(message)
        if message_len > 12:
            message_sensur = message[:12]
            message_sensur = message_sensur + "..."
        else:
            message_sensur = message

        Status_Change()
                
        def request():
            threads = []
            try:
                while True:
                    time.sleep(0.09)
                    t = threading.Thread(target=raid, args=(tokens, channels, message))
                    t.start()
                    threads.append(t)
            except:
                print("error")

            for thread in threads:
                thread.join()

        while True:
            request()
    except Exception as e:
        print(e)
