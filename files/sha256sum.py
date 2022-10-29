opts = ljinux.api.xarg()

try:
    if len(opts["w"]) > 0:
        with open(ljinux.api.betterpath(opts["w"][0]), "rb") as f:
            dataa = f.read()
            from adafruit_hashlib import sha256

            a = sha256()
            a.update(dataa)
            dataa = a.hexdigest()
            del (
                a,
                sha256,
                modules["adafruit_hashlib"],
                modules["adafruit_hashlib._sha512"],
                modules["adafruit_hashlib._sha1"],
                modules["adafruit_hashlib._sha256"],
                modules["adafruit_hashlib._md5"],
            )
            ljinux.based.user_vars["return"] = str(dataa) + " " + opts["w"][0]
            del dataa
            print(ljinux.based.user_vars["return"])
    else:
        ljinux.based.error(1)
        ljinux.based.user_vars["return"] = "1"


except OSError:
    ljinux.based.error(4, ljinux.based.user_vars["argj"].split()[1])
    ljinux.based.user_vars["return"] = "1"

del opts
