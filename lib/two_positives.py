def two_positives(a, b, c):
    if a > 0 and b > 0 and c > 0:
        return False
    elif a > 0 and c > 0:
        return True
    elif b > 0 and c > 0:
        return True
    elif a > 0 and b > 0:
        return True
    else:
        return False
    
print(two_positives(8,9,-2))
print(two_positives(-3,-4,-2))
print(two_positives(1,-1,0))
print(two_positives(-4,9,6))
print(two_positives(8,9,2))