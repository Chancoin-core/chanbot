import basc_py4chan
from subprocess import call

board = basc_py4chan.Board('biz')
chanthread = 3118874
chanthread = board.get_thread(chanthread)
#posts = thread.posts
found_addys = []

def has_doubles(n,dub):
	return(len(set((str(n))[-dub:])) < 2)

def send_coins(address, amount):
	call(["./chancoind", "sendtoaddress", str(address), str(amount)])

while True:
	allthreads = board.get_all_thread_ids()
	for x in range(len(allthreads)):	
		thread = board.get_thread(allthreads[x])
		if type(thread) != type(None):
			posts = thread.posts
#			print("Scanning", thread)
			for i in range(len(posts)):
				currentpost = posts[i]
				currentnum = currentpost.post_number
#				if "$4CHN:" in currentpost.name and currentpost.name not in open("bot.txt","r").read():
				if type(currentpost.name) == str and "$4CHN:" in currentpost.name and str(currentnum) not in open("bot.txt", "r").read() and has_doubles(currentnum,2):
					addy = currentpost.name.replace("$4CHN:", "")
					print("Found addy", addy, "with GET", currentnum, "in thread", thread)
					send_coins(addy, 0.5)
					print("Coins sent to ", addy)
					print("------")
					open("bot.txt","a").write(str(currentnum))
#				elif str(currentnum) in open("bot.txt", "r").read():
#					print("Found post ", currentnum, "but it is already in bot.txt. Skipping")
#					print("-------")
#	print("Scanning again..")

