# Michael Williamson
# 1/10/2022
# Create a simple Juice class, which has name and capacity properties. The class should also
# permit the adding of two separate instances of the Juice object resulting in a new instance with
# the combined capacity and names of the juices being added
# For example, if you add an Orange juice with 1.0 capacity and an Apple juice with 2.5
# capacity, the resulting juice should have:
# name: “Orange&Apple”, capacity: 3.5
import time
start_time = time.time()

# First attempt

class Juice():
    def __init__(self, name, capacity) -> None:
        self.name = name
        self.capacity = capacity

    def addJuice(self, juice):
        return(Juice(self.name+"&"+juice.name, self.capacity+juice.capacity))

aj = Juice('apple', 2.5)
oj = Juice('orange', 1.0)

oaj = oj.addJuice(aj)
oaoaj = oaj.addJuice(oaj)

print("name: ", oaoaj.name)
print("capacity: ",  oaoaj.capacity)
print("--- %s seconds ---" % (time.time() - start_time))