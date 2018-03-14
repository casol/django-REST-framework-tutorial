#! /usr/bin/python

import pickle


class Animal:
 def __init__(self, attr="Horse"):
      self.attr = attr



# serialize - save to file
def test_serialize():
    a = Animal()
    print a.attr
    f = open("dump.dat", "w")
    pickle.dump(a, f)
    f.close()

# deserialize - load from file
def test_deserialize():
    f = open("dump.dat", "r")
    a = pickle.load(f)
    f.close()
    print(a.attr)

def test():
    test_serialize()
    test_deserialize()

if __name__ == "__main__":
    test()

