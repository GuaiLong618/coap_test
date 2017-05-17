#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import binascii
import struct
from aiocoap import *

#str_data = b'60416802602A43414530303030313130D2F407D1'
#str_data = '60416802602A43414530303030313130D2F407D1'
str_data = '6041680660D2F607D1'

def info_print():
    """coap unpack print coap info vesion msgtype code msgid token remote opt payload"""
    bytes_data = bytes().fromhex(str_data)

    print("rawdata:", str_data)
    print("bytes:", bytes_data)
    hex_data = binascii.hexlify(bytes_data)
    print(hex_data)

    (vttkl, code, mid) = struct.unpack('!BBH', bytes_data[:4])
    print("vttkl:","%x"%vttkl)
    print("code:", "%x"%code)
    print("mid:", "%x"%mid)

    msg = Message.decode(bytes_data)
    print(msg)

    print("version:", msg.version)
    print("msg type:", msg.mtype)
    token_length = (vttkl & 0x0F)
    print("TKL:", token_length)
    print("msg ID:", msg.mid)
    print("token:", msg.token)
    print("opt:", msg.opt)
    print("remote:", msg.remote)
    #parsed opt
    msg.opt.decode(bytes_data[4 : 4 + token_length])
    #msg.opt._options.items()


def info_encode():
    "coap pack"
    msg = Message(mtype=ACK, mid=0x6802, code=CREATED, payload=b'5000')
    msg_encode = Message.encode(msg)

    #print(msg)
    #print(msg_encode)

    msg_decode_obj = Message.decode(msg_encode)
    #print(msg_decode_obj)

if __name__ == '__main__':
    info_print()


















