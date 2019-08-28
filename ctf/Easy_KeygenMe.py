#!/usr/bin/env python3

serial = b'\x5B\x13\x49\x77\x13\x5E\x7D\x13'
v6 = [16, 32, 48]
name = ''

idx = 0
for b in serial:
    name += chr(b ^ v6[idx % 3])
    idx += 1

print(name)