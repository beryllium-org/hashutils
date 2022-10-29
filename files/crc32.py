opts = ljinux.api.xarg()

try:
    if len(opts["w"]) > 0:
        with open(ljinux.api.betterpath(opts["w"][0]), "rb") as f:
            dataa = f.read()
            from binascii import crc32

            dataa = hex(crc32(dataa))[2:]
            del crc32
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
