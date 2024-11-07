from typing import Callable, List, Dict
from easy_algo_provider.utils.parser import parse_algorithm
from easy_algo_provider.models.algorithm import Algorithm
from easy_algo_provider.app import start_api_server


class AlgoProvider:
    def __init__(self):
        self.algorithms: Dict[str, Algorithm] = {}

    def add_algo(self, func: Callable):
        algo = parse_algorithm(func)
        self.algorithms[algo.id] = algo

    def get_algorithms(self) -> List[Algorithm]:
        return list(self.algorithms.values())

    def run_algorithm(self, algorithm_id: str, inputs: Dict):
        if algorithm_id not in self.algorithms:
            raise ValueError(f"Algorithm '{algorithm_id}' not found.")
        algorithm = self.algorithms[algorithm_id]
        return algorithm.func(**inputs)

    def start_server(self, host="0.0.0.0", port=8000):
        start_api_server(self, host, port)
