#the function checks for only 2 positve numbers else returns false
def two_positives(a, b, c):
    if a > 0 and b > 0 and c > 0:  # conditional statement when all 3 are positive
        return False
    elif a > 0 and c > 0: # conditional statement when 2 are positive
        return True
    elif b > 0 and c > 0: # conditional statement when 2 are positive
        return True
    elif a > 0 and b > 0: # conditional statement when 2 are positive
        return True
    else:
        return False     #if not exactly 2 positives return false

        # example outputs of function to terminal    
print(two_positives(8,9,-2))
print(two_positives(-3,-4,-2))
print(two_positives(1,-1,0))
print(two_positives(-4,9,6))
print(two_positives(8,9,2))