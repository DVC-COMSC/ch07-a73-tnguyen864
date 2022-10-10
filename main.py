# List of numbers
numbers = [5, 20, 30, 35, 50]

# Get insertion value and add to list
insval = int(input('Enter the insertion value: '))
numbers.append(insval)

# Sort list
numSorted = []
for i in range(len(numbers)):
    minIndex = numbers.index(min(numbers))
    transfer = numbers.pop(minIndex)
    numSorted.append(transfer)

# Print sorted numbers
print (numSorted)
