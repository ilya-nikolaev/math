def fibonacci_sequence(n: int) -> list[int]:
    if n < 0: raise ValueError("the number must be non-negative")
    
    seq = [0, 1]
    for i in range(n - 1):
        seq.append(seq[-1] + seq[-2])
    
    return seq


def main():
    print(*fibonacci_sequence(10))


if __name__ == '__main__':
    main()
