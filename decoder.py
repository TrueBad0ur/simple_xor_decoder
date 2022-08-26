# decoder

initial_byte = 0x41			# CHANGE IT

arr = [39, 75, 42, 77, 54, 94, 109, 1, 109, 93, 2, 123, 72, 41, 84]			# CHANGE IT

print(chr(initial_byte ^ arr[0]), end="")

for i in range(len(arr)):
	first = arr[i] ^ arr[i+1]
	print(chr(first), end="")
	if i+2 == len(arr):
		break