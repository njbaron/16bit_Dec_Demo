class key_reader:

    def _init_(self, keyFile):
        self.f = open(keyFile, "rb")
        self.newKey = self.get_new_key()

    def get_new_key(self):
        return self.f.read(1)


    def get_key(self):
        currentKey = self.newKey
        self.newKey = self.get_new_key()
        return currentKey

    def has_next(self):
        return not self.newKey

