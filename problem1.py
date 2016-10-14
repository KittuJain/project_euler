# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def get_multiples_of(number, threshold, sum):
  max_divisible_of_number = threshold / number
  index = 1
  while index < max_divisible_of_number:
    sum += index * number
    index += 1
  return sum

sum = 0
threshold = 1000
sum = get_multiples_of(5, threshold, get_multiples_of(3, threshold, sum))

print(sum)