from .config import *
import requests



def Joiner():
    try:
        def joiner(token, invite):
            invite_code = invite.split("/")[-1]

            try:
                response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")
                if response.status_code == 200:
                    server_name = response.json().get('guild', {}).get('name')
                else:
                    server_name = invite
            except:
                server_name = invite

            try:
                response = requests.post(f"https://discord.com/api/v9/invites/{invite_code}", headers={'Authorization': token})
                    
                if response.status_code == 200:
                    print(colored_green(f"Status: Joined Server: {server_name}"))
                elif response.status_code == 400:
                    print(colored_red_purple(f"Status: Error Captcha Not Solved  Server: {server_name}"))
                else:
                    print(colored_red_purple(f"Status: Error {response.status_code}  Server: {server_name}"))
            except Exception as e:
                print(colored_red_purple(f"Status: Error Server: {server_name}"))

        token = Choice1TokenDiscord()
        invite = input(f"{now_time()}~ Server Invitation ~ {purple}[ {end}> {purple}]  {end}")
        joiner(token, invite)
        print(f"{purple}>>>{end}  to exit print  15")
        main()
    except Exception as e:
        print(e)
