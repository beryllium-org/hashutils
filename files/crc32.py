vr("opts", be.api.xarg())

if len(vr("opts")["w"]):
    from binascii import crc32

    be.api.setvar("return", "")
    for pv[get_pid()]["i"] in vr("opts")["w"]:
        with be.api.fs.open(vr("i"), "rb") as pv[get_pid()]["f"]:
            if vr("f") is not None:
                vr("data", vr("f").read())
                vr("data", hex(crc32(vr("data")))[2:])

                be.based.user_vars["return"] += str(vr("data")) + " " + vr("i") + "\n"
                vrd("data")
            else:
                be.based.error(4, vr("i"))
                be.api.setvar("return", "1")
                break
    if be.api.getvar("return") != "1":
        be.api.setvar("return", be.api.getvar("return")[:-1])
        term.write(be.api.getvar("return"))
    del crc32
else:
    be.based.error(1)
    be.api.setvar("return", "1")
