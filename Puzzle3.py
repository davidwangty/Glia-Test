import sys
from math import sqrt

#Record the Combination we already compute
global Combin_table
Combin_table = {}

def Combination(n, r):
	if r == 1:
		return n
	elif n == r:
		return 1
	else:
		#If it is not compute before
		if Combin_table[n - 1][r - 1] == -1:
			result = Combination(n - 1, r) + Combination(n - 1, r - 1)
			Combin_table[n - 1][r - 1] = result
			return result
		else:
			return Combin_table[n - 1][r - 1]

def main():
	num1 = int(raw_input("Please Enter the number of n:"))
	num2 = int(raw_input("Please Enter the number of r:"))
	#Init the table
	for i in range(num1):
		Combin_table[i] = {}
		for j in range(num2):
			Combin_table[i][j] = -1
	result = Combination(num1, num2)

	print(result)
	return result
	

if __name__=="__main__":
	main()
