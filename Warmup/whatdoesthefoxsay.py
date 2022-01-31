n = int(input())
for i in range(n):
	if i > 0:
		print()
	sample = input().strip().split(" ")
	sounds = set()
	inp = input()
	while inp != "what does the fox say?":
		sounds.add(inp.strip().split(" ")[-1])
		inp = input()
	for sound in sample:
		if sound not in sounds:
			print(sound, end=" ")