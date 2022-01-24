def recursive_fib(n: int):
    if n < 0: raise ValueError("the number must be non-negative")
    elif n == 0: return 0
    elif n == 1: return 1
    else: return recursive_fib(n - 1) + recursive_fib(n - 2)


def fib(n: int):
    if n < 0: raise ValueError("the number must be non-negative")
    
    lst = [0, 1]
    
    for i in range(n - 1):
        lst.append(lst[-1] + lst[-2])
    
    return lst[n]


def main():
    print(fib(int(input("Number: "))))


if __name__ == '__main__':
    main()
