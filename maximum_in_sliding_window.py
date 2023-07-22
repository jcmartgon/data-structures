def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    window = a[:m]

    for i, elem in enumerate(a[m:]):
        print(max(window[i : i + m]), end=" ")
        window.append(elem)

    print(max(window[i : i + m]))


if __name__ == "__main__":
    main()
