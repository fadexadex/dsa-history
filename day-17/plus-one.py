def plusOne(self, digits):
    digits.reverse()
    
    one, i = 1, 0
    while one:
        if i < len(digits):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                one = 0
        else:
            digits.append(1)
            one = 0
        i += 1
    
    digits.reverse()
    return digits


# def plusOne(self, digits):
#     carry = 1 
#     l = len(digits) - 1 
#     while l >= 0:
#         sum = digits[l] + carry
#         if sum <= 9:
#             digits[l] = sum
#             return digits
#         else:
#             digits[l] = 0
#             l -= 1
#     return [carry] + digits