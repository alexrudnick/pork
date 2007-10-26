import array, os

class Memory:
    "Represents the memory of the z-machine"

    # an array that represnts memory
    mem = array.array('B')
    version = None 

    def __init__(self, filename):
        f = open(filename)
        self.mem.fromfile(f, os.stat(filename)[6])
        self.version = self.byte(0)

    def twobytes(self, loc, a):
        one = self.mem[loc]
        two = self.mem[loc + 1]
        return (one << 8) + two

    def byte(self, loc):
        return self.mem[loc]

