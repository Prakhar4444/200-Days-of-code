def raisetopower( base_n , pow_n):
    result = 1
    for index in range(pow_n) :
        result = result * base_n
    return result
print(raisetopower(2,4))