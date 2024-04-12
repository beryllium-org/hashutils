be.based.run("mkdir /lib/adafruit_hashlib")
for pv[get_pid()]["f"] in [
    "__init__.mpy",
    "_md5.mpy",
    "_sha1.mpy",
    "_sha224.mpy",
    "_sha256.mpy",
    "_sha384.mpy",
    "_sha512.mpy",
]:
    be.based.run("cp " + vr("f") + " /lib/adafruit_hashlib/" + vr("f"))

for pv[get_pid()]["f"] in [
    "crc32.lja",
    "md5sum.lja",
    "sha1sum.lja",
    "sha224sum.lja",
    "sha256sum.lja",
    "sha384sum.lja",
    "sha512sum.lja",
]:
    be.based.run("cp " + vr("f") + " /bin/" + vr("f"))

be.based.run("mkdir /bin/hashutils")
for pv[get_pid()]["f"] in [
    "crc32.py",
    "md5sum.py",
    "sha1sum.py",
    "sha224sum.py",
    "sha256sum.py",
    "sha384sum.py",
    "sha512sum.py",
    "sha512subscript.py",
]:
    be.based.run("cp " + vr("f") + " /bin/hashutils/" + vr("f"))
be.api.setvar("return", "0")
