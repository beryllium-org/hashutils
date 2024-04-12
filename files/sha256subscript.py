# Subscript meant to be used with a "input" variable
from adafruit_hashlib import sha256

vr("a", sha256())
vr("a").update(vr("input"))
vr("output", vr("a").hexdigest())
vrd("a")
vrd("input")
del (
    sha512,
    modules["adafruit_hashlib"],
    modules["adafruit_hashlib._sha512"],
    modules["adafruit_hashlib._sha1"],
    modules["adafruit_hashlib._sha256"],
    modules["adafruit_hashlib._md5"],
)
