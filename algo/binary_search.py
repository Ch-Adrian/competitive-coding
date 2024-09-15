
def binary_search(l: list, target: int) -> int:
    
    low = 0
    high = len(l)-1
    while low <= high:
        mid = (low+high)//2
        if l[mid] == target:
            return mid
        elif l[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1 

if __name__ == "__main__":
    if 7 == binary_search([1,2,3,4,5,6,7,8,9], 8):
        print("true")
    else:
        print("false")
    if -1 == binary_search([1,2,3,4,5,6,7,8,9], 20):
        print("true")
    else:
        print("false")
