def sumOfNatureNumber(num):
    if num == 1:
        return 1
    
    return num + sumOfNatureNumber(num - 1)

print(sumOfNatureNumber(10))