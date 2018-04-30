for num in range(1,101):
	string = ""
	if num % 3 == 0:
		string = string + "Fizz"
	if num % 5 == 0:
		string = string + "Buzz"
	if num % 5 != 0 and num % 3 != 0:
		string = string + str(num)
	print(string)
	

# The code shown is a FizzBuzz program code. It shows that multiples of 15 print as 'FizzBuzz' , multiples of 5 print as 'Buzz' , and multiples of 3 print as 'Fizz'. 
# People can use this simple code to not only check if their program is running correctly, but to also practice functions such as Variables and constants, Operators, and Control structures.
