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

	# these are needed to decode packed addresses, so
	# read them first
	self.r_o = self.twobytes(40) / 8
	self.s_o = self.twobytes(42) / 8
   
        self.high_mem_loc = self.twobytes(4)
        self.initpc_loc = self.twobytes(6) # version < 6
        self.main_loc = self.read_packed_address(6) # version >= 6

        self.dict_loc = self.twobytes(8)
        self.object_table_loc = self.twobytes(10)
        self.global_vars_table_loc = self.twobytes(12)
        self.static_mem_loc = self.twobytes(14)

    def twobytes(self, loc):
        one = self.mem[loc]
        two = self.mem[loc + 1]
        return (one << 8) + two

    def byte(self, loc):
        return self.mem[loc]

    def decode_packed_address(self, p, paddr):
        if (self.version <= 3):
            return 2 * p
        elif (self.version <= 5):
            return 4 * p
        elif (self.version <= 7 and paddr == False):
            return (4 * p) + (8 * self.r_o)
        elif (self.version <= 7):
            return (4 * p) + (8 * self.s_o)
        elif (self.version == 8):
            return (8 * p)

    def read_packed_address(self, loc, paddr=False):
	return self.decode_packed_address(self.twobytes(loc), paddr)
