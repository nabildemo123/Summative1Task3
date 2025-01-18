# /15 = FizzBuzz
# /3 = Fizz
# /5 = Buzz
# anything else output the number

def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 ==0:
        return "Buzz"
    else:
        return str(n)