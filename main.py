
from cost_function_definition import f, f_prime, f_double_prime


def minimize(f0, f1, f2, guess, epsilon):
    #xn+1 = x0 - f'(x0)/f''(x0)


    #print str(f0(guess)) + " is minimized at " + str(guess)
    if f0(guess) == 0:
        return "f0 is zero"
    if f1(guess) == 0:
        return "f1 is zero"
    if f2(guess) == 0:
        return "undefined"
    if guess > epsilon:
        minimize(f1, f2, guess - f1(guess)/f2(guess), epsilon)
    else:
        return guess
    print(guess)
    return guess




minimize(f, f_prime, f_double_prime, 0, 0.000001)
