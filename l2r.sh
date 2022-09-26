
#!/bin/bash
# consumes from stdin and writes to stdout
# turn off line buffering: stdbuf -i0 -o0 -e0 command

#tee l2r | stdbuf -i0 -o0 -e0 xxd | tee l2r.hex | stdbuf -i0 -o0 -e0 xxd -r
#tee l2r | tee /dev/null | tee /dev/null
#tee l2r
#tee l2r | stdbuf -i0 -o0 -e0 hexdump -v -e '/1 "%02X\n"' | tee l2r.hex | stdbuf -i0 -o0 -e0 ./unhex.py
stdbuf -i0 -o0 -e0 hexdump -v -e '/1 "%02X\n"' | tee l2r.hex | stdbuf -i0 -o0 -e0 ./unhex.py
