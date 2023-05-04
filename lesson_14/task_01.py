NUMBER_OF_STUDENT = 3


def calc_mark_avg(mark1, mark2, mark3):
    return (mark1 + mark3 + mark3) / NUMBER_OF_STUDENT


def main():
    mark1 = int(input("Input rating mark1: "))
    mark2 = int(input("Input rating mark2: "))
    mark3 = int(input("Input rating mark3: "))

    avg = calc_mark_avg(mark1, mark2, mark3)
    avg = round(avg, 1)

    msg = f" Group average mark is {avg}"

    print(msg)


if __name__ == '__main__':
    main()
