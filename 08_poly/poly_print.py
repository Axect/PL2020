from poly import Polynomial, zip_with

a = Polynomial([1,2,-3])
print(a)

b = zip_with(lambda x, y: x + y, [1,2,3], [3,1])
print(b)

c = zip_with(lambda x, y: x * y, [1,2,3],[3,4,5])
print(c)
print(sum(c))
