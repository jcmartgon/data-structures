from collections import deque


def main():
    buffer_size, n = map(int, input().split())
    time = 0
    buffer = deque()

    for _ in range(n):
        arrival_time, processing_time = map(int, input().split())

        if arrival_time < time:
            if len(buffer) == buffer_size:
                print(-1)
                continue
            buffer.appendleft(arrival_time)
        else:
            while buffer:
                print(time)
                time += buffer.pop()

        if arrival_time < time:
            if len(buffer) == buffer_size:
                print(-1)
                continue
            buffer.appendleft(arrival_time)
        else:
            print(time)
            time += processing_time


if __name__ == "__main__":
    main()
