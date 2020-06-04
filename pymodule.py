def sum(x, y):
    return x + y


if __name__ == "__main__":
    import sys
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    result = sum(x, y)
    print(result)
    print(dir())
