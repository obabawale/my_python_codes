def fibonacci(n):
	number = {}
	number[1] = 1
	number[2] = 1
	print (1, ":", number[1])
	print (2, ":", number[2])
	for i in range (3, n):
		number[i] = number[i - 1] + number[i - 2]
		print (i, ":", number[i])

if __name__ == "__main__":
	n = int(input("Enter the range for the fibonacci sequence: "))
	fibonacci(n)
