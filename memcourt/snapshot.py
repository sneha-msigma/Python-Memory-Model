# memcourt/snapshot.py

import gc


class Snapshot:
    def __init__(self, data):
        self.items = []
        self._capture(data)

    def _capture(self, data):
        for name, obj in data.items():
            self.items.append({
                "name": name,
                "id": id(obj),
                "value": repr(obj),
                "refs": len(gc.get_referents(obj))
            })

    def diff(self, other):
        result = {
            "aliasing": False,
            "nested_mutation": False,
            "details": []
        }

        before_map = {i["name"]: i for i in self.items}
        after_map = {i["name"]: i for i in other.items}

        # Aliasing check
        ids = [i["id"] for i in self.items]
        if len(ids) != len(set(ids)):
            result["aliasing"] = True

        # Nested mutability check
        for name in before_map:
            if name in after_map:
                b = before_map[name]
                a = after_map[name]
                if b["id"] == a["id"] and b["value"] != a["value"]:
                    result["nested_mutation"] = True
                    result["details"].append(name)

        return result
