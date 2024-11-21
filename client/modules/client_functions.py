import socket
import tqdm
import os
import time
import sys
import ipaddress
import tkinter as tk
from tkinter.filedialog import askopenfilename
from modules import client_functions as cf

def menu():

    menu_loop = True

    while menu_loop:

        print("[1] Connect to a server.")
        print("[2] Settings.")
        print("[3] Quit.")
    
        menu_selection = input("Please enter a number to select an option. \n")

        if menu_selection == "1":
            menu_loop = False
            os.system("cls")
            connect()
        elif menu_selection == "2":
            menu_loop = False
            os.system("cls")
            settings()
        elif menu_selection == "3":
            sys.exit()
        else:
            os.system("cls")
            print("[!] Input not recognized. Please try again.")

def connect():
    
    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 4096
    host = "192.168.0.63"
    port = 5001
    s = socket.socket()

    ip_input_loop = True

    while ip_input_loop:

        host = input("Please enter the IP address of the server you would like to connect to: \n")

        if is_valid_ip(host):
            ip_input_loop = False
            os.system("cls")
            print(f"{host} is a valid IP address.")
        else:
            os.system("cls")
            print(f"{host} is not a valid IP address. Please try again. \n")

    print(f"[+] Connecting to {host}:{port}")

    s.connect((host, port))

    print("[+] Connected.")

def connected_menu():

    tk.Tk().withdraw()
    fn = askopenfilename()
    print("user chose", fn)

    menu_loop = True

    while menu_loop:

        print("[1] Select a file.")
        print("[2] Transfer selected file to the server.")
        print("[3] Quit.")
    
        menu_selection = input("Please enter a number to select an option. \n")

def settings():

    pass

def is_valid_ip(ip_str):

    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False