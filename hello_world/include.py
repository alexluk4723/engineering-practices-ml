import string

import numpy as np


def start_message() -> (
    string
):
    return "Hello, what is your name?"


def hello_name(
    name: string,
) -> string:
    return (
        f"Hello, {name}"
    )


def say_hello_to_name(
    name: string,
):
    print(
        hello_name(name)
    )


def multiply_vector(
    a, b, c
):
    return (
        np.array([a, b])
        * c
    )
