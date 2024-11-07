# easy_algo_provider/utils/parser.py

import inspect
from easy_algo_provider.models.algorithm import Algorithm


def parse_algorithm(func):
    # Extract the docstring
    docstring = inspect.getdoc(func)
    # Parse the docstring (you can use docstring_parser library)
    # For simplicity, we'll just assign dummy values here
    algorithm_id = func.__name__
    description = docstring if docstring else "No description provided."
    # Extract input and output annotations
    signature = inspect.signature(func)
    inputs = []
    for name, param in signature.parameters.items():
        input_type = (
            param.annotation.__name__ if param.annotation != inspect._empty else "Any"
        )
        inputs.append({"name": name, "type": input_type})
    output_type = (
        signature.return_annotation.__name__
        if signature.return_annotation != inspect._empty
        else "Any"
    )

    return Algorithm(
        id=algorithm_id,
        name=func.__name__,
        description=description,
        inputs=inputs,
        outputs=[{"name": "result", "type": output_type}],
        func=func,
    )
