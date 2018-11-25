#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" pySim: Dump APDU to disk
"""

from pySim.transport import LinkBase


class DiskLink(LinkBase):
    """ Transport module to simply dump APDUs to disk
    """

    def __init__(self, file_output='/tmp/apdu_dump', delimiter='\n'):
        """ Default dump to /tmp/apdu_dump, newline delimiter
        """
        self.file_path = file_output
        self.delimiter = delimiter

    def send_apdu_raw(self, pdu):
        """ Take raw APDUs and write them to disk. Return generic SW.
        """
        fd = open(self.file_path, "a+")
        fd.write(pdu)
        fd.write(self.delimiter)
        fd.close()
        return "0000000000000090000000", ["90", "00"]

    def send_apdu_checksw(self, pdu, sw="9000"):
        rv = self.send_apdu(pdu)
        return rv

