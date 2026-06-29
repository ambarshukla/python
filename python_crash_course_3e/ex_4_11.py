my_pizzas = ['pepperoni','chicken']
your_pizzas = my_pizzas[:]

my_pizzas.append('tuna')
your_pizzas.append('veggies')

print("My pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("---\nYour pizzas are:")
for pizza in your_pizzas:
    print(pizza)
