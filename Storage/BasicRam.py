class BasicRam:

    pages: int
    rows: int
    storage: any

    def __init__(self, pages: int, rows: int):
        self.storage = [[None for x in range(rows)] for y in range(pages)]
        self.pages = pages
        self.rows = rows

    def store(self, data_word):
        for i in range(self.pages):
            for j in range(self.rows):
                if self.storage[i][j] is None:
                    self.storage[i][j] = data_word
                    return (i,j)
        print("RamOverload")
        return (-1, -1)

    def read(self, page: int, row: int):
        return self.storage[page][row]

    def delete(self, page: int, row: int):
        self.storage[page][row] = None
