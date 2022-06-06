#! /usr/bin/env python3

import os

def showMenu():  
 print("""
1.MAC Changer
2.Network Manager       
3.ARP spoofer        
4.Lazagne      
5.Exit """)

def selection(op):
    if op == "1":
      interface = input("Interface to use:")
      mac = input("Input the new mac:")
      print("MAC changer")
      os.system("python3 mac_changer.py -i"+interface+" -m"+mac)

    elif op == "2": 
      exit()

print("----------------------")
print("Swiss-Messer ver.0.1")
print("Ctrl+c to Exit!")
print("----------------------")

while True:
    showMenu()
    option = input("Chose an option:")
    selection(option)
