"""
Simple Python 2.7 program that checks if a manually input integer is prime.
MemoryError will be encountered for integers with 10 or more digits.
"""


#That prime checking function.
def is_prime(x):
    # Checks to see if the number can't possibly be a prime.
    if x < 2:
        if x == 0 or x == 1:
            return str(x) + " is NOT a prime number. It is an identity element."


        print "Negative numbers are and are not primes. I hope this was helpful."/n
     # Checks to see if x is a composite number.
    else:
        for fac in range(2,x):
            if x % fac == 0:
                return str(x) + " is not a prime number, but it IS primely composed."

    return str(x) + " is prime time!"

print "Welcome to Primecheck5001!"  # Glorious welcome!
print " "
print "Type 'done' when you've had enough priming."
print " "

while True:
	p = raw_input("Give meh a numbah!") # Input that stuff!
	print " "

	if p == "done":
		break
	s = int(p)                          # From string to integer.
	print is_prime(s)
quit()
