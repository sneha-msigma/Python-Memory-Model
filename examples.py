# examples.py

def alias_make():
    a = []
    b = a
    return {"a": a, "b": b}


def alias_change(data):
    data["a"].append(1)


def nested_make():
    x = {"k": [1, 2]}
    return {"x": x}


def nested_change(data):
    data["x"]["k"].append(3)
