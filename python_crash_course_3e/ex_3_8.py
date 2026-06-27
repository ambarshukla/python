fave_places = ['London', 'New York', 'Beijing', 'Taipei', 'Singapore']

print("Original list is", end="")
print(fave_places)


print("Sorted order is ", end="")
print(sorted(fave_places))


fave_places.sort()
print("Sorted original list ", end="")
print(fave_places)

fave_places.sort(reverse=True)
print("Reverse Sorted original list ", end="")
print(fave_places)
