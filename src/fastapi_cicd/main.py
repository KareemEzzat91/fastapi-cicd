from fastapi import FastAPI

from fastapi_cicd import __version__

app = FastAPI(
    title="fastapi-cicd",
    version=__version__,
    description="Minimal FastAPI service for CI/CD and cloud deployment practice.",
)


@app.get("/", tags=["root"])
def read_root() -> dict[str, str]:
    """Return basic service metadata."""
    return {
        "service": "fastapi-cicd",
        "version": __version__,
        "status": "running",
    }


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    """Return service health status for readiness and liveness probes."""
    return {"status": "ok"}
