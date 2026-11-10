class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        if i < self.length:
            return self.arr[i]
        # Throw error if index is out of bounds


    def set(self, i: int, n: int) -> None:
        if i < self.length:
            self.arr[i] = n
        # Throw error if index is out of bounds


    def pushback(self, n: int) -> None:
        if self.capacity == self.length:
            self.resize()
        self.arr[self.length] = n
        self.length += 1
        


    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
            element = self.arr[self.length]
            self.arr[self.length] = 0
            return element
        # Throw error if index is out of bounds
 

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        newArray = [0] * self.capacity

        for i in range(self.length):
            newArray[i] = self.arr[i]
        
        self.arr = newArray


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
