#!/usr/bin/env python3
# -*- coding: utf-8 -*-

prefix_list_tmpl = "set policy-options prefix-list 64510-customers {ip}/32"

if __name__ == "__main__":
    with open("fixtures/ip_addresses.txt", "r") as file_handler:
        for line in file_handler:
            ip_address = line.strip()
            full_string = prefix_list_tmpl.format(ip=ip_address)
            print(full_string)
