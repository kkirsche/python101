#!/usr/bin/env python3

if __name__ == "__main__":
    prefix_list_tmpl = "set policy-options prefix-list 64510-customers {!s}/32"
    with open("fixtures/ip_addresses.txt", "r") as file_handler:
        for line in file_handler:
            ip_address = line.strip("\n")
            full_string = prefix_list_tmpl.format(ip_address)
            print(full_string)
