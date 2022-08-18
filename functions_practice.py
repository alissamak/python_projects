def hello():
    print("Hello!")

def pack(x, y, z):
    return [x, y, z]

def eat_lunch(my_list):
    if len(my_list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(my_list)):
            if i == 0:
                print(f"First I eat {my_list[0]}")
            else:
                print(f"Next I eat {my_list[i]}")


hello()
print(pack("x", "y", "z"))
print(pack("shoes", "lunch", "hat"))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple", "oreos", "sandwich", "tuna"])