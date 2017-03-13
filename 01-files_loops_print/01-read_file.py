#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Open the file
    with open("fixtures/ip_addresses.txt", "r") as file_handler:
        # Read the entire contents of the file into memory
        # NOTE / WARNING: doing this against a large file may crash the program
        # or the system as it will fill up the entire machine's available RAM.
        contents = file_handler.read()
        # Print the contents of the file to the screen
        print(contents)
