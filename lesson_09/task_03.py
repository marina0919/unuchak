# до 13 включительно – детство (childhood);
# от 14 до 34 – молодость (youth);
# от 35 до 59 – зрелость (maturity);
# от 60 – старость (old age).


def call_age(age):
    if not (0 <= age <= 150):
        return "Error. User data was invalid."

    if age <= 13:
        msg = "Childhood"
    elif age <= 34:
        msg = "Youth"
    elif age <= 59:
        msg = "Maturity"
    else:
        "Old age"

    return msg


def main():
    age = int(input("Input your age: "))
    msg = call_age(age)
    print(msg)


main()
