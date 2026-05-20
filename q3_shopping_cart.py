# q3_shopping_cart.py

# -----------------------------------
# Part A — Spot the Bug
# -----------------------------------

def add_item(item, cart=[]):
    cart.append(item)
    return cart


print("Part A Output:")
print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))

"""
Expected Output:

['apple']
['apple', 'banana']
['bread', 'milk']
['apple', 'banana', 'eggs']

Explanation:
The default list cart=[] is created ONLY ONCE when the function is defined,
not every time the function is called.

So:
1st call -> list becomes ['apple']
2nd call -> SAME list reused -> ['apple', 'banana']
3rd call -> a NEW list ['bread'] is passed explicitly
4th call -> original default list reused again -> ['apple', 'banana', 'eggs']
"""


# -----------------------------------
# Part B — Correct Fix
# -----------------------------------

def fixed_add_item(item, cart=None):
    # Create a fresh list every time if cart is not provided
    if cart is None:
        cart = []

    cart.append(item)
    return cart


print("\nPart B Output:")
print(fixed_add_item("apple"))
print(fixed_add_item("banana"))
print(fixed_add_item("milk", ["bread"]))
print(fixed_add_item("eggs"))


# -----------------------------------
# Part C — Shopping Cart Program
# -----------------------------------

# Function to create a cart
def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


# Function to add items to cart
def add_to_cart(cart, name, price, qty=1):
    item = {
        "name": name,
        "price": price,
        "qty": qty
    }

    cart["items"].append(item)


# Function to demonstrate tuple immutability
def update_price(price_tuple, new_price):

    # Tuples are immutable.
    # Attempting to change an element raises TypeError.

    try:
        price_tuple[1] = new_price
    except TypeError as e:
        print("\nTuple Modification Error:")
        print(e)


# Function to calculate total after discount
def calculate_total(cart):

    total = 0

    for item in cart["items"]:
        total += item["price"] * item["qty"]

    discount_amount = (cart["discount"] / 100) * total
    final_total = total - discount_amount

    return final_total


# -----------------------------------
# Demonstration
# -----------------------------------

# Create two independent carts
cart1 = create_cart("Rakesh", discount=10)
cart2 = create_cart("Arjun", discount=5)

# Add items to cart1
add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 1000, 2)

# Add items to cart2
add_to_cart(cart2, "Phone", 20000, 1)
add_to_cart(cart2, "Charger", 1500, 1)

# Display carts
print("\nCart 1:")
print(cart1)

print("\nCart 2:")
print(cart2)

# Calculate totals
print("\nFinal Total for Cart 1:", calculate_total(cart1))
print("Final Total for Cart 2:", calculate_total(cart2))

# Demonstrate tuple immutability
price_info = ("Laptop", 50000)

update_price(price_info, 60000)


# -----------------------------------
# Discussion Points
# -----------------------------------

"""
1. Why is discount=0 safe but cart=[] dangerous?

discount=0 is safe because integers are immutable.
Python creates a new integer object when needed.

cart=[] is dangerous because lists are mutable.
The SAME list object is reused across function calls.


2. What is the difference between rebinding and mutating?

Rebinding:
Changing the variable reference to point to a new object.

Example:
x = [1, 2]
x = [3, 4]

Mutating:
Changing the contents of the same object.

Example:
x.append(5)


3. Which of these are mutable?

Mutable:
- list
- dict
- set

Immutable:
- tuple
- str
- int


4. When you pass a list into a function and modify it,
   do changes reflect outside? Why?

Yes.

Lists are mutable objects.
Functions receive references to the same object,
so modifying the list inside the function changes
the original list outside the function as well.
"""