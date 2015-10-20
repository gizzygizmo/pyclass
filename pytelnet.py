#!/usr/bin/env python

import time
import telnetlib
TELNET_PORT = 23
TELNET_TIMEOUT = 6

import socket
import sys

def cmd(remote_conn, cmd):
   cmd = cmd.rstrip() # strip off whitespace
   remote_conn.write(cmd+"\n")
   time.sleep(1)
   return remote_conn.read_very_eager()

def tlogin(remote_conn, username, password):
   result = remote_conn.read_until("rname:", TELNET_TIMEOUT)
   remote_conn.write(username + '\n')
   result += remote_conn.read_until("assword:", TELNET_TIMEOUT)
   remote_conn.write(password + '\n')
   time.sleep(1)
   cmd(remote_conn, "term len 0")

def telnet_connect(ipaddr):
   try:
      return telnetlib.Telnet(ipaddr, TELNET_PORT, TELNET_TIMEOUT)
   except socket.timeout:
      sys.exit("Unable to form connection to "+ipaddr)

def main():
   username = 'pyclass';
   password = '88newclass'
   ipaddr = '50.76.53.27'

   remote_conn = telnet_connect(ipaddr); 
   tlogin(remote_conn, username, password)
   
   print  cmd(remote_conn, "show ip int br")

   remote_conn.close

# test
if __name__ == "__main__":
   main()
