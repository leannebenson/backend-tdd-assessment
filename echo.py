#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "LeanneBenson"


import sys
import argparse

def create_parser():
    parser = argparse.ArgumentParser(
        description="Echo and Transform a message")
    parser.add_argument('msg', help="Message to display.")
    parser.add_argument('-u', "--upper", action='store_true',
                        help="Transfors the message to Uppercase.")
    parser.add_argument('-l', '--lower',  action='store_true',
                        help="Transforms the message to lowercase.")
    parser.add_argument('-t', '--title', action='store_true',
                        help="Transforms the message to Title Case.")
    return parser
    
def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args()
    msg = ns.msg
    if ns.upper:
        msg = msg.upper()
    if ns.lower:
        msg = msg.lower()
    if ns.title:
        msg = msg.title()
    print(msg)


if __name__ == '__main__':
    main(sys.argv[1:])
