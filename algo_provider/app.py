from flask import jsonify, request
import connexion
from flask_cors import CORS
import requests
from algo_provider.algo_provider_API import AlgoProviderAPI


PORT = 3020

# Setup app
app = connexion.App(__name__)
app.add_api("Algo_OpenAPI_V0.yaml", strict_validation=True)
CORS(app.app)

algo_api = AlgoProviderAPI("http://localhost:3020/algorithms")


@app.route("/algorithms", methods=["GET"])
def get_algorithms():
    """Endpoint to retrieve a list of algorithms."""
    try:
        algorithms = algo_api.get_algorithms()
        return jsonify(algorithms), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


@app.route("/algorithms/<string:algorithm_id>/run", methods=["POST"])
def run_algorithm(algorithm_id):
    """Endpoint to run an algorithm by its ID."""
    try:
        inputs = request.json.get("inputs", [])
        url = f"{algo_api.url}/algorithms/{algorithm_id}/run"
        response = requests.post(url, json={"inputs": inputs})
        response.raise_for_status()
        return jsonify(response.json()), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Run the service
    # print(
    #     "================ My Algo Service "
    #     + get_app_version()
    #     + " ===================="
    # )
    # init()
    print("============================ RUN ===========================")
    print("App running : http://localhost:{}".format(PORT))
    print("Swagger UI : http://localhost:{}/ui/".format(PORT))
    app.run(port=PORT, debug=True)
