#!/usr/bin/env python3

if __name__ == "__main__":
    with open("fixtures/ip_addresses.txt", "r") as file_handler:
        contents = file_handler.read()
        print(contents)
