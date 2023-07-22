def main():
    n = int(input())
    parents = set([x for x in input().split() if x != "-1"])

    print(len(parents) + 1)


if __name__ == "__main__":
    main()
