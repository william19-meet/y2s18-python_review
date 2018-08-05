# Write your solution for 1.4 here!


def is_prime(x):
	i = 2
	while(x > (i-1)):
		i = i + 1
		if(x % i == 0 and x/1 == x):
			print("is prime")
		else:
			print("it isnt prime")


is_prime(7)