def uniqueOccurrences(arr):
    hashmap = {}
    uniq = set()

    for i in arr:
        hashmap[i] = hashmap.get(i, 0)+1

    for i in hashmap.values(): 
        if i in uniq:
            return False
        uniq.add(i)
    return True