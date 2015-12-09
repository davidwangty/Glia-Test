import sys

global NUM 
global FIRST_FACTOR
global SECOND_FACTOR
NUM = 1000
FIRST_FACTOR = 3
SECOND_FACTOR = 5

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

def main():
	result = 0
	temp = 0
	#Sum of multiples of FIRST_FACTOR
	for i in range(int(NUM / FIRST_FACTOR)):
		temp += i + 1
	temp *=  FIRST_FACTOR
	result += temp
	temp = 0
	#Use to delete multiples of both FIRST_FACTOR and SECOND_FACTOR
	lcm_factor = lcm(FIRST_FACTOR, SECOND_FACTOR) / SECOND_FACTOR
	#Sum of multiples of SECOND_FACTOR
	for i in range(int(NUM / SECOND_FACTOR)):
		if i + 1 % lcm_factor != 0:
			temp += i + 1
	temp *= SECOND_FACTOR
	result += temp

	print(result)
	return result

	

if __name__=="__main__":
	main()
