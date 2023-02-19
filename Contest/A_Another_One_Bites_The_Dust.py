data = list(map(int, input().split()))

if data[0] == data[1]:
	print(data[0] + data[1] + (data[2] * 2))
elif data[0] > data[1]:
	print(data[1] + data[1] + 1 + (data[2] * 2))
else:
	print(data[0] + data[0] + 1+  (data[2] * 2))