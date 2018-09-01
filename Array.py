class Array:
	''' Makes a fixed-size array that cannot be expanded or contracted, and 
	   elements in the middle cannot be deleted or added without copying all
	   other elements down or up.
	   This is useful when you want to set bounds on the size of a list.
	   Python's list type expands and contracts as needed.
	   If you try to go outside the bounds of the size of this array, it will
	   throw a ValueError. 
	'''

	def __init__(self, parm1, initialvalue=None):
		'''   Contructs a new fixed-size array.  You can give the
		     constructor either an int, which will specify the size of
		     the array, or a list, which will be copied into the array.
		     The size of your array will start out as the size of the list's
		     value when you initialize it.  But it cannot expand or contract.
		     If you specify the size only, then you can specify the initial
		     value to store.  If you don't it defaults to None.
		'''

		self.innerlist = []
		if type(parm1) == list:
			self.size = len(parm1)
			for x in parm1:
				self.innerlist.append(x)
		else:
			self.size = parm1
			for i in range(self.size):
				self.innerlist.append(initialvalue)
	
	def __getitem__(self, index):
		'''  Used with the brackets notation to get an item out of the array.
		    If you give an index number less than 0 or greater than the 
		    size -1 it will throw a ValueError.
		    Example use:         x = myarray[5]
		'''
		assert type(index) is int, "__getitem__ requires int index"
		if index >= 0 and index < self.size:
			return self.innerlist[index]
		else:
			raise ValueError("Array index out of bounds")

	def __setitem__(self, index, newvalue):
		'''  Used with the brackets notation to put an item into the array
		    at the specified location, or change the value that is there.
		    If you give an index number less than 0 or greater than the 
		    size -1 it will throw a ValueError.
		    Example use:         myarray[5] = x
		'''
		assert type(index) is int, "__getitem__ requires int index"
		if index >= 0 and index < self.size:
			self.innerlist[index] = newvalue
		else:
			raise ValueError("Array index out of bounds")

	def __len__(self):
		'''   Returns the size of the array, which is the one fixed by __init__
		     and not open to change.
		'''
		return self.size

	def __list__(self):
		'''  Allows us to get at the actual Python list underneath.
		    You can use this in a casting fashion:    newlist = list(myarray)
		'''
		return self.innerlist

	def __iter__(self):
		'''  this is used with a for in loop to iterate through the array.
		    Needs __next__() as well for this to work.
		'''
		self.__i__ = 0
		return self

	def __next__(self):
		'''  used in conjunction with __iter__ to iterate through the array.
		    Used with for in loops.
		'''
		if self.__i__ < self.size:
			k = self.__i__
			self.__i__ += 1
			return self.innerlist[k]
		else:
			raise StopIteration
		

def main():
	heat = Array(10)   # fixed size array, cannot go outside bounds
	heat[0] = 75
	heat[1] = 55
	heat[2] = 97
	print(heat[1])
	#heat[20] = 55
	stuff = Array([57,26,33,97])   # start out with these values, also size is fixed to 4
	print(stuff[3])
	print("  now iterate  ")
	for k in stuff:
		print("----",k)
	z = list(stuff)
	print(z)
	#stuff[4] = 999    # or comment this out and proceed to the following

	try:
		stuff[4] = 999
	except ValueError:
		print("Illegal array operation")

if __name__ == "__main__":
	main()