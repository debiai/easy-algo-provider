import requests


class AlgoProviderAPI:

    def __init__(self, url):
        self.url = url

    def get_algorithms(self):
        """Retrieve a list of algorithms from the API."""
        response = requests.get(self.url)
        response.raise_for_status()
        return response.json()

    def run_algorithms(self):
        """Run all algorithms from the API."""
        algorithms = self.get_algorithms()
        for algorithm in algorithms:
            response = requests.post(f"{self.url}/{algorithm['id']}/run")
            response.raise_for_status()

        return response.json()
