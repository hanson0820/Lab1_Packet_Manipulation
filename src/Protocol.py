#!/usr/bin/env python

from scapy.all import *

'''
Define your own protocol
'''
class Protocol(Packet):
    # Set the name of protocol
    name = 'Student'

    # Define the fields in protocol
    # [TODO] add the 2nd string field called 'id' with default value '0000000'
    fields_desc = [
        StrField('dept', 'cs', fmt = 'H', remain = 0),
        StrField('id', '0000000', fmt = 'H', remain = 0),
        # TODO here
    ]

'''
Add customized protocol into IP layer
'''
bind_layers(TCP, Protocol, frag = 0, proto = 99)
conf.stats_classic_protocols += [Protocol]
conf.stats_dot11_protocols += [Protocol]
