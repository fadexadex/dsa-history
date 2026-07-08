def checkIfPangram(self, sentence):
        read = set(sentence)
        if len(read) == 26:
            return True
        return False
        

        # known = "abcdefghijklmnopqrstuvwxyz"
        # for letter in known:
        #     if letter not in sentence:
        #         return False
        # return True

# set the list of letters to 26
# if you count a sentemce and it is not equal to 26,
# you know it's false
# if it is more than 26, use a set to store the seen letters
# we can have more than 26 letters in a sentence, 
# and it is possible that we don't have a particular letter in it

# so i can use a len to count the number of letter in a sentence
# and i can use a set that will make it to be equal to 26