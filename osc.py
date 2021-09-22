import math

# Imagine a set of toilets that are slowly
# getting filled up. The moment a toilet is filled up,
# it flushes, filling up all other toilets by some small amount
# Also imagine that the toilets are leaking, so that the more full they are,
# the less they get filled up. The following is a discrete demonstration of 
# the syncronization of the flushing.

# A step fill up of all oscillators
def fill_up(oscs):
    for index, osc in enumerate(oscs):
        oscs[index] += math.sqrt(25-pow(oscs[index],2))
    return oscs

# Discharge any full oscillators, do so until no discharge is possible
def discharge(oscs):
    for index, osc in enumerate(oscs):
        if osc >= 5:
            oscs[index] = 0 
            for index2, osc2 in enumerate(oscs):
                if index != index2:
                    oscs[index2] += 0.0001
            discharge(oscs)
    return oscs

# Initial conditions for 100 oscillators
oscs = [0.05*x for x in range(0,99)]
print("Initial Conditions:")
print(oscs)

while True:
    oscs = fill_up(oscs)
    oscs = discharge(oscs)
    # Crude check to stop 
    if(abs(oscs[0]-oscs[1]) < 0.05 and abs(oscs[1]-oscs[2]) < 0.05 and abs(oscs[0]-oscs[2])<0.05):
        print("Final Conditions:")
        print(oscs)
        break
