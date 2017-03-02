#!/usr/bin/env python3

# To run:
# python3 01-reading_a_file.py
#
# Expected output:
# Path to desired file: fixtures/ip_addresses.txt
# set policy-options prefix-list 64510-customers 192.168.1.1/32
# set policy-options prefix-list 64510-customers 192.168.1.2/32
# set policy-options prefix-list 64510-customers 192.168.1.3/32
# set policy-options prefix-list 64510-customers 192.168.1.4/32
# set policy-options prefix-list 64510-customers 192.168.1.5/32
# set policy-options prefix-list 64510-customers 192.168.1.6/32
# set policy-options prefix-list 64510-customers 192.168.1.7/32
# set policy-options prefix-list 64510-customers 192.168.1.8/32
# set policy-options prefix-list 64510-customers 192.168.1.9/32
# set policy-options prefix-list 64510-customers 192.168.1.10/32

if __name__ == "__main__":
    prefix_list_tmpl = "set policy-options prefix-list 64510-customers {!s}/32"
    # We want to open the file in the directory ./fixtures/ip_addresses.txt
    path_to_desired_file = "fixtures/ip_addresses.txt"
    # Print out the path so that we can see it
    print("Path to desired file: {!s}".format(path_to_desired_file))

    # Open the file using the string representation of the path to the file
    # as the first argument.
    # In the second argument, we pass the mode with which to open the file.
    # In this example, we want to read the file. Because of this, we use "r"
    # for "Read Mode." Read mode is used when the file is only being read, not
    # written to or appended to.
    with open(path_to_desired_file, "r") as file_handler:
        # We want to walk through the file line by line because each line of
        # the file has a single IP address. A for loop allows us to go one
        # line at a time through the file.
        for line in file_handler:
            # We use the .strip("\n") method to remove the newlines at the end
            # of each line in the file. Without this, we'd end up printing
            # something like:
            # 192.168.1.1
            #
            # 192.168.1.2
            #
            # 192.168.1.3
            # ...
            ip_address = line.strip("\n")
            # Next, we insert the IP address into our template string
            prefix_list_statement = prefix_list_tmpl.format(ip_address)
            # And print this to the screen
            print(prefix_list_statement)
