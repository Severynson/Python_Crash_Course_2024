cars = ["bmw", "audi", "cadilac"]
print(cars)  # printing ["bmw", "audi", "cadilac"] how it is...
print(*cars)  # printing bare values without [ , , , ]
print(cars[0])  # zero element
print(cars[-1])  # last
print(cars[-2])  # one before last

cars[0] = "ducati"  # changing value by a zero index for 'ducati' instead of 'bmw'
print(*cars)  # displaying changes

cars.append("merzedes")  # adding a new value to the end ('merzedes')
print(*cars)  # displaying changes

cars = []
print(*cars)  # crearing the list and ensuring in success by displaying it
cars.append("bmw")
cars.append("audi")
cars.append("cadilac")
print(*cars)  # creating a list from scratch with append and displaying it

cars = ["(value that was initial)"]
print(*cars)  # crearing the list and ensuring in success by displaying it
cars.insert(0, "bmw")
cars.insert(0, "audi")
cars.insert(0, "cadilac")
print(*cars)
# it is possible to push new elements into a certain position by the method ".insert",
# the previous value by a selected index and the following elements will shift by 1 position ahead each

cars = ["bmw", "audi", "cadilac"]
del cars[0]  # deleting the element by a zero index
print(*cars)  # now list is just ["audi", "cadilac"]

cars = ["bmw", "audi", "cadilac"]
lastValNowDeleted = cars.pop()
# by default ".pop()" method removes a last element from the list and return it
print(
    f"The last value of the 'cars' list which is now deleted was: '{lastValNowDeleted}'"
)
print(f"Now the list of cars looks like: {cars}")

cars = ["bmw", "audi", "cadilac"]
elementWithIndexOneDeletedNow = cars.pop(1)
print(f"{elementWithIndexOneDeletedNow} was deleted from the list of cars")
print(f"New list of cars appearance {cars}")


cars = ["bmw", "audi", "cadilac"]
cars.remove("cadilac")  # Deleting an element from the cars list knowing just its value
print(f"New list of cars appearance {cars}")

cars = ["bmw", "audi", "cadilac"]
numbers = [2, 3, 1]
stringNums = ["2", "3", "1"]
cars.sort()  # By default sort in the alphabetic ...
numbers.sort()  # or numerc order ...
stringNums.sort()  # order
print(cars)
print(numbers)
print(stringNums)

cars = ["bmw", "audi", "cadilac"]
numbers = [2, 3, 1]
stringNums = ["2", "3", "1"]
cars.sort(reverse=True)  # Now - sorted in the reversed order
numbers.sort(reverse=True)
stringNums.sort(reverse=True)
print(cars)
print(numbers)
print(stringNums)

numbers = [2, 3, 1]
print(f"Initialy the numbers list was: {numbers}")
print(f"No changes, just displaying with a 'sorted()' function: {sorted(numbers)}")
print(f"The numbers list is still: {numbers}, completely the same as it was")
print(
    f"Reverse=True parameter also works for the 'sorted(toSortList, reverse=True)': {sorted(numbers, reverse=True)}"
)

numbers = [2, 3, 1]
numbers.reverse()
print(numbers)  # Notice - reverse, but doesn't sort
numbers.reverse()
print(numbers)  # Now - the same order as it was initialy again

numbers = [2, 3, 1]
lengthOfNumList = len(numbers)  # returns a length of the list
print(lengthOfNumList)
    