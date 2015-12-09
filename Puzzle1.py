import sys
from math import sqrt

def main():
	num = long(raw_input("Please Enter the number:"))
	max_prime_factor = -1
	i = 2
	while i <= num:
		#First Check if it is a factor of num
		isFactor = 0
		while num % i == 0:
			isFactor = 1
			num /= i
		#If it is factor then check for prime
		if isFactor:
			isPrime = 1
			for j in xrange(2, int(sqrt(i))):
				if i % j == 0:
					isPrime = 0
					break
			if isPrime == 1:
				max_prime_factor = i
			if num == 1:
				break
		i = i + 1

	#print the answer
	print(max_prime_factor)
	return max_prime_factor

	

if __name__=="__main__":
	main()
