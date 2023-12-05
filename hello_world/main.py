from include import *

if (
    __name__
    == "__main__"
):
    print(
        start_message()
    )
    name = input()
    print(
        hello_name(name)
    )
    print(
        "Введите 3 числа"
    )
    a, b, c = map(
        int,
        (
            input().split()
        ),
    )
    print(
        multiply_vector(
            a, b, c
        )
    )
