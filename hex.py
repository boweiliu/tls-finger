#!/usr/bin/env python3
# usage: socat -x -lu tcp-listen:9090,reuseaddr,fork tcp:www.google.com:443 2>&1 | tee /tmp/socat | ./hex.py | xxd | vi -R - 
out=''
with open('/dev/stdin') as f:
    for line in f:
        if line[0] == '>' or line[0] == '<':
            continue
        for s in line.split(' '):
            if s == '':
                continue
            out += chr(int('0x' + s, 0))
with open('/dev/stdout', 'w') as g:
    g.write(out)