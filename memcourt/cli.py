# memcourt/cli.py

import json


def show(before, after, diff, json_out=False):
    if json_out:
        print(json.dumps({
            "before": before.items,
            "after": after.items,
            "analysis": diff
        }, indent=2))
        return

    print("\nSNAPSHOT BEFORE")
    for i in before.items:
        print(i)

    print("\nSNAPSHOT AFTER")
    for i in after.items:
        print(i)

    print("\nANALYSIS")
    print("Aliasing detected:", diff["aliasing"])
    print("Nested mutability detected:", diff["nested_mutation"])

    if diff["details"]:
        print("Mutated variables:", diff["details"])
