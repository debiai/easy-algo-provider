import inspect
import re
from easy_algo_provider.models.algorithm import Algorithm

TYPE_MAPPING = {
    "int": "number",
    "float": "number",
    "str": "string",
    "bool": "boolean",
    "Any": "any",
}


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

    # Extraction of the function arguments with their types and descriptions
    args_descriptions = {}
    if docstring:
        # This regular expression match the parameters in the docstring of the function
        # It looks for a word followed by a colon and the type in parenthesis
        pattern = re.compile(r"(\w+)\s*\(([^)]+)\):\s*([^\n]+)")

        for match in pattern.finditer(docstring):
            param_name = match.group(1)
            param_type = match.group(2)
            param_description = match.group(3)

            args_descriptions[param_name] = {
                "type": TYPE_MAPPING.get(param_type, param_type),
                "description": param_description,
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


def parse_algorithm(func):
    # Extract the function metadata
    metadata = extract_algorithm_metadata(func)

    # Create an Algorithm object
    algorithm = Algorithm(
        **metadata,
        func=func,
        version="0.1.0",
        creationDate="2023-01-01",
    )

    return algorithm
