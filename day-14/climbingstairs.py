# - one , two = 1, 1
# - curr_sum = 0 
# - for i  range(n) -> 2 time
#     - curr_sum = one + two
#     - two = one 
#     - one = curr_sum
# - return curr_sum


def climbStairs(self, n: int) -> int:
    if n <= 2:
        one, two = 1, 1
        curr_sum = 0

    for i in range(n-1):
        curr_sum = one + two
        two = one
        one = curr_sum
    return curr_sum
    



# store = {}
# steps= [1, 2]
# store[0] = 1

# for i in range(1, n + 1):
#     for step in steps:
        
#         subproblem = i - step
#         if subproblem < 0:
#             continue
#         store[i] = store[i] + store[subproblem]

# return store[n]    



