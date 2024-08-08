import math
import random
import statistics

root = math.sqrt(16)
print(root)

print(math.pi)
print(math.e)

print(round(5.5))
print(math.floor(5.7))
print(math.ceil(5.7))

print("-------------------")

random_int = random.randint(1, 10)
print(random_int)

rand_range = random.randrange(1, 10)
print(rand_range)

rand_float = random.random()
print(rand_float)

rand_choice = random.choice([1, 2, 3, 4, 5])
print(rand_choice)

list = [1, 2 ,3, 4, 5]
random.shuffle(list)
print(list)

print("--------------")

data = [2 ,4, 6, 7, 9, 8, 4, 5, 10, 7]

data_mean = statistics.mean(data)
print(f"The mean of dataset is {data_mean}")

data_median = statistics.median(data)
print(f"The median of dataset is {data_median}")

data_mode = statistics.mode(data)
print(f"The mode of dataset is {data_mode}")

data_stdev = statistics.stdev(data)
print(f"The stdev of dataset is {data_stdev}")