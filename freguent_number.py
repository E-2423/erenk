
  Hello how are you today?I am very good.
  freguent number cod:


numbers = [1, 3, 7, 4, 4, 3, 0, 3, 16, 4, 3, 7, 4, 4]
item = max(numbers, key = numbers.count)
repetition = numbers.count(item)
print("the most frequent number is {} and it was {} times \
repeated".format(item, repetition))
the most frequent number is 4 and it was 5 times repeated


numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
item = max(numbers, key = numbers.count)
repetition = numbers.count(item)
print("the most frequent number is {} and it was {} times \
repeated".format(item, repetition))
the most frequent number is 3 and it was 4 times repeated

numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
item = max(numbers, key = numbers.count)
repetition = numbers.count(item)
print(f"the most frequent number is {item} and it was {repetition} times repeated.")

