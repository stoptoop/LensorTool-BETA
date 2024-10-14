import requests
from .config import *




def tokeninfo():
    try:
        token_discord=input(f"{now_time()}~ Insert Token ~ {purple}[ {end}> {purple}]  {end}")
        os.system('cls||clear')
        print(f"{now_time()}", colored_yellow(f"Token: {token_discord}"))
        print(f"{now_time()}", colored_yellow(f"Start Checking token"))
        try:
            api = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord}).json()

            response = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord, 'Content-Type': 'application/json'})

            if response.status_code == 200: status = "Valid"
            else: status = "Invalid"

            username_discord = api.get('username', "None") + '#' + api.get('discriminator', "None")
            display_name_discord = api.get('global_name', "None")
            user_id_discord = api.get('id', "None")
            email_discord = api.get('email', "None")
            email_verified_discord = api.get('verified', "None")
            phone_discord = api.get('phone', "None")
            mfa_discord = api.get('mfa_enabled', "None")
            country_discord = api.get('locale', "None")
            avatar_discord = api.get('avatar', "None")
            avatar_decoration_discord = api.get('avatar_decoration_data', "None")
            public_flags_discord = api.get('public_flags', "None")
            flags_discord = api.get('flags', "None")
            banner_discord = api.get('banner', "None")
            banner_color_discord = api.get('banner_color', "None")
            accent_color_discord = api.get("accent_color", "None")
            nsfw_discord = api.get('nsfw_allowed', "None")

            try: created_at_discord = datetime.fromtimestamp(((int(api.get('id', 'None')) >> 22) + 1420070400000) / 1000, timezone.utc)
            except: created_at_discord = "None"

            try:
                if api.get('premium_type', 'None') == 0:
                    nitro_discord = 'False'
                elif api.get('premium_type', 'None') == 1:
                    nitro_discord = 'Nitro Classic'
                elif api.get('premium_type', 'None') == 2:
                    nitro_discord = 'Nitro Boosts'
                elif api.get('premium_type', 'None') == 3:
                    nitro_discord = 'Nitro Basic'
                else:
                    nitro_discord = 'False'
            except:
                nitro_discord = "None"

            try: avatar_url_discord = f"https://cdn.discordapp.com/avatars/{user_id_discord}/{api['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{user_id_discord}/{api['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{user_id_discord}/{api['avatar']}.png"
            except: avatar_url_discord = "None"
            
            try:
                linked_users_discord = api.get('linked_users', 'None')
                linked_users_discord = ' / '.join(linked_users_discord)
                if not linked_users_discord.strip():
                    linked_users_discord = "None"
            except:
                linked_users_discord = "None"
            
            try:
                bio_discord = "\n" + api.get('bio', 'None')
                if not bio_discord.strip() or bio_discord.isspace():
                    bio_discord = "None"
            except:
                bio_discord = "None"
            
            try:
                authenticator_types_discord = api.get('authenticator_types', 'None')
                authenticator_types_discord = ' / '.join(authenticator_types_discord)
            except:
                authenticator_types_discord = "None"

            try:
                guilds_response = requests.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers={'Authorization': token_discord})
                if guilds_response.status_code == 200:
                    guilds = guilds_response.json()
                    try:
                        guild_count = len(guilds)
                    except:
                        guild_count = "None"
                    try:
                        owner_guilds = [guild for guild in guilds if guild['owner']]
                        owner_guild_count = f"({len(owner_guilds)})"
                        owner_guilds_names = [] 
                        if owner_guilds:
                            for guild in owner_guilds:
                                owner_guilds_names.append(f"{guild['name']} ({guild['id']})")
                            owner_guilds_names = "\n" + "\n".join(owner_guilds_names)
                    except:
                        owner_guild_count = "None"
                        owner_guilds_names = "None" 
            except:
                owner_guild_count = "None"
                guild_count = "None"
                owner_guilds_names = "None"


            try:
                billing_discord = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token_discord}).json()
                if billing_discord:
                    payment_methods_discord = []

                    for method in billing_discord:
                        if method['type'] == 1:
                            payment_methods_discord.append('CB')
                        elif method['type'] == 2:
                            payment_methods_discord.append("Paypal")
                        else:
                            payment_methods_discord.append('Other')
                    payment_methods_discord = ' / '.join(payment_methods_discord)
                else:
                    payment_methods_discord = "None"
            except:
                payment_methods_discord = "None"
            
            try:
                friends = requests.get('https://discord.com/api/v8/users/@me/relationships', headers={'Authorization': token_discord}).json()
                if friends:
                    friends_discord = []
                    for friend in friends:
                        unprefered_flags = [64, 128, 256, 1048704]
                        data = f"{friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})"

                        if len('\n'.join(friends_discord)) + len(data) >= 1024:
                            break

                        friends_discord.append(data)

                    if len(friends_discord) > 0:
                        friends_discord = '\n' + ' / '.join(friends_discord)
                    else:
                        friends_discord = "None"
                else:
                    friends_discord = "None"
            except:
                friends_discord = "None"

            try:
                gift_codes = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': token_discord}).json()
                if gift_codes:
                    codes = []
                    for gift_codes_discord in gift_codes:
                        name = gift_codes_discord['promotion']['outbound_title']
                        gift_codes_discord = gift_codes_discord['code']
                        data = f"Gift: {name}\nCode: {gift_codes_discord}"
                        if len('\n\n'.join(gift_codes_discord)) + len(data) >= 1024:
                            break
                        gift_codes_discord.append(data)
                    if len(gift_codes_discord) > 0:
                        gift_codes_discord = '\n\n'.join(gift_codes_discord)
                    else:
                        gift_codes_discord = "None"
                else:
                    gift_codes_discord = "None"
            except:
                gift_codes_discord = "None"

        except Exception as e:
            print(f"erorr b1")

        Slow(f"""
    {now_time()} Status       : {purple}[{end} {status} {purple}] {end}
    {now_time()} Token        : {purple}[{end} {token_discord} {purple}] {end}
    {now_time()} Username     : {purple}[{end} {username_discord} {purple}] {end}
    {now_time()} Display Name : {purple}[{end} {display_name_discord} {purple}] {end}
    {now_time()} Id           : {purple}[{end} {user_id_discord} {purple}] {end}
    {now_time()} Created      : {purple}[{end} {created_at_discord} {purple}] {end}
    {now_time()} Email        : {purple}[{end} {email_discord} {purple}] {end}
    {now_time()} Verified     : {purple}[{end} {email_verified_discord} {purple}] {end}
    {now_time()} Phone        : {purple}[{end} {phone_discord} {purple}] {end}
    {now_time()} Nitro        : {purple}[{end} {nitro_discord} {purple}] {end}
    {now_time()} Linked Users : {purple}[{end} {linked_users_discord} {purple}] {end}
    {now_time()} Avatar Decor : {purple}[{end} {avatar_decoration_discord} {purple}] {end}
    {now_time()} Avatar       : {purple}[{end} {avatar_discord} {purple}] {end}
    {now_time()} Avatar URL   : {purple}[{end} {avatar_url_discord} {purple}] {end}
    {now_time()} Accent Color : {purple}[{end} {accent_color_discord} {purple}] {end}
    {now_time()} Banner       : {purple}[{end} {banner_discord} {purple}] {end}
    {now_time()} Banner Color : {purple}[{end} {banner_color_discord} {purple}] {end}
    {now_time()} Flags        : {purple}[{end} {flags_discord} {purple}] {end}
    {now_time()} Public Flags : {purple}[{end} {public_flags_discord} {purple}] {end}
    {now_time()} NSFW         : {purple}[{end} {nsfw_discord} {purple}] {end}
    {now_time()} Multi-Factor Authentication : {purple}[{end} {mfa_discord} {purple}] {end}
    {now_time()} Authenticator Type          : {purple}[{end} {authenticator_types_discord} {purple}] {end}
    {now_time()} Billing      : {purple}[{end} {payment_methods_discord} {purple}] {end}
    {now_time()} Gift Code    : {purple}[{end} {gift_codes_discord} {purple}] {end}
    {now_time()} Guilds       : {purple}[{end} {guild_count} {purple}] {end}
    {now_time()} Owner Guilds : {purple}[{end} {owner_guild_count}{owner_guilds_names} {purple}] {end}
    {now_time()} Bio          : {purple}[{end} {bio_discord} {purple}] {end}
    {now_time()} Friends       : {purple}[{end} {friends_discord} {purple}] {end}
        """)
        print(f"{purple}>>>{end}  to exit print  15")
        main()
    except Exception as e:
        print(f"error b2 {e}")

tokeninfo()