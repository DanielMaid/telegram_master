#!/bin/env python3
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UsernameInvalidError
import configparser
import os, sys
import csv
import random
import time

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

random_time = [30, 31, 32, 33, 34, 35]
SLEEP_TIME = random.choice(random_time)

class main():


    def banner():
        
        print(f"""
    {re}╔╦╗{cy}┌─┐┬  ┌─┐{re}╔═╗  ╔═╗{cy}┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
    {re} ║ {cy}├┤ │  ├┤ {re}║ ╦  ╚═╗{cy}│  ├┬┘├─┤├─┘├┤ ├┬┘
    {re} ╩ {cy}└─┘┴─┘└─┘{re}╚═╝  ╚═╝{cy}└─┘┴└─┴ ┴┴  └─┘┴└─

            """)

    def send_sms():
        try:
            cpass = configparser.RawConfigParser()
            cpass.read('config.data')
            api_id = cpass['cred']['id']
            api_hash = cpass['cred']['hash']
            phone = cpass['cred']['phone']
            api_id2 = cpass['ban']['id']
            api_hash2 = cpass['ban']['hash']
            phone2 = cpass['ban']['phone']
            api_id3 = cpass['qaqa']['id']
            api_hash3 = cpass['qaqa']['hash']
            phone3 = cpass['qaqa']['phone']
        except KeyError:
            os.system('clear')
            main.banner()
            print(re+"[!] run python3 setup.py first !!\n")
            sys.exit(1)


        client = TelegramClient(phone, api_id, api_hash)
        client1 = TelegramClient(phone, api_id, api_hash)
        client2 = TelegramClient(phone2,api_id2, api_hash2)
        client3 = TelegramClient(phone3,api_id3, api_hash3)

        print(phone,phone2,phone3)
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            os.system('clear')
            main.banner()
            client.sign_in(phone, input(gr+'[+] Enter the code: '+re))




        os.system('clear')
        main.banner()
        input_file = sys.argv[1]
        users = []
        with open(input_file, encoding='UTF-8') as f:
            rows = csv.reader(f,delimiter=",",lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {}
                user['username'] = row[0]
                user['id'] = int(row[1])
                user['access_hash'] = int(row[2])
                user['name'] = row[3]
                users.append(user)
        print(gr+"[1] send sms by user ID\n[2] send sms by username ")
        mode = int(input(gr+"Input : "+re))
         
        #message = input(gr+"[+] Enter Your Message : "+re)
        message = "Hello, I have seen you in 3 commas group! I also use 3 com for make auto trading, much better if u create a long  bot with a coin that will go up. So I created a group where I send a lot of graphics from Trading view, you can use this signals for manual and automation(bot) trading. My signals always free, just subscribe and enjoy! Wish you a good profit!  https://t.me/cryptotradetop"
        #message = ["Hi", "Hello", "Hey"]

        count = 2
        for user in users[556:len(users)]:
            time.sleep(2)
            if mode == 2:
                if user['username'] == "":
                    continue
                receiver = client.get_input_entity(user['username'])
            elif mode == 1:
                receiver = InputPeerUser(user['id'],user['access_hash'])
            else:
                print(re+"[!] Invalid Mode. Exiting.")
                client.disconnect()
                sys.exit()
            try:
                if count % 10 == 0:
                    print("[+] Sleeping 123 seconds.\n")
                    time.sleep(123)
                messagenew = message+" "+str(random.randint(1, 123))
                print(gr+"[+] Sending Message to:", user['name'])
                client.send_message(receiver, messagenew.format(user['name']))
                print(gr+"[+] Waiting {} seconds".format(random.choice(random_time)))
                time.sleep(random.choice(random_time))
                count += 1
                print("[+] Number of sent messages ",count)
            except PeerFloodError:
                print(re+"[!] Getting Flood Error from telegram. \n[!] Script is stopping now. \n[!] Please try again after some time.")
                #client.disconnect()
                print("[+] Changing user....")
                if client == client3:
                    print("[+] Users are over = (")
                    client.disconnect()
                    sys.exit()
                elif client == client2:
                    print("[+] Changing for client3")
                    client = client3
                    client.connect()
                    if not client.is_user_authorized():
                        client.send_code_request(phone3)
                        main.banner()
                        client.sign_in(phone3, input(gr + '[+] Enter the code: ' + re))
                    #receiver = client.get_input_entity(user['username'])
                elif client == client1:
                    print("[+] Changing for client2")
                    client = client2
                    client.connect()
                    if not client.is_user_authorized():
                        client.send_code_request(phone2)
                        main.banner()
                        client.sign_in(phone2, input(gr + '[+] Enter the code: ' + re))
                    #receiver = client.get_input_entity(user['username'])
            except Exception as e:
                print(re+"[!] Error:", e)
                print(re+"[!] Trying to continue...")
                time.sleep(2)
                continue
        client.disconnect()
        print("Done. Message sent to all users.")





main.send_sms()
