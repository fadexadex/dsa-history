def firstUniqChar(self, s: str) -> int:
    car = {} 
    for char in s:
    car[char] = car.get(char,0) +1

    for i, char in enumerate(s):
        if count[char] = 1:
            return i

    return -1 
