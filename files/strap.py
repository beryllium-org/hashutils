try:
    mkdir(path.join(root, "lib/adafruit_hashlib"))
except FileExistsError:
    pass

for i in [
    "__init__.mpy",
    "_md5.mpy",
    "_sha1.mpy",
    "_sha224.mpy",
    "_sha256.mpy",
    "_sha384.mpy",
    "_sha512.mpy",
]:
    shutil.copy(i, path.join(root, "lib/adafruit_hashlib", i))

for i in [
    "crc32.lja",
    "md5sum.lja",
    "sha1sum.lja",
    "sha224sum.lja",
    "sha256sum.lja",
    "sha384sum.lja",
    "sha512sum.lja",
]:
    shutil.copy(i, path.join(root, "bin", i))

try:
    mkdir(path.join(root, "bin/hashutils"))
except FileExistsError:
    pass

for i in [
    "crc32.py",
    "md5sum.py",
    "sha1sum.py",
    "sha224sum.py",
    "sha256sum.py",
    "sha384sum.py",
    "sha512sum.py",
    "sha512subscript.py",
]:
    shutil.copy(i, path.join(root, "bin/hashutils", i))
