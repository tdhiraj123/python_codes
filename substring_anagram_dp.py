 
def countOfAnagramSubstring(s): 

	n = len(s) 
	mp = {} 
	for i in range(n): 
		sb = '' 
		for j in range(i, n): 
			sb = ''.join(sorted(sb + s[j])) 
			mp[sb] = mp.get(sb, 0) 
			mp[sb] += 1

	anas = 0
	for v in mp.values(): 
		anas += (v*(v-1))//2
        
	return anas
s = "abcbca"
print(countOfAnagramSubstring(s)) 

