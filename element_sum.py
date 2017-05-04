#Algorithm to check the total of ways 2 elements of an array can sum to a given K

a = [5,7,3,6,14,10,1,9,2,8,12]

a.sort()
# a = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 14]


K = 6

start = 0
end = len(a) - 1

count = 0

for i in range(len(a)):
	if a[start] + a[end] > K:
		end = end -1

	elif a[start] + a[end] < K:
		start = start + 1

	else:
		print "Element:", a[start], "and", a[end]
		count +=1
		start = start + 1

	if start == end:
		break

print "Total ways:", count
