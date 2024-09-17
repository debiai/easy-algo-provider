import inspect
import json
import re
from algo_provider.algorithms.my_algorithms import add_floats


def extract_algorithm_metadata(function):
    # Get the docstring of the function (if it exists)
    docstring = function.__doc__

    # Parse function signature using inspect module
    signature = inspect.signature(function)

    # Initialize the structure for the metadata
    algorithm_metadata = {
        "id": function.__name__,
        "name": function.__name__.replace("_", " ").title(),
        "description": (
            docstring.split("\n\n")[0].strip() if docstring else ""
        ),  # Default empty if no docstring
        "inputs": [],
        "outputs": [],
    }

    # Extraction of the Args
    args_descriptions = {}
    if docstring:
        args_section = re.search(r"Args:\s*(.*?)(Returns:|\Z)", docstring, re.DOTALL)
        if args_section:
            args_text = args_section.group(1).strip()
            # Split each argument and description based on indentation
            args_lines = re.split(r"\n\s+", args_text)
            for arg_line in args_lines:
                match = re.match(r"(\w+)\s*\(([^)]+)\):\s*(.*)", arg_line)
                if match:
                    arg_name, arg_type, arg_desc = match.groups()
                    args_descriptions[arg_name] = {
                        "type": arg_type.strip(),
                        "description": arg_desc.strip(),
                    }

    # Gets inputs from function signature
    for param_name, param in signature.parameters.items():
        param_data = args_descriptions.get(param_name, {})

        # Infer type from the function signature if not in docstring
        param_type = param_data.get("type")
        if not param_type:
            param_type = (
                param.annotation.__name__
                if isinstance(param.annotation, type)
                else (
                    str(param.annotation)
                    if param.annotation != inspect._empty
                    else "unknown"
                )
            )

        # Input
        input_metadata = {
            "name": param_name,
            "description": param_data.get("description", ""),
            "type": param_type,
            "default": (
                param.default if param.default != inspect.Parameter.empty else None
            ),
        }
        algorithm_metadata["inputs"].append(input_metadata)

    # Output
    return_type = (
        signature.return_annotation
        if signature.return_annotation != inspect.Signature.empty
        else list
    )
    algorithm_metadata["outputs"].append(
        {
            "name": "result",
            "description": f"The result of {function.__name__}.",
            "type": "array" if return_type == list else "number",
        }
    )

    return algorithm_metadata


def save_metadata_to_json(metadata, file_path):
    with open(file_path, "w") as f:
        json.dump(metadata, f, indent=4)


# Example function (user-defined algorithm)
def moving_average(data: list, periods: int = 3) -> list:
    """Defines the logic of the algorithm

    Args:
        data (list): List of numbers to calculate the moving average on.
        periods (int): Number of periods for the moving average.

    Returns:
        list: The calculated moving average.
    """
    return [
        sum(data[i : i + periods]) / periods for i in range(len(data) - periods + 1)
    ]


# metadata = extract_algorithm_metadata(moving_average)
metadata = extract_algorithm_metadata(add_floats)

file_path = "algo.json"

save_metadata_to_json(metadata, file_path)

print(f"Algorithm metadata saved to {file_path}")
