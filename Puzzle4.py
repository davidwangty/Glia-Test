def anonymous(x):

    return x**2 + 1


def integrate(fun, start, end):

    step = 0.1

    intercept = start

    area = 0

    while intercept < end:

        intercept += step

        # Implement of the graph 3 in the puzzle
        area += step * fun(intercept)

    return area


def main():
    print(integrate(anonymous, 0, 10))


if __name__ == "__main__":
    main()
