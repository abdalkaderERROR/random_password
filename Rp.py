import string
import random
import pyfiglet

#print(dir(string))
def s(cunt):
	l = string.ascii_letters + string.hexdigits 
	#print(l)
	le = len(l)
	#print(le)
	li = []
	while cunt >0:
		rand = random.randrange(0,le -1)
		n = l[rand]
		li.append(n)
		cunt-=1
	return "".join(li)

log = pyfiglet.figlet_format("E R R OR 4 0 4")
print(log)

while True:
	print("_"*60)
	print()
	i_n = int(input("inter len pass word: "))
	print("_"*60)
	print()
	print(s(i_n))
