def catalan_sequence(n: int) -> list[int]:
    if n < 0: raise ValueError("the number must be non-negative")
    
    seq = [1]
    for i in range(1, n + 1):
        seq.append(sum(e * seq[i - 1 - j] for j, e in enumerate(seq)))
    
    return seq


def main():
    print(*catalan_sequence(10))


if __name__ == '__main__':
    main()
