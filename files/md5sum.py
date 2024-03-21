vr("opts", be.api.xarg())

if len(vr("opts")["w"]):
    from adafruit_hashlib import md5

    be.api.setvar("return", "")
    for pv[get_pid()]["i"] in vr("opts")["w"]:
        with be.api.fs.open(vr("i"), "rb") as pv[get_pid()]["f"]:
            if vr("f") is not None:
                vr("data", vr("f").read())
                vr("a", md5())
                vr("a").update(vr("data"))
                vr("data", vr("a").hexdigest())
                vrd("a")

                be.based.user_vars["return"] += str(vr("data")) + " " + vr("i") + "\n"
                vrd("data")
            else:
                be.based.error(4, vr("i"))
                be.api.setvar("return", "1")
                break
    if be.api.getvar("return") != "1":
        be.api.setvar("return", be.api.getvar("return")[:-1])
        term.write(be.api.getvar("return"))
    del (
        md5,
        modules["adafruit_hashlib"],
        modules["adafruit_hashlib._md5"],
        modules["adafruit_hashlib._sha256"],
        modules["adafruit_hashlib._sha512"],
        modules["adafruit_hashlib._sha1"],
    )
else:
    be.based.error(1)
    be.api.setvar("return", "1")
