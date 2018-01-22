class file_reader:

    def __init__(self, readFile):
        self.f = open(readFile, "rb")

    def read(self):
        return self.f.read()
