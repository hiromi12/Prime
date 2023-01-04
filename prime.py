# Prime Checker
# Date: Sep 7, 2022
# Author: Hiromi Honda

# Program Description: 
# Function 'prime' is a bool function that tells you the parameter n is a prime or not.
# Function 'max_prime_in_ramge' is a function that tells you maximum prime number in the range that you put onto parameter of it.
# It also tells you all prime numbers in the range and the number of the prime numbers.

def prime(n):
  if n < 2:
    return False
  for i in range(2, int(n ** 0.5 + 1)):
    if n % i == 0:
      return False
  return True

def max_prime_in_range(a, b):
  counter = 0
  prime_array = []
  for i in range(a, b):
    if prime(i) == True:
      max_prime = i
      prime_array.append(i)
      counter += 1
  print("Primes: "+str(prime_array))
  print("The number of prime numbers: "+str(counter))
  print("Max Prime: "+str(max_prime))

max_prime_in_range(500, 1000)

# Output
# 
# Primes: [503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
# The number of prime numbers: 73
# Max Prime: 997
# 