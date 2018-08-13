#!/usr/bin/env python


class First:

    def __init__(self, numbers):
        self.numbers = numbers


    def numsort(self):
        return sorted(self.numbers)

    def numsum(self):
        i = 0
        for n in self.numbers:
            i += n
        return n

    def getlow(self):
        low = self.numbers[0]
        for n in self.numbers:
            if n < low:
                low = n
        return n

    def gethigh(self):
        high = self.numbers[0]
	for n in self.numbers:
            if n > high:
		high = n
	return n

    
                
        
