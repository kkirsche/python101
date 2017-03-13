#!/usr/bin/env python3
# -*- coding: utf-8 -*-

prefix_list_tmpl = "set policy-options prefix-list 64510-customers {ip}/32"

if __name__ == "__main__":
    ip_address = "192.168.1.1"
    full_string = prefix_list_tmpl.format(ip=ip_address)
    print(full_string)
