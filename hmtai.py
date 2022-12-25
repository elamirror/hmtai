from hmtai import get as img
from requests import get

from threading import Thread, Lock

category = input("TAG(s): ")
count = int(input("COUNT: "))
print()
c = 1
d = 1
ded = []
def download():
	global d
	ded.append((get(img("nekobot", el)).content))
	locker.acquire()
	d += 1
	print(f"\rDOWNLOADED: {d}", end = "")
	locker.release()


def main():
	global c
	for el in ded:
		f = open(f"/storage/emulated/0/DCIM/Camera/{c}.gif", "wb")
		f.write(el)
		print(f"\rDONE: {c}", end = "")
		c += 1

if __name__ == "__main__":
	locker = Lock()
	threads = []
	for el in category.split():
		for _ in range(count):
			thread = Thread(target = download)
			threads.append(thread)
		for t in threads:
			t.start()
		for t in threads:
			t.join()
		threads = []
	print()
	main()
