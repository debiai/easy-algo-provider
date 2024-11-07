# easy_algo_provider/models/algorithm.py

from dataclasses import dataclass, field
from typing import List, Callable, Dict, Any


@dataclass
class Algorithm:
    id: str
    name: str
    description: str
    inputs: List[Dict[str, Any]]
    outputs: List[Dict[str, Any]]
    func: Callable = field(repr=False)
