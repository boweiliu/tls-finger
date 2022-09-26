#!/bin/bash
# source: https://fossies.org/linux/socat/EXAMPLES
#  40 // this is a cool trick, proposed by Christophe Lohr, to dump communications to
#  41 // two files; it would also work for other manipulations (recode, compress...)
#  42 // and it might also work with netcat ;-)
#  43 $ socat TCP-LISTEN:5555 SYSTEM:'tee l2r | socat - "TCP:remote:5555"  | tee r2l' 

socat TCP-LISTEN:9090,reuseaddr,fork SYSTEM:'./l2r.sh | socat - "TCP:www.google.com:443"  | tee r2l'
