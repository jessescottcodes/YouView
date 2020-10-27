import os
import time
import sys
import random
import socket
import string
import webbrowser

print("Welcome to YouView | v1.0.0")
print("Created by Jesse Scott")
print()
url = input("URL: ")

running = True
while running:
    webbrowser.open(url)
    time.sleep(4)