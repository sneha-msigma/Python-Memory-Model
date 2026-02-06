# main.py

import sys
import importlib
from memcourt.snapshot import Snapshot
from memcourt.cli import show


def run_case(title, make, change, json_out):
    print(f"\n{title}")

    data = make()
    before = Snapshot(data)

    change(data)
    after = Snapshot(data)

    diff = before.diff(after)
    show(before, after, diff, json_out)


def main():
    script_name = sys.argv[2].replace(".py", "")
    script = importlib.import_module(script_name)
    json_out = "--json" in sys.argv

    run_case(
        "Aliasing Case",
        script.alias_make,
        script.alias_change,
        json_out
    )

    run_case(
        "Nested Mutability Case",
        script.nested_make,
        script.nested_change,
        json_out
    )


if __name__ == "__main__":
    main()
