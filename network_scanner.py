#! /usr/bin/env python

import scapy.all as scapy
import argparse

def scan(ip):

    # Ask who has the ip
    arp_request = scapy.ARP(pdst = ip)

    # Destination mac to the broadcast mac
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")

    # New packet by appending with foward slash
    arp_request_broadcast = broadcast/arp_request

    # stand-recive-custom(ether)
    # send packet and recive response"

    ans_list = scapy.srp(arp_request_broadcast, timeout = 1,verbose = False)[0]

    clients_list = []

    for element in ans_list:

        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}

        clients_list.append(client_dict)

    return clients_list

def print_result(result_list):
    print(" IP\t\t\tMAC aAddress\n---------------------------------------------")
    for client in result_list :
        print(client["ip"]+"\t\t"+client["mac"])

def get_ip_range():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r","--range", dest="range", help="Specify the ip range for the scan")
    options = parser.parse_args()

   # if not range.range:
      #  range.error("[-] Please specify the range,for help use --help")

    return options

options = get_ip_range()

scan_result = scan(options.range)

print_result(scan_result)


# arp_request_broadcast.show()

# print(broadcast.summary())

# scapy.ls(scapy.Ether) #info about fields

# print(arp_request.summary())
