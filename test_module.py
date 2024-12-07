from easy_algo_provider import AlgoProvider


provider = AlgoProvider()


# 0 : Simplest example
def my_algo_0(input1, input2):
    return input1 + input2


provider.add_algo(my_algo_0)


# 1 : Example with type hints
def my_algo_1(input1: int, input2: int) -> int:
    return input1 + input2


provider.add_algo(my_algo_1)


def my_algo_2(input1: int, input2: int) -> int:
    """
    This is a simple algorithm that adds two numbers together.

    Parameters:
        input1 (int): The first number to add.
        input2 (int): The second number to add.

    Returns:
        int: The sum of the two numbers.
    """
    return input1 + input2


provider.add_algo(my_algo_2)


def my_algo_3(input1: int, input2: int) -> int:
    """
    This is a simple algorithm that adds two numbers together.

    Parameters:
        input1 (int): The first number to add.
        input2 (int): The second number to add.

    Returns:
        int: The sum of the two numbers.
    """
    return input1 + input2


algo = provider.add_algo(
    my_algo_3,
    author="DebiAI",
    version="1.0.0",
    creation_date="2024-01-01",
    update_date="2024-01-01",
    tags=["Math", "Addition"],
)

print(algo)

provider.start_server()
