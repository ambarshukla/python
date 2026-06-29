cities = ['London', 'Paris', 'Pune', 'Mumbai', 'Manila', 'Tokyo', 'New York']

print(f"List of cities is: {cities}")

print("First 3 cities are:")
for city in cities[0:3]:
      print(city)


print("---")
print("Last 3 cities are:")
for city in cities[-3:]:
      print(city)

print("---")
middle = int(len(cities)/2)-1
print("Middle 3 cities are:")
for city in cities[middle:middle+3]:
      print(city)
