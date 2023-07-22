def main():
    print(check_brackets(input()))


def check_brackets(s):
    symbols = {")": "(", "]": "[", "}": "{"}
    queued = []

    for i, c in enumerate(s):
        if c in ["(", "[", "{"]:
            queued.append((i, c))
        if c in [")", "]", "}"]:
            if symbols[c] != queued[-1][1]:
                return i + 1
            else:
                queued.pop()
    if queued:
        return queued[-1][0] + 1
    return "Success"


if __name__ == "__main__":
    main()
