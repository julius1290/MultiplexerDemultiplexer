class BasicRam:

    pages: int
    rows: int
    storage: any

    def __init__(self, pages: int, rows: int):
        self.storage = [[None for x in range(rows)] for y in range(pages)]
        self.pages = pages
        self.rows = rows

    def store(self, data_word, pos: tuple):
        if pos[0] <= self.pages and pos[1] <= self.rows:
            self.storage[pos[0]][pos[1]] = data_word
            return (pos)
        print("RamOverload")
        return (-1, -1)

    def read(self, page: int, row: int):
        return self.storage[page][row]

    def delete(self, page: int, row: int):
        self.storage[page][row] = None
