def main():
    n = int(input())
    stack = MaxStack()

    for _ in range(n):
        query = input()
        try:
            query, value = query.split()
        except ValueError:
            pass

        match query:
            case "push":
                stack.push(value)
            case "pop":
                stack.pop()
            case "max":
                print(stack.max())


class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1][0]:
            self.max_stack.append((value, len(self.stack) - 1))

    def pop(self):
        value = self.stack.pop()
        if len(self.stack) == self.max_stack[-1][1]:
            self.max_stack.pop()
        return value

    def max(self):
        return self.max_stack[-1][0]


if __name__ == "__main__":
    main()
