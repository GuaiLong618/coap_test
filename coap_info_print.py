#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import binascii
import struct
#from aiocoap.optiontypes import *
#from aiocoap.numbers.optionnumbers import OptionNumber
from aiocoap.options import *
from aiocoap import *


#str_data = b'60416802602A43414530303030313130D2F407D1'
str_data = '60416802602A43414530303030313130D2F407D1'
#str_data = '6041680660D2F607D1'

class coap_info_print(Options):

    def __init__(self, dat):
        self.dat = dat
        #扩展options 新增oneM2M TS 008 RSC
        OptionNumber.ONEM2M_RSC = OptionNumber(265)
        Options.onem2m_rsc = options._single_value_view(OptionNumber.ONEM2M_RSC)
        Options.onem2m_rsc = 265
        OptionNumber.ONEM2M_RSC.format = optiontypes.UintOption
        print(Options.onem2m_rsc)

        pass

    def info_print(self):
        """coap unpack print coap info vesion msgtype code msgid token remote opt payload"""
        bytes_data = bytes().fromhex(self.dat)

        print("rawdata:", self.dat)
        print("bytes:", bytes_data)
        hex_data = binascii.hexlify(bytes_data)
        print(hex_data)

        (vttkl, code, mid) = struct.unpack('!BBH', bytes_data[:4])
        print("vttkl:","%x"%vttkl)
        print("code:", "%x"%code)
        print("mid:", "%x"%mid)
        print("\r")

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
        print("payload:", msg.payload)
        print("\r")
        #parsed opt
        text = ", ".join("%s: %s" % (OptionNumber(k), " / ".join(map(str, v))) for (k, v) in msg.opt._options.items())
        print(text)

        list_data = list(msg.opt._options.items())
        print(list_data)
        #for tuples in list_data:
        #    print(tuples[0], struct.unpack('!H', tuples[1][0]))

        #hex_dat = list_data[0][1][0].value.hex()
        # opt_value = struct.unpack('!H', list_data[0][1][0].value)
        # print(opt_value)

        # OptionNumber.ONEM2M_RSC = OptionNumber(265)
        # options.onem2m_rsc = options._single_value_view(OptionNumber.ONEM2M_RSC)
        # options.onem2m_rsc = 265
        # OptionNumber.ONEM2M_RSC.format = optiontypes.UintOption
        # print(options.onem2m_rsc)

        # msg = Message.decode(bytes_data)
        # text = ", ".join("%s: %s" % (OptionNumber(k), " / ".join(map(str, v))) for (k, v) in msg.opt._options.items())
        # print(text)

        pass


    def info_encode(self):
        "coap pack"
        #msg = Message(mtype=ACK, mid=0x6802, code=CREATED, payload=b'5000')
        #msg_encode = Message.encode(msg)

        #print(msg)
        #print(msg_encode)

        #msg_decode_obj = Message.decode(msg_encode)
        #print(msg_decode_obj)
        pass

if __name__ == '__main__':
    info = coap_info_print(str_data)
    info.info_print()
    #info.info_encode()
    pass

















