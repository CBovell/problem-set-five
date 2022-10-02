import math

def findvalue(list, value, correctionValue):
    left = 0
    right = len(list)-1

    if len(list) == 0:
        return -1
    
    if list[left] == value:
        return left
    elif list[right] == value:
        return right

    while (right>left) and (right<=len(list)) and {left>= 0}:
        mid = math.floor(right+left)

        if list[mid] == value and list[mid+correctionValue] != value:
            return mid
        
        elif list[mid] > value:
            right = mid-1
        
        elif list[mid] < value:
            left = mid+1
    return -1

def findstart(list, value):
    findvalue(list,value,-1)

def findend(list,value):
    findvalue(list,value,1)

def count(list, value):
    lowBound=findstart(list,value)
    highBound=findend(list,value)
    return [lowBound,highBound]

    
