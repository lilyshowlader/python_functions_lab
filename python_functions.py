# Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

# def sum_to(n):
# #   #returns the sum of the integers from 1 to n.
#   print(n * (n + 1) // 2)

# sum_to(6)  # returns 21
# sum_to(10) # returns 55



# Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(nums):
  nums.sort()
  return nums[-1]

print(largest([1, 2, 3, 4, 0]))  # returns 4
print(largest([10, 4, 2, 231, 91, 54]))

# Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.


def occurances(string1, string2):
  return string1.count(string2)
	
print(occurances('fleep floop', 'e'))   # returns 2
print(occurances('fleep floop', 'p') )  # returns 2



# Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product

print(product(-1, 4)) # returns -4
print(product(2, 5, 5)) # returns 50
print(product(4, 0.5, 5)) # returns 10.0