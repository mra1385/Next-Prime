###    Assignment   ###
#
# Your assignment is to implement the
# following function: `find_next_prime`.
# As the name states, given the number `n` the 
# function should return the next closest prime.
#
# Examples:
#  * `find_next_prime(6)` should return 7.
#  * `find_next_prime(10)` should return 11.
#  * `find_next_prime(11)` should return 13.
#
# You can use whatever you want (data structures,
# language features, etc).
# 
# Unit tests would be a plus. Actually, just knowing what
# they are would be a plus :)
#
### End Assignment  ###
 
# Do your coding here

n = raw_input("What is your number? ")
n = int(n)

def is_prime(n):
    if n <= 1:
        return False
		
    for i in range(2, n):
        if (n % i) == 0:
            return False
			
	return True

def print_next_prime(n):
	number = n
	while True:
		number += 1
		if n <= 1:
			print(2)
			break
		elif is_prime(number):
			print(number)
			break

print_next_prime(n)