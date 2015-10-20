#!/usr/bin/env python

import pysnmp
import snmp_helper

def main():
   ipaddr = '50.76.53.27'

   for i in (7961, 8061):
      print i,":\n";
      print "name     >>> ",snmp_helper.snmp_extract(snmp_helper.snmp_get_oid([ipaddr, "galileo", i], '.1.3.6.1.2.1.1.5.0'))
      print "sysdescr >>> ",snmp_helper.snmp_extract(snmp_helper.snmp_get_oid([ipaddr, "galileo", i], '.1.3.6.1.2.1.1.1.0'))
   

if __name__ == "__main__":
   main()
