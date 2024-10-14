import requests
from .config import *





def serverinfo():
	try:
		invite=input(f"{now_time()}~ Server Invitation ~ {purple}[ {end}> {purple}]  {end}")
		os.system('cls||clear')
		try:
			invite_code = invite.split("/")[-1]
		except:
			invite_code = invite

		response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")

		if response.status_code == 200:
			api = response.json()

			type_value = api.get('type', "None")
			code_value = api.get('code', "None")
			inviter_info = api.get('inviter', {})
			inviter_id = inviter_info.get('id', "None")
			inviter_username = inviter_info.get('username', "None")
			inviter_avatar = inviter_info.get('avatar', "None")
			inviter_discriminator = inviter_info.get('discriminator', "None")
			inviter_public_flags = inviter_info.get('public_flags', "None")
			inviter_flags = inviter_info.get('flags', "None")
			inviter_banner = inviter_info.get('banner', "None")
			inviter_accent_color = inviter_info.get('accent_color', "None")
			inviter_global_name = inviter_info.get('global_name', "None")
			inviter_banner_color = inviter_info.get('banner_color', "None")
			expires_at = api.get('expires_at', "None")
			flags = api.get('flags', "None")
			server_info = api.get('guild', {})
			server_id = server_info.get('id', "None")
			server_name = server_info.get('name', "None")
			server_icon = server_info.get('icon', "None")
			server_features = server_info.get('features', "None")
			if server_features != "None":
				server_features = ' / '.join(server_features)
			server_verification_level = server_info.get('verification_level', "None")
			server_nsfw_level = server_info.get('nsfw_level', "None")
			server_descritpion = server_info.get('description', "None")
			server_nsfw = server_info.get('nsfw', "None")
			server_premium_subscription_count = server_info.get('premium_subscription_count', "None")
			channel_info = api.get('channel', {})
			channel_id = channel_info.get('id', "None")
			channel_type = channel_info.get('type', "None")
			channel_name = channel_info.get('name', "None")
		else:
			print("ERROR")

		Slow(f"""
{colored_green(f"Invitation Information:")}
{now_time()} Invitation         : {purple}[{end} {invite} {purple}] {end}
{now_time()} Type               : {purple}[{end} {type_value} {purple}] {end}
{now_time()} Code               : {purple}[{end} {code_value} {purple}] {end}
{now_time()} Expired            : {purple}[{end} {expires_at} {purple}] {end}
{now_time()} Server ID          : {purple}[{end} {server_id} {purple}] {end}
{now_time()} Server Name        : {purple}[{end} {server_name} {purple}] {end}
{now_time()} Channel ID         : {purple}[{end} {channel_id} {purple}] {end}
{now_time()} Channel Name       : {purple}[{end} {channel_name} {purple}] {end}
{now_time()} Channel Type       : {purple}[{end} {channel_type} {purple}] {end}
{now_time()} Server Description : {purple}[{end} {server_descritpion} {purple}] {end}
{now_time()} Server Icon        : {purple}[{end} {server_icon} {purple}] {end}
{now_time()} Server Features    : {purple}[{end} {server_features} {purple}] {end}
{now_time()} Server NSFW Level  : {purple}[{end} {server_nsfw_level} {purple}] {end}
{now_time()} Server NSFW        : {purple}[{end} {server_nsfw} {purple}] {end}
{now_time()} Flags              : {purple}[{end} {flags} {purple}] {end}
{now_time()} Server Verification Level         : {purple}[{end} {server_verification_level} {purple}] {end}
{now_time()} Server Premium Subscription Count : {purple}[{end} {server_premium_subscription_count} {purple}] {end}
	""")

		if inviter_info:
			Slow(f"""    
{colored_green(f"Inviter Information:")}
{now_time()} ID            : {purple}[{end} {inviter_id} {purple}] {end}
{now_time()} Username      : {purple}[{end} {inviter_username} {purple}] {end}
{now_time()} Global Name   : {purple}[{end} {inviter_global_name} {purple}] {end}
{now_time()} Discriminator : {purple}[{end} {inviter_discriminator} {purple}] {end}
{now_time()} Public Flags  : {purple}[{end} {inviter_public_flags} {purple}] {end}
{now_time()} Banner        : {purple}[{end} {inviter_banner} {purple}] {end}
{now_time()} Accent Color  : {purple}[{end} {inviter_accent_color} {purple}] {end}
{now_time()} Banner Color  : {purple}[{end} {inviter_banner_color} {purple}] {end}
{now_time()} Avatar        : {purple}[{end} {inviter_avatar} {purple}] {end}
		""")
		print(f"{purple}>>>{end}  to exit print  15")
		main()
	except Exception as e:
		print(e)


