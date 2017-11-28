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
#str_data = '60416802602A43414530303030313130D2F407D1'
bin_data = "440201D7D701100FB2726411283D0565703D38363531393930333030323036\
333403623D55066C743D333030DD2302383635313939303330303230363334FF3C2F3E3B72\
743D226F6D612E6C776D326D222C3C2F333230302F303E"

data0 = '60410000602A43414530303030313636D2F407D1'
data1 = '6041000960D2F607D1'

zte_con_data = '6041000960D2F607D1'  



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
        print("\r")
        print("bytes:", bytes_data)
        print("\r")
        hex_data = binascii.hexlify(bytes_data)
        print(hex_data)
        print("\r")

        (vttkl, code, mid) = struct.unpack('!BBH', bytes_data[:4])
        print("vttkl:","0x%x"%vttkl)
        print("code:", "0x%x"%code)
        print("mid:", "0x%x"%mid)
        print("\r")

        msg = Message.decode(bytes_data)
        print(msg)

        print("version:", msg.version)
        print("msg type:", msg.mtype)
        print("code:", msg.code)
        token_length = (vttkl & 0x0F)
        print("TKL:", token_length)
        print("msg ID:", msg.mid)
        print("token:", msg.token)
        print("opt:", msg.opt)
        print("\r")
        #parsed opt
        text = ", ".join("%s: %s \r\n " % (OptionNumber(k), " / ".join(map(str, v))) for (k, v) in msg.opt._options.items())
        print(text)
        print("\r")
        print("remote:", msg.remote)
        print("\r")
        print("payload:", msg.payload)
        print("\r")
        
        #list_data = list(msg.opt._options.items())
        #print(list_data)

        #for i in range(len(list_data)):
        #    print (list_data[i])
        
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
    #info = coap_info_print(data0)
    #info.info_print()

    #print('-----------------------')
    #info = coap_info_print(data1)
    #info.info_print()

    
    print('-----------------------')
    info = coap_info_print(zte_con_data)
    info.info_print()
    
    #info.info_encode()
    pass
















