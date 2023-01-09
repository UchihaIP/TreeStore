from typing import Optional, TypedDict


class Item(TypedDict):
    id: int
    parent: int
    type: str | None


class TreeStore:
    def __init__(self, items: list[Item]):
        self.items = {item["id"]: item for item in items}

    def get_all(self) -> list[Item]:
        """Возвращает все элементы списка"""
        return list(self.items.values())

    def get_item(self, id: int) -> Item:
        """Возвращает элемент по его id"""
        return self.items.get(id)

    def get_children(self, id: int) -> list[Item]:
        """Возвращает массив элементов,
        являющихся дочерними для элемента переданного в id
        """
        return [item for item in self.get_all() if item.get("parent") == id]

    def get_all_parents(self, id: int) -> list[Item]:
        """Возвращает массив из цепочки родительских элементов,
        начиная от самого элемента переданного в id
        """
        if id > len(self.items):
            raise TypeError(f"Элемента с id {id} - не существует")

        parent = self.get_item(id).get("parent")
        if parent and not parent == "root":
            return [self.get_item(parent)] + self.get_all_parents(parent)
        return []


def main() -> None:
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]

    ts = TreeStore(items)

    print(ts.get_all())
    print(ts.get_item(3))
    print(ts.get_children(4))
    print(ts.get_all_parents(6))
    print(ts.get_all_parents(9))



if __name__ == '__main__':
    main()
