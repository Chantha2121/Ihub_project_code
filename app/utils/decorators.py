
def local_val(dct):
    dct.pop("self", None)
    return list(dct.values())


def local_dict(**kwargs):
    return locals()["kwargs"]


def repr(obj):
    name = obj.__class__.__name__
    data = ",".join(
        "%s=%s" % (k, obj.__dict__[k]) for k in obj.__dict__ if "_sa_" != k[:4]
    )
    return f"[{name}({data})]"