# backspaceCompare inefficient solution

def backspaceCompare(self, s: str, t: str) -> bool:
    list_s = []  s = "ab#c" -> [a, c]
    list_t = [] -> (s+t) -> O(n)
    
    
    for char in s:
        
        if list_s and char == '#':
            list_s.pop()
        elif:
          list_s.append(char)

    for char in t:
      if list_t and char == '#':
            list_t.pop()
        elif:
          list_t.append(char)

return list_s == list_t -> [a, c] == [a, c] 
            

# climbStairs (dp solution)
def climbStairs(self, n):
    if n == 0 or n == 1:
        return 1
    return climbStairs(n - 1)  +  climbStairs(n-2)

# climbStairs (memoization solution)
def climbStairs(self, n):
    memo = {}
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    memo[n] = climbStairs(n - 1)  +  climbStairs(n-2)
    return memo[n]