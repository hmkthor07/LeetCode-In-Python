"""
Given the capacity of the cache, implement a put and a get operation for an LRU cache

Step 1: Define the input/output interface

"""

class LRUCache:
    def initializer(self, length:int) -> None:
        self.length = length
        self.my_list = []

    def get(self, key) -> None:
        flag = False
        for eachMap in self.my_list:
            if key in eachMap:
                tmp = eachMap
                self.my_list.remove(eachMap)
                self.my_list.insert(0,tmp)
                flag = True
                break
        if flag == False:    
            return -1

    def put(self, key, value) -> None:
        flag = False
        for eachMap in self.my_list:
            if key in eachMap:
                tmp = eachMap
                self.my_list.remove(eachMap)
                self.my_list.insert(0,tmp)
                flag = True
                break
        if (flag == False): 
            if len(self.my_list) == self.length:
                return -1
            else:
                self.my_list.insert(0,{key:value})

    def printMe(self):
        print(self.my_list)

s = LRUCache()
s.initializer(4)
s.put(1,100)
s.put(2,200)
s.get(1)
s.put(3,300)
s.get(2)
s.put(4,400)
s.printMe()

