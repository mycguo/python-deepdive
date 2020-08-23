min_length = 2
name = input("Please enter your name:")

while not(len(name) >= min_length and name.isprintable() and name.isalnum()):
    name = input("Please try again:")
print("Hello, {0}".format(name))

while True:
    name = input("Please enter your name:")
    if len(name) >= min_length and name.isprintable() and name.isalnum():
        print("Hello, {0}".format(name))
        break

s = 'hello'
for i, c in enumerate(s):
    print(i, c)
