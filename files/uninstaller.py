# adafruit_hashlib
hl = " &/lib/adafruit_hashlib/"
ljinux.api.var(
    "argj",
    "rm"
    + hl
    + "__init__.mpy"
    + hl
    + "_md5.mpy"
    + hl
    + "_sha1.mpy"
    + hl
    + "_sha224.mpy"
    + hl
    + "_sha256.mpy"
    + hl
    + "_sha384.mpy"
    + hl
    + "_sha512.mpy",
)
ljinux.based.command.fpexecc([None, "/bin/rm.py"])
del hl

ljinux.api.var("argj", f"rmdir &/lib/adafruit_hashlib")
ljinux.based.command.fpexecc([None, "/bin/rmdir.py"])

# bins
bl = " /bin/"
ljinux.api.var(
    "argj",
    "rm"
    + bl
    + "md5sum.lja"
    + bl
    + "md5sum.py"
    + bl
    + "sha1sum.lja"
    + bl
    + "sha1sum.py"
    + bl
    + "sha224sum.lja"
    + bl
    + "sha224sum.py"
    + bl
    + "sha256sum.lja"
    + bl
    + "sha256sum.py"
    + bl
    + "sha384sum.lja"
    + bl
    + "sha384sum.py"
    + bl
    + "sha512sum.lja"
    + bl
    + "sha512sum.py",
)
ljinux.based.command.fpexecc([None, "/bin/rm.py"])
del bl

ljinux.api.var("return", "0")
