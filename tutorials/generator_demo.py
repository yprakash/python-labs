# @author: yprakash
# A simple generator function

m = (x ** 2 for x in range(5))
print(next(m))
print(next(m))
print(list(m))

def create_generator():
    mylist = range(3)
    for e in mylist:
        yield e*e

my_generator = create_generator()  # create a generator
print(my_generator)  # my_generator is an object!
for i in my_generator:
    print(i)
