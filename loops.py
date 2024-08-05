for i in range(5):
    print(i)

print("---------")

for i in range(2, 11, 2):
    print(i)


fruits = ["apple", "cherry", "banana"]
for fruit in fruits:
    print(fruit)

text = "Python"
for char in text:
    print(char)


person = {"name":"John", "age":30, "city":"New York"}
for key, value in person.items():
    print(key, value)


counter = 0
while counter < 5:
    print(counter)
    counter +=1

total = 0
number = 1
while number <= 10:
    total += number
    number += 1
print("Sum numbers of 1 to 10 is", total)