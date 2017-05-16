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

#
hex_data = bytes().fromhex(str_data)

print(str_data)
print(hex_data)
h_data = binascii.hexlify(hex_data)
print(h_data)

(vttkl, code, mid) = struct.unpack('!BBH', hex_data[:4])
print("%x"%vttkl)
print("%x"%code)
print("%x"%mid)

msg = Message.decode(hex_data)
print(msg)

msg = Message(mtype=ACK, mid=0x6802, code=CREATED, payload=b'5000')
msg_encode = Message.encode(msg)

#print(msg)
#print(msg_encode)

msg_decode_obj = Message.decode(msg_encode)
#print(msg_decode_obj)

