from typing import Callable, List, Dict, Optional
from easy_algo_provider.utils.parser import extract_algorithm_metadata
from easy_algo_provider.models.algorithm import Algorithm
from easy_algo_provider.app import start_api_server
from rich.console import Console
from rich.panel import Panel


class AlgoProvider:
    def __init__(self):
        self.algorithms: Dict[str, Algorithm] = {}

    def add_algo(
        self,
        func: Callable,
        tags: List[str] = [],
        author: Optional[str] = None,
        version: Optional[str] = None,
        creation_date: Optional[str] = None,
        update_date: Optional[str] = None,
    ) -> Algorithm:
        """
        Adds an algorithm to the provider.

        Parameters:
            func (Callable): The function to add as an algorithm.
            tags (List[str]): The tags of the algorithm.
            version (Optional[str]): The version of the algorithm.
            creation_date (Optional[str]): The creation date of the algorithm.
            update_date (Optional[str]): The update date of the algorithm.

        Returns:
            Algorithm: The algorithm object.
        """
        algo_metadata = extract_algorithm_metadata(func)

        algorithm = Algorithm(
            func=func,
            **algo_metadata,
            tags=tags,
            author=author,
            version=version,
            creationDate=creation_date,
            updateDate=update_date,
        )

        self.algorithms[algorithm.id] = algorithm
        return algorithm

    def get_algorithms(self) -> List[Algorithm]:
        return list(self.algorithms.values())

    def run_algorithm(self, algorithm_id: str, inputs: Dict):
        if algorithm_id not in self.algorithms:
            raise ValueError(f"Algorithm '{algorithm_id}' not found.")
        algorithm = self.algorithms[algorithm_id]
        return algorithm.func(**inputs)

    def start_server(self, host="0.0.0.0", port=8000):
        console = Console()
        console.print(
            Panel(
                "The Easy Algorithm Provider is being started..."
                + f"\n\n[bold]API Server[/bold]: http://{host}:{port}"
                + f"\n[bold]Number of Algorithms[/bold]: {len(self.get_algorithms())}",
                title="Easy Algorithm Provider",
                width=80,
                border_style="bold",
            )
        )
        # Print the creation message of each algorithm
        for algorithm in self.get_algorithms():
            algorithm.print_table()

        start_api_server(self, host, port)
