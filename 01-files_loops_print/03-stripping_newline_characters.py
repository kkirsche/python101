#!/usr/bin/env python3

if __name__ == "__main__":
    with open("fixtures/ip_addresses.txt", "r") as file_handler:
        for line in file_handler:
            no_newline = line.strip("\n")
            print(no_newline)
