# reverse a number using while loop without string conversion
	# i/p : 1234
	# o/p : 4321

num = 1234
rev = 0
while num>0:
    last = num%10
    rev = rev * 10 + last
    num//=10
print(rev)