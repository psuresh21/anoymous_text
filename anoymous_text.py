import datetime

print("---------------------------------------------------------")
mydt = datetime.datetime.now()
print("welcome to anoymous text")
print("it will anoymous text to original text")
print("Copyright (c) " + mydt.strftime("%Y") + " Suresh Pandiyan \n")

print("welcome to anoymous text \n")
ask_q = str(input("enter the file path: \n"))

moo = []

def readthedata(filename):
	try:
		with open(filename) as f:
			for m in f:
				moo.append(m)
				
	except IOError as ioerr:
		return(ioerr)


y = readthedata(ask_q)

		
s = []

def lostryi():
	for n in range(0, len(moo)):
		#iop = y[n]
		iop = moo[n].replace("1","a").replace(".."," ").replace("6","f").replace("aa","11").replace("11","k").replace("af","p").replace("2","b").replace("7","g").replace("ab","l").replace("1","a").replace("3","c").replace("8","h").replace("ac","m").replace("ah","r").replace("4","d").replace("9","i").replace("ad","n").replace("ai","s").replace("5","e").replace("a0","j").replace("ae","o").replace("b0","t").replace("ba","u").replace("bb","v").replace("bc","w").replace("bd","x").replace("be","y").replace("bf","z")
		k = iop.split('.')
		m = ''.join(k)
		#l = m.split(',')
		s.append(str(m))

lostryi()

repls = ''.join(s).replace("ag","q")

print(repls)	
