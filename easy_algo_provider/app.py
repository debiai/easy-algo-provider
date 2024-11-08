import uvicorn
from fastapi import FastAPI, HTTPException
from typing import List, Dict, Any
from easy_algo_provider.models.algorithm import Algorithm
from fastapi.middleware.cors import CORSMiddleware

APP_VERSION = "0.1.0"


def start_api_server(provider, host, port):
    app = FastAPI(
        title="Algo API",
        version=APP_VERSION,
        description="API for algorithm provider",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/algorithms", response_model=List[Algorithm])
    def get_algorithms():
        return provider.get_algorithms()

    @app.post("/algorithms/{algorithm_id}/run")
    def run_algorithm(algorithm_id: str, inputs: Dict[str, Any]):
        try:
            result = provider.run_algorithm(algorithm_id, inputs)
            return {"outputs": result}
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    uvicorn.run(app, host=host, port=port)
