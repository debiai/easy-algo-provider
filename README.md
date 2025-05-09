# Algo Provider Python module

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

This Algo-Provider Python module allows you to easily deploy your own algorithm through the Algo Provider API.

## What is an Algo Provider?

An Algo Provider is a service that provides algorithms to be used by different applications such as [DebiAI](https://debiai.irt-systemx.fr/) or any other application that uses the Algo Provider API.

Creating an algo-provider requires to create a server, it requires some skills and a lot of time.

The goal of this project is to create a new solution that makes it easier to start an algo-provider, without the need for Docker or advanced developer skills. The targets are Data Scientists that want to use their algorithms with DebiAI.

## Getting started

Install the module with pip:

```bash
pip install algo-provider
```

Then, create a Python file with the following content:

```python
# First define your algorithm following a strict docstring format
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

# Then create an AlgoProvider object and add your algorithm to it
from algo_provider import AlgoProvider
provider = AlgoProvider()
provider.add_algo(my_algo1)

# Finally, start the server
provider.start_server()
```

Run the Python file and your algorithm is now available through the Algo Provider API!

![Expected output](./result.png)

The content of the docstring will be used to generate Algo descriptions in the DebiAI interface, and the function will be called with the parameters provided by the user. The return value will be sent back to the user and displayed in the DebiAI interface.

## Parameters

You can specify the following parameters when adding an algorithm:

```python
provider.add_algo(
    my_algo_3,
    author="DebiAI",
    version="1.0.0",
    creation_date="2024-01-01",
    update_date="2024-01-01",
    tags=["Math", "Addition"],
)
```
