Elemento = dict[int, object]

class thing(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self) -> str:
        return f"key: {self.key}, value: {self.value}"

class Node:
    def __init__(self, element: Elemento) -> None:
        self.key = element["key"]
        self.value = element["value"]

    def print(self):
        print(type(self.value))
        print(self.key)
        print(type(self.key))
        print(self.value)
        print(type(self.value))

if __name__ == "__main__":
    t = thing(1, "a")
    n = Node({"key": 1, "value": t})
    print(n.key)
    n.key = 2
    key_attr = "key"
    print(eval(f"n.{key_attr}"))

    n.print()
