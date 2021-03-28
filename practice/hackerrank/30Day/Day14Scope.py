class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        for i in range(len(self.__elements) - 1):
            for j in range(len(self.__elements) - 1):
                if abs(self.__elements[i] - self.__elements[j + 1]) > self.maximumDifference:
                    self.maximumDifference = abs(self.__elements[i] - self.__elements[j + 1])
        return self.maximumDifference


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

