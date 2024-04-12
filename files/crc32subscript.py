# Subscript meant to be used with a "input" variable
from binascii import crc32

vr("output", hex(crc32(vr("input")))[2:])
vrd("input")
del crc32
