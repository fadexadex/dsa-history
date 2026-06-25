lucky = -1
freq = {}

for i in arr:
    freq[i] = freq.get(i, 0) + 1
for i, j in freq.items():
    if i == j:
        lucky = max(lucky, i)
return lucky




lucky = -1
freq = {}

for i in arr:
    freq[i] = freq.get(i, 0) + 1
for i, j in freq.items():
    if i == j:
        lucky = max(lucky, i)
return lucky