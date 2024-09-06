def main():
    plate=input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    # plate has to be betweeen length 2 and 6
    if len(s)<2 or len(s)>6:
        return False
    
    # first two characters in plate have to be letters not numbers 
    if s[0].isalpha()==False or s[1].isalpha()==False:
        return False 
    
    # if the 0th part of the string is not part of the alphabet, then run next line of code, which says if that 0th part of the string is the number zero, return false since the first number cannot be zero. If that 0th part of the string is not zero, then break the while loop. If the 0th part of the string is part of the alphabet then move onto the 1st part of the string (seen with i+=1) and run this code over again. 
    i=0
    while i<len(s):
        if s[i].isalpha()==False:
            if s[i]=="0":
                return False 
            else:
                break
        i += 1

    # plate cannot have period, space, or punctuation marks   
    for c in s:
        if c in [".", " ", "!", "?"]:
            return False
    
    # plate cannot have numbers in between letters 
    i=0
    while i<len(s):
        if s[i].isalpha()==True:
            i+=1
        else:
            while i<len(s):
                if s[i].isalpha()==False:
                    i += 1
                else:
                    return False 
    
    # If we pass all the tests, return True 
    return True

main()
