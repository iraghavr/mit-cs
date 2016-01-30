x = 1234567

epsilon = 0.01
numGuesses = 0
low = 0.0
high = x

ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + '; high = ' + str(high) + '; ans = ' + str(ans))
    numGuesses += 1

    if ans**2 > x:
        high = ans
    else:
        low = ans

    ans = (high + low)/2.0

print('guesses: ' + str(numGuesses))
print(str(ans) + ' is close to the square root of ' + str(x))

