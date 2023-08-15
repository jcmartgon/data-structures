def main():
    n = int(input())
    a = list(map(int, input().split()))
    swaps = []

    l = len(a) - 1
    for i in range(l, -1, -1):
        j = i
        while j <= l:
            j1 = j * 2 + 1
            j2 = j * 2 + 2

            try:
                kid1 = a[j1]
                kid2 = a[j2]

            except IndexError:
                break

            if kid1 < kid2 and kid1 < a[j]:
                a[j], a[j1] = a[j1], a[j]
                swaps.append((j, j1))
                j = j1

            elif kid2 < kid1 and kid2 < a[j]:
                a[j], a[j2] = a[j2], a[j]
                swaps.append((j, j2))
                j = j2

            else:
                break

    print(len(swaps))
    for swap in swaps:
        print(*swap)


if __name__ == "__main__":
    main()
