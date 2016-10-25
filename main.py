
from cost_function_definition import f, f_prime, f_double_prime


def minimize(f0, f1, f2, guess, epsilon):
    #print str(f0(guess)) + " is minimized at " + str(guess)
    if f0 == 0:
        return "f0 is zero"
    if f1 == 0:
        return "f1 is zero"
    if f2 == 0:
        return "f2 is zero"
    while guess > epsilon:
        epsilon = guess - f1(guess)/f2(guess)
        guess = abs(0 - f(guess))
    return guess




minimize(f, f_prime, f_double_prime, 0, 0.000001)
