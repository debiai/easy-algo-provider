# user_script.py

from easy_algo_provider import AlgoProvider


def my_algo1(input1: int, input2: int) -> int:
    """
    This is a simple algorithm that adds two numbers together.

    Parameters:
        input1 (int): The first number to add.
        input2 (int): The second number to add.

    Returns:
        int: The sum of the two numbers.
    """
    return input1 + input2


provider = AlgoProvider()
provider.add_algo(my_algo1)
provider.start_server()
