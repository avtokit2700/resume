topping = []


def topping_pizza(top):
    """print"""
    print("Your choises is : ")
    for t in top:
        print("-" + t)

while True:
    top_pizza = input("Enter topping for your pizza(enter q for quit): ")
    if top_pizza != 'q':
        topping.append(top_pizza)
    else:
        break

topping_pizza(topping)
