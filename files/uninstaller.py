be.based.run(
    "rm /lib/adafruit_hashlib/__init__.mpy /lib/adafruit_hashlib/_md5.mpy /lib/adafruit_hashlib/_sha1.mpy /lib/adafruit_hashlib/_sha224.mpy /lib/adafruit_hashlib/_sha256.mpy /lib/adafruit_hashlib/_sha384.mpy /lib/adafruit_hashlib/_sha512.mpy"
)
be.based.run("rmdir /lib/adafruit_hashlib")
be.based.run(
    "rm /bin/md5sum.lja /bin/hashutils/md5sum.py /bin/sha1sum.lja /bin/hashutils/sha1sum.py /bin/sha224sum.lja /bin/hashutils/sha224sum.py /bin/sha256sum.lja /bin/hashutils/sha256sum.py /bin/sha384sum.lja /bin/hashutils/sha384sum.py /bin/sha512sum.lja /bin/hashutils/sha512sum.py"
)
be.based.run("rmdir /bin/hashutils")
be.api.setvar("return", "0")
