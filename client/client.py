import socket
import tqdm
import os
import time
import sys
import ipaddress
import tkinter as tk
from tkinter.filedialog import askopenfilename
from modules import client_functions as cf

print("[+] Client started.")
time.sleep(2)
os.system("cls")

"""
tk.Tk().withdraw()
fn = askopenfilename()
print("user chose", fn)

time.sleep(2)
"""

cf.menu()

"""
# the name of file we want to send, make sure it exists
filename = os.path.join(os.path.dirname(__file__), "test.txt")
# get the file size
filesize = os.path.getsize(filename)

# send the filename and filesize
s.send(f"{filename}{SEPARATOR}{filesize}".encode())

# start sending the file
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break
        # we use sendall to assure transimission in 
        # busy networks
        s.sendall(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))
# close the socket
s.close()

user_input = input("\nPlease enter q to quit")
if user_input == "q":
    quit()
"""