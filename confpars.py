from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

print cisco_cfg

cryptomaps = cisco_cfg.find_objects(r"^crypto map CRYPTO")

for i in cryptomaps:
   print "Crypto match: ",i.text
   for child in i.children:
      print child.text

print "\n### Matching PFS group2 only\n";

cryptomaps = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"pfs group2")

for i in cryptomaps:
   print "Crypto match: ",i.text
   for child in i.children:
      print child.text

print "\n### Maps not use AES:\n";

trans_sets = cisco_cfg.find_objects(r"crypto ipsec transform-set(?!.*esp-aes)")

import re

for i in trans_sets:
   #print "Crypto match: ",i.text
   tmp_transform_set = re.search(r'transform-set (.*?) esp-', i.text);
   #print "Match: ",tmp_transform_set.group(1);
   cryptomaps = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=tmp_transform_set.group(1));
   for i in cryptomaps:
      print "Crypto match: ",i.text
      for child in i.children:
         print child.text


