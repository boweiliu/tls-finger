
#!/bin/bash
# consumes from stdin and writes to stdout

tee l2r | xxd | tee l2r.hex | xxd -r
