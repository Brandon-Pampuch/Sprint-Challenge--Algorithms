
test = 700
loopcount = 0


def bunnyEars(bunnies):
    global loopcount
    loopcount = loopcount + 1
    print(loopcount)
    if bunnies == 0:
        return 0

    return 2 + bunnyEars(bunnies-1)


print(bunnyEars(test))
