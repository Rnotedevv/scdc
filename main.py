import time
import os
import requests
from colorama import Fore

# Header information
print("=================================================")
author = "RipNote"
print("Author: " + author)
script = "AUTO SEND"
print("Script: " + script)
discord = "http://discord.com/ripnoteee"
print("Discord: " + discord)
print("===========================================")
print('Enjoy the script!')
print("===========================================\n")

time.sleep(1)

# User inputs
channel_id = input("Masukkan ID channel: ")
waktu2 = int(input("Set Waktu Kirim Pesan (dalam detik): "))

# Countdown before starting
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

# Clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Load authorization token
if os.path.exists("token.txt"):
    with open("token.txt", "r") as f:
        authorization = f.readline().strip()
else:
    print(Fore.RED + "token.txt file not found.")
    exit()

# Read all messages from pesan.txt
if os.path.exists("pesan.txt"):
    with open("pesan.txt", "r") as f:
        messages = f.readlines()
else:
    print(Fore.RED + "pesan.txt file not found.")
    exit()

# Combine all lines into one single message (join with newlines)
combined_message = "\n".join([line.strip() for line in messages])

# Auto-loop to send the combined message continuously
while True:
    payload = {
        'content': combined_message  # All lines combined into one message
    }

    headers = {
        'Authorization': authorization,
        'Content-Type': 'application/json'
    }

    # Send message to Discord
    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", json=payload, headers=headers)

    # Check if the message was successfully sent
    if r.status_code == 201:
        print(Fore.WHITE + "Pesan sukses terkirim!")
    else:
        print(Fore.RED + f"Failed to send message. Status code: {r.status_code}")
        print(Fore.RED + f"Response body: {r.text}")

    # Delay before sending the message again
    time.sleep(waktu2)
