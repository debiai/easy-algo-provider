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


provider.add_algo(
    my_algo_3,
    author="DebiAI",
    version="1.0.0",
    creation_date="2024-01-01",
    update_date="2024-01-01",
    tags=["Math", "Addition"],
)


def algo_array_input(list_input) -> int:
    """
    This is a simple algorithm that adds all the numbers in a list.

    Parameters:
        list_input (list): The list of numbers to add.

    Returns:
        int: The sum of the numbers in the list.
    """
    return sum(list_input)


provider.add_algo(algo_array_input)


def algo_array_input2(list_input: list) -> int:
    """
    This is a simple algorithm that adds all the numbers in a list.

    Parameters:
        list_input (list): The list of numbers to add.

    Returns:
        int: The sum of the numbers in the list.
    """
    return sum(list_input)


provider.add_algo(algo_array_input2)


def algo_array_input3(list_input: list[int]) -> int:
    """
    This is a simple algorithm that adds all the numbers in a list.

    Parameters:
        list_input (list): The list of numbers to add.

    Returns:
        array[int]: The sum of the numbers in the list.
    """
    # Multiply by
    list_input = [x * 2 for x in list_input]
    return list_input


provider.add_algo(algo_array_input3)


provider.start_server()
