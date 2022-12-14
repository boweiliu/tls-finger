#!/usr/bin/env python3
#input: lines of hex codes, 2 ch per line
#output: edit the nth hex character

"""
eg
00000000: 1603 0102 0001 0001 fc03 03f4 8ed8 de28  ...............(
00000010: 0ff0 f95a 9bc9 e228 dd94 1a8b cc11 876d  ...Z...(.......m
00000020: b215 2861 121d fd04 bc51 1620 0def 3a2a  ..(a.....Q. ..:*
00000030: e194 e032 18d3 4ff2 f1ea 2d28 81ae cebb  ...2..O...-(....
00000040: 693d 429f c45c f003 0e16 cfd4 003e 1302  i=B..\.......>..
00000050: 1303 1301 c02c c030 009f cca9 cca8 ccaa  .....,.0........
00000060: c02b c02f 009e c024 c028 006b c023 c027  .+./...$.(.k.#.'
00000070: 0067 c00a c014 0039 c009 c013 0033 009d  .g.....9.....3..
00000080: 009c 003d 003c 0035 002f 00ff 0100 0175  ...=.<.5./.....u
00000090: 0000 000e 000c 0000 096c 6f63 616c 686f  .........localho
000000a0: 7374 000b 0004 0300 0102 000a 0016 0014  st..............
000000b0: 001d 0017 001e 0019 0018 0100 0101 0102  ................
000000c0: 0103 0104 3374 0000 0010 000e 000c 0268  ....3t.........h
000000d0: 3208 6874 7470 2f31 2e31 0016 0000 0017  2.http/1.1......
"""

with open('/dev/stdout', 'w') as g:
    with open('/dev/stdin') as f:
        for idx, line in enumerate(f):
            out = line # swap 0x86 and 0x88, 0035 and 002f
            if idx == 135:
                assert(line[0:2] == '35')
                out = '2F\n'
            if idx == 137:
                assert(line[0:2] == '2F')
                out = '35\n'
            g.write(out)
            g.flush()
