def plusOne(self, digits):
    carry = 1 
    l = len(digits) - 1 
    while l >= 0:
        sum = digits[l] + carry
        if sum <= 9:
            digits[l] = sum
            return digits
        else:
            digits[l] = 0
            l -= 1
    return [carry] + digits