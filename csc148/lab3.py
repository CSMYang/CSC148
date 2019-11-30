class my_queue:
    def __init__(self) -> None:
        self.content = []

    def add(self, item) -> None:
        self.content.append(item)

    def remove(self) -> object:
        return self.content.pop(0)

    def list_container(self) -> object:

