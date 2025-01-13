def fizzbuzz(rules=None):
    for i in range(1, 101, 1):
        if isinstance(rules, dict):
            output = ""
            for key, value in rules.items():
                if i % int(key) == 0:
                    output += value
            print(output if output else i)
        else:
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 5 == 0:
                print("Buzz")
            elif i % 3 == 0:
                print("Fizz")
            else :
                print(i)
if __name__ == '__main__':
    fizzbuzz()

