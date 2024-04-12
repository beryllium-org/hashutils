be.based.run(
    "rm /lib/adafruit_hashlib/__init__.mpy /lib/adafruit_hashlib/_md5.mpy /lib/adafruit_hashlib/_sha1.mpy /lib/adafruit_hashlib/_sha224.mpy /lib/adafruit_hashlib/_sha256.mpy /lib/adafruit_hashlib/_sha384.mpy /lib/adafruit_hashlib/_sha512.mpy"
)
be.based.run("rmdir /lib/adafruit_hashlib")
be.based.run(
    "rm /bin/crc32.lja /bin/hashutils/crc32.py /bin/hashutils/crc32subscript.py /bin/md5sum.lja /bin/hashutils/md5sum.py /bin/hashutils/md5subscript.py /bin/sha1sum.lja /bin/hashutils/sha1sum.py /bin/hashutils/sha1subscript.py /bin/sha224sum.lja /bin/hashutils/sha224sum.py /bin/hashutils/sha224subscript.py /bin/sha256sum.lja /bin/hashutils/sha256sum.py /bin/hashutils/sha256subscript.py /bin/sha384sum.lja /bin/hashutils/sha384sum.py /bin/hashutils/sha384subscript.py /bin/sha512sum.lja /bin/hashutils/sha512sum.py /bin/hashutils/sha512subscript.py"
)
be.based.run("rmdir /bin/hashutils")
be.api.setvar("return", "0")
