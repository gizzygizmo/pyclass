from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

print cisco_cfg

cryptomaps = cisco_cfg.find_objects(r"^crypto map CRYPTO")

for i in cryptomaps:
   print "Crypto match: ",i.text
   for child in i.children:
      print child.text

print "\nMatching PFS group2 only\n";

cryptomaps = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"pfs group2")

for i in cryptomaps:
   print "Crypto match: ",i.text
   for child in i.children:
      print child.text
   

