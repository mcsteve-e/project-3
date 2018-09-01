import Array

class Associator:
    def __init__(self, size):
        ''' Creates two different versions of the program:
            one resizes, and the other does not.
        '''
        self.size = size
        self.prim_keys = Array.Array(size)
        self.prim_values = Array.Array(size)
        self.ovflw_keys = Array.Array(size)
        self.ovflw_values = Array.Array(size)
        self.resizing = True 
        self.debugging = False

    def _hash(self, key):
        total = (ord(key[0])+ord(key[-1]))*79
        value = total % self.size
        return value

    def _rehash(self, key):
        pos = 0
        total = 0
        for x in key:
            total += (ord(x)*31)
        value = total % self.size
        return value

    def put(self, key, value):
        h = self._hash(key)
        r = self._rehash(key)
        o = 0
        n = 0
        if self.prim_keys[h] == None:
            self.prim_keys[h] = key
            self.prim_values[h] = value
        else:
            if self.prim_keys[h] == key:
                self.prim_values[h] = value
                return
            elif self.prim_keys[h] != key:
                if self.ovflw_keys[r] == None:
                    self.ovflw_keys[r] = key
                    self.ovflw_values[r] = value
                else:
                    if self.ovflw_keys[r] == key:
                        self.ovflw_values[r] = value
                    elif self.ovflw_keys[r] != key:
                        o = self._find_ovflow(key)
                        if o != -1:
                            self.ovflw_values[o] = value
                        else:
                            n = self._find_empty()
                            self.ovflw_keys[n] = key
                            self.ovflw_values[n] = value
        return True

    def get(self, key):
        h = self._hash(key)
        r = self._rehash(key)
        o = 0
        if self.prim_keys[h] == None:
            return None
        elif self.prim_keys[h] == key:
            return self.prim_values[h]
        else:
            print("Hash1(" + key + ")=" + str(h))
            if self.ovflw_keys[r] == None:
                return None
            else:
                if self.ovflw_keys[r] == key:
                    print("Hash2(" + key + ")=" + str(r))
                    return self.ovflw_values[r]
                elif self.ovflw_keys[r] != key:
                    o = self._find_ovflw(key)
                    return self.ovflw_values[o]
        return None

#   def delete(key):
#       return

    def exists(self, key):
        h = self._hash(key)
        r = self._hash(key)
        if self.prim_keys[h] == key:
            return True
        elif self.ovflw_keys[r] == key:
            return True
        else: return False
 
#   def find(value):
#       return

    def stats(self):
        size = self.size
        prim_used = 0
        ovflw_used = 0
        for key in self.prim_keys:
            if key != None:
                prim_used += 1
        for key in self.ovflw_keys:
            if key != None:
                ovflw_used += 1
        print("\nSTATISTICS")
        print("--------------------")
        print("The size of the primary area is: %d \nNumber of used slots in primary area: %d \nThe size of the secondary area is: %d \nNumber of used slots in secondary area: %d" %
              (size, prim_used, size, ovflw_used))
        return

    def debug(self):
        self.debugging = True
        for key in self.prim_keys:
            if key != None:
                print("Hash1(%s) = %d" % (key, self._hash(key)))
        for key in self.ovflw_keys:
            if key != None:
                print("Hash1(%s) = %d" % (key, self._hash(key)))
                print("Hash2(%s) = %d" % (key, self._rehash(key)))
        return

    def dump(self):
        s = ""
        for i in range(0,len(self.prim_keys)):
            if self.prim_keys[i] is not None:
                s += "put " + self.prim_keys[i] + "=" + self.prim_values[i] + "\n"

        for i in range(0,len(self.ovflw_keys)):
            if self.ovflw_keys[i] is not None:
                s += "put " + self.ovflw_keys[i] + "=" + self.ovflw_values[i] + "\n";
        return s
            
    def print(self):
        print("\nPRIMARY AREA")
        print("--------------------")
        count=0
        for i in range(len(self.prim_keys)):
            if self.prim_keys[i] != None:
                print("%2d. %-12s %-12s" % (i, self.prim_keys[i], self.prim_values[i]))
                count += 1
        print("(" + str(count) + " key/value pairs in primary area)")

        count = 0
        for i in range(len(self.ovflw_keys)):
            if self.ovflw_keys[i] != None:
                count += 1
        if count == 0:
            print(" Secondary area is empty")
            return
    
        print("\nSECONDARY AREA")
        print("--------------------")
        for i in range(len(self.ovflw_keys)):
            if self.ovflw_keys[i] != None:
                print("%2d. %-12s %-12s" % (i, self.ovflw_keys[i], self.ovflw_values[i]))
        print("(" + str(count) + " key/value pairs in primary area)")

    def clear(self):
        self.prim_keys = Array.Array(size)
        self.prim_values = Array.Array(size)
        self.ovflw_keys = Array.Array(size)
        self.ovflw_values = Array.Array(size)
                
    def _find_ovflow(self, key):
        for i in range(len(self.ovflw_keys)):
            if self.ovflw_keys[i] == key:
                return i
        return -1

    def _find_empty(self):
        for i in range(len(self.ovflw_keys)):
            if self.ovflw_keys[i] == None:
                return i
        return #supposed to return self._resize() but didn't do that method

#   def _resize(self):
#       return

#   def _compact(self):
#       return
