#!/usr/bin/env python

import telnetlib
TELNET_PORT = 23
TELNET_TIMEOUT = 6

def main():
   username = 'pyclass';
   password = '88newclass'
   ipaddr = '50.76.53.27'

   remote_conn = telnetlib.Telnet(ipaddr, TELNET_PORT, TELNET_TIMEOUT)

   remote_conn.close



if __name__ == "__main__":
   main()
